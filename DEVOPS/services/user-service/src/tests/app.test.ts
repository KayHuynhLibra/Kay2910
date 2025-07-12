import request from 'supertest';
import express from 'express';
import { Pool } from 'pg';
import Redis from 'ioredis';
import { createLogger } from 'winston';

// Mock dependencies
jest.mock('pg');
jest.mock('ioredis');
jest.mock('winston');

describe('User Service', () => {
  let app: express.Application;
  let mockPool: jest.Mocked<Pool>;
  let mockRedis: jest.Mocked<Redis>;

  beforeEach(() => {
    // Reset mocks
    jest.clearAllMocks();

    // Setup mock pool
    mockPool = {
      query: jest.fn(),
    } as any;

    // Setup mock redis
    mockRedis = {
      get: jest.fn(),
      setex: jest.fn(),
      del: jest.fn(),
    } as any;

    // Create app instance
    app = express();
    app.use(express.json());

    // Add test routes
    app.get('/api/users', async (req, res) => {
      try {
        const cacheKey = 'users:all';
        const cachedUsers = await mockRedis.get(cacheKey);

        if (cachedUsers) {
          return res.json(JSON.parse(cachedUsers));
        }

        const result = await mockPool.query('SELECT * FROM users');
        await mockRedis.setex(cacheKey, 3600, JSON.stringify(result.rows));
        res.json(result.rows);
      } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
      }
    });

    app.get('/api/users/:id', async (req, res) => {
      try {
        const { id } = req.params;
        const cacheKey = `users:${id}`;
        const cachedUser = await mockRedis.get(cacheKey);

        if (cachedUser) {
          return res.json(JSON.parse(cachedUser));
        }

        const result = await mockPool.query('SELECT * FROM users WHERE id = $1', [id]);
        
        if (result.rows.length === 0) {
          return res.status(404).json({ error: 'User not found' });
        }

        await mockRedis.setex(cacheKey, 3600, JSON.stringify(result.rows[0]));
        res.json(result.rows[0]);
      } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
      }
    });

    app.post('/api/users', async (req, res) => {
      try {
        const { name, email } = req.body;
        const result = await mockPool.query(
          'INSERT INTO users (name, email) VALUES ($1, $2) RETURNING *',
          [name, email]
        );
        
        await mockRedis.del('users:all');
        
        res.status(201).json(result.rows[0]);
      } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
      }
    });
  });

  describe('GET /api/users', () => {
    it('should return users from cache if available', async () => {
      const mockUsers = [{ id: 1, name: 'Test User', email: 'test@example.com' }];
      mockRedis.get.mockResolvedValue(JSON.stringify(mockUsers));

      const response = await request(app).get('/api/users');

      expect(response.status).toBe(200);
      expect(response.body).toEqual(mockUsers);
      expect(mockRedis.get).toHaveBeenCalledWith('users:all');
      expect(mockPool.query).not.toHaveBeenCalled();
    });

    it('should fetch users from database if not in cache', async () => {
      const mockUsers = [{ id: 1, name: 'Test User', email: 'test@example.com' }];
      mockRedis.get.mockResolvedValue(null);
      mockPool.query.mockResolvedValue({ rows: mockUsers } as any);

      const response = await request(app).get('/api/users');

      expect(response.status).toBe(200);
      expect(response.body).toEqual(mockUsers);
      expect(mockRedis.get).toHaveBeenCalledWith('users:all');
      expect(mockPool.query).toHaveBeenCalledWith('SELECT * FROM users');
      expect(mockRedis.setex).toHaveBeenCalledWith('users:all', 3600, JSON.stringify(mockUsers));
    });
  });

  describe('GET /api/users/:id', () => {
    it('should return user from cache if available', async () => {
      const mockUser = { id: 1, name: 'Test User', email: 'test@example.com' };
      mockRedis.get.mockResolvedValue(JSON.stringify(mockUser));

      const response = await request(app).get('/api/users/1');

      expect(response.status).toBe(200);
      expect(response.body).toEqual(mockUser);
      expect(mockRedis.get).toHaveBeenCalledWith('users:1');
      expect(mockPool.query).not.toHaveBeenCalled();
    });

    it('should return 404 if user not found', async () => {
      mockRedis.get.mockResolvedValue(null);
      mockPool.query.mockResolvedValue({ rows: [] } as any);

      const response = await request(app).get('/api/users/999');

      expect(response.status).toBe(404);
      expect(response.body).toEqual({ error: 'User not found' });
    });
  });

  describe('POST /api/users', () => {
    it('should create new user and invalidate cache', async () => {
      const newUser = { name: 'New User', email: 'new@example.com' };
      const createdUser = { id: 1, ...newUser };
      mockPool.query.mockResolvedValue({ rows: [createdUser] } as any);

      const response = await request(app)
        .post('/api/users')
        .send(newUser);

      expect(response.status).toBe(201);
      expect(response.body).toEqual(createdUser);
      expect(mockPool.query).toHaveBeenCalledWith(
        'INSERT INTO users (name, email) VALUES ($1, $2) RETURNING *',
        [newUser.name, newUser.email]
      );
      expect(mockRedis.del).toHaveBeenCalledWith('users:all');
    });
  });
}); 
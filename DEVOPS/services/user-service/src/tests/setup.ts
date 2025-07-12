import { Pool } from 'pg';
import Redis from 'ioredis';

// Mock console methods to keep test output clean
global.console = {
  ...console,
  log: jest.fn(),
  error: jest.fn(),
  warn: jest.fn(),
  info: jest.fn(),
  debug: jest.fn(),
};

// Mock environment variables
process.env = {
  ...process.env,
  NODE_ENV: 'test',
  PORT: '3000',
  POSTGRES_HOST: 'localhost',
  POSTGRES_PORT: '5432',
  POSTGRES_USER: 'test',
  POSTGRES_PASSWORD: 'test',
  POSTGRES_DB: 'test',
  REDIS_HOST: 'localhost',
  REDIS_PORT: '6379',
};

// Mock database and cache connections
jest.mock('pg', () => ({
  Pool: jest.fn(() => ({
    query: jest.fn(),
    connect: jest.fn(),
    end: jest.fn(),
  })),
}));

jest.mock('ioredis', () => {
  return jest.fn().mockImplementation(() => ({
    get: jest.fn(),
    setex: jest.fn(),
    del: jest.fn(),
    quit: jest.fn(),
  }));
});

// Clean up after each test
afterEach(() => {
  jest.clearAllMocks();
}); 
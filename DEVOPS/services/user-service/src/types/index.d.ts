declare namespace Express {
  export interface Request {
    user?: {
      id: number;
      name: string;
      email: string;
    };
  }
}

interface User {
  id: number;
  name: string;
  email: string;
  created_at?: Date;
  updated_at?: Date;
}

interface CreateUserDTO {
  name: string;
  email: string;
}

interface UpdateUserDTO {
  name?: string;
  email?: string;
}

interface DatabaseConfig {
  host: string;
  port: number;
  database: string;
  user: string;
  password: string;
}

interface RedisConfig {
  host: string;
  port: number;
}

interface AppConfig {
  port: number;
  nodeEnv: string;
  logLevel: string;
  rateLimit: {
    windowMs: number;
    max: number;
  };
} 
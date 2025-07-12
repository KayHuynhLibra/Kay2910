# User Service

Microservice quản lý người dùng với các tính năng:
- Quản lý thông tin người dùng
- Caching với Redis
- Database PostgreSQL
- API RESTful
- Monitoring và logging

## Yêu cầu hệ thống

- Node.js >= 18.0.0
- npm >= 8.0.0
- PostgreSQL >= 13.0
- Redis >= 6.0

## Cài đặt

1. Clone repository:
```bash
git clone <repository-url>
cd services/user-service
```

2. Cài đặt dependencies:
```bash
npm install
```

3. Tạo file .env từ .env.example và cấu hình các biến môi trường:
```bash
cp .env.example .env
```

4. Build và chạy service:
```bash
# Development
npm run dev

# Production
npm run build
npm start
```

## API Endpoints

### GET /api/users
Lấy danh sách người dùng

### GET /api/users/:id
Lấy thông tin người dùng theo ID

### POST /api/users
Tạo người dùng mới

## Testing

```bash
# Chạy tests
npm test

# Chạy tests với watch mode
npm run test:watch

# Kiểm tra coverage
npm run test:coverage
```

## Linting và Formatting

```bash
# Kiểm tra lint
npm run lint

# Tự động sửa lỗi lint
npm run lint:fix

# Format code
npm run format
```

## Docker

Build và chạy container:
```bash
docker build -t user-service .
docker run -p 3000:3000 user-service
```

## Kubernetes

Deploy lên Kubernetes:
```bash
kubectl apply -f kubernetes/
```

## Monitoring

Service được tích hợp với:
- Prometheus metrics
- Grafana dashboards
- Winston logging

## License

MIT 
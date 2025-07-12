# AI System - Phase 1: Core System

## Tổng Quan

Phase 1 tập trung vào việc xây dựng hệ thống cốt lõi với các tính năng:
- Xác thực và phân quyền người dùng
- API endpoints cơ bản
- Monitoring và metrics
- Cấu trúc cơ sở dữ liệu

## Cấu Trúc Thư Mục

```
phase1/
├── core/
│   ├── security.py        # Xác thực và phân quyền
│   ├── monitoring.py      # Monitoring cơ bản
│   └── database.py        # Quản lý database
├── api/
│   ├── routes/
│   │   ├── auth.py       # API xác thực
│   │   └── health.py     # API kiểm tra hệ thống
├── models/
│   └── user.py           # Model người dùng
├── tests/
│   ├── test_auth.py
│   └── test_health.py
└── config/
    └── settings.py       # Cấu hình hệ thống
```

## Cài Đặt

1. Tạo môi trường ảo:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

3. Tạo file .env:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///./ai_system.db
REDIS_URL=redis://localhost:6379
```

## Chạy Ứng Dụng

1. Khởi động server:
```bash
uvicorn main:app --reload
```

2. Truy cập:
- API documentation: http://localhost:8000/docs
- Health check: http://localhost:8000/api/v1/health
- Metrics: http://localhost:8000/api/v1/metrics

## API Endpoints

### Authentication
- POST `/api/v1/token` - Đăng nhập và lấy token
- POST `/api/v1/users/` - Tạo người dùng mới
- GET `/api/v1/users/me/` - Lấy thông tin người dùng hiện tại

### Health & Monitoring
- GET `/api/v1/health` - Kiểm tra trạng thái hệ thống
- GET `/api/v1/metrics` - Lấy metrics Prometheus

## Chạy Tests

```bash
pytest tests/
```

## Tính Năng

### Security
- JWT authentication
- Password hashing với bcrypt
- CORS middleware
- Rate limiting

### Monitoring
- Request timing
- Error tracking
- Prometheus metrics
- Health checks

### Database
- SQLAlchemy ORM
- Connection pooling
- Session management

## Bảo Mật

1. JWT Token:
- Sử dụng HS256 algorithm
- Token expiration: 30 phút
- Secure password hashing

2. CORS:
- Cấu hình linh hoạt
- Hỗ trợ credentials
- Custom headers

3. Database:
- Connection pooling
- Prepared statements
- Session management

## Monitoring

1. Metrics:
- Request count
- Response time
- Error rate
- Status codes

2. Health Checks:
- System status
- Version info
- Debug mode

## Phát Triển

1. Cấu trúc module:
- Core functionality
- API routes
- Models
- Tests

2. Best practices:
- Type hints
- Async/await
- Error handling
- Logging

## Troubleshooting

1. Database Issues:
- Kiểm tra connection string
- Xác nhận database đang chạy
- Kiểm tra permissions

2. Authentication Issues:
- Kiểm tra SECRET_KEY
- Xác nhận token expiration
- Kiểm tra password hashing

3. Monitoring Issues:
- Kiểm tra Prometheus endpoint
- Xác nhận metrics collection
- Kiểm tra logging

## Contributing

1. Code Style:
- PEP 8
- Type hints
- Docstrings

2. Testing:
- Unit tests
- Integration tests
- Coverage reports

3. Documentation:
- API docs
- Code comments
- README updates 
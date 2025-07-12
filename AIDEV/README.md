# AI System Project

## Tổng Quan

Dự án AI System được phát triển theo 4 giai đoạn, mỗi giai đoạn tập trung vào một khía cạnh cụ thể của hệ thống:

1. **Phase 1: Core System**
   - Xác thực và phân quyền
   - API endpoints cơ bản
   - Monitoring đơn giản
   - Cấu trúc cơ sở dữ liệu

2. **Phase 2: Analytics & Monitoring**
   - Phân tích cảm xúc
   - Theo dõi tương tác
   - Monitoring nâng cao
   - Metrics và logging

3. **Phase 3: Advanced Features**
   - Machine Learning
   - Bảo mật nâng cao
   - Phát hiện bất thường
   - Xử lý ngôn ngữ tự nhiên

4. **Phase 4: Integration & Scaling**
   - Containerization
   - Kubernetes deployment
   - Tích hợp với hệ thống khác
   - Load balancing và caching

## Cấu Trúc Dự Án

```
ai_system/
├── phase1/              # Core System
│   ├── core/           # Core functionality
│   ├── api/            # API endpoints
│   ├── models/         # Data models
│   ├── tests/          # Unit tests
│   └── config/         # Configuration
│
├── phase2/              # Analytics & Monitoring
│   ├── analytics/      # Analytics features
│   ├── monitoring/     # Monitoring tools
│   └── tests/          # Unit tests
│
├── phase3/              # Advanced Features
│   ├── ml/            # Machine Learning
│   ├── security/      # Advanced security
│   └── tests/         # Unit tests
│
└── phase4/              # Integration & Scaling
    ├── deployment/     # Deployment configs
    ├── scaling/        # Scaling features
    └── tests/          # Unit tests
```

## Yêu Cầu Hệ Thống

- Python 3.10+
- PostgreSQL 13+
- Redis 6+
- Docker & Docker Compose
- Kubernetes (cho Phase 4)

## Cài Đặt

1. Clone repository:
```bash
git clone https://github.com/your-username/ai-system.git
cd ai-system
```

2. Tạo môi trường ảo:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Cài đặt dependencies cho từng phase:
```bash
# Phase 1
cd phase1
pip install -r requirements.txt

# Phase 2
cd ../phase2
pip install -r requirements.txt

# Phase 3
cd ../phase3
pip install -r requirements.txt

# Phase 4
cd ../phase4
pip install -r requirements.txt
```

4. Tạo file .env:
```env
# Core settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/ai_system
REDIS_URL=redis://localhost:6379

# External services
ELASTICSEARCH_URL=http://localhost:9200
SENTRY_DSN=your-sentry-dsn

# ML services
TENSORFLOW_GPU=True
MODEL_PATH=/path/to/models
```

## Chạy Ứng Dụng

### Phase 1: Core System
```bash
cd phase1
uvicorn main:app --reload
```

### Phase 2: Analytics & Monitoring
```bash
cd phase2
uvicorn main:app --reload
```

### Phase 3: Advanced Features
```bash
cd phase3
uvicorn main:app --reload
```

### Phase 4: Integration & Scaling
```bash
cd phase4
docker-compose up -d
```

## API Documentation

Mỗi phase có API documentation riêng:
- Phase 1: http://localhost:8000/docs
- Phase 2: http://localhost:8001/docs
- Phase 3: http://localhost:8002/docs
- Phase 4: http://localhost:8003/docs

## Monitoring

### Health Checks
- Phase 1: http://localhost:8000/api/v1/health
- Phase 2: http://localhost:8001/api/v1/health
- Phase 3: http://localhost:8002/api/v1/health
- Phase 4: http://localhost:8003/api/v1/health

### Metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## Testing

Chạy tests cho từng phase:
```bash
# Phase 1
cd phase1
pytest tests/

# Phase 2
cd ../phase2
pytest tests/

# Phase 3
cd ../phase3
pytest tests/

# Phase 4
cd ../phase4
pytest tests/
```

## Bảo Mật

1. Authentication:
- JWT tokens
- OAuth2
- Role-based access control

2. Data Protection:
- Encryption at rest
- Secure communication
- Input validation

3. Monitoring:
- Audit logging
- Anomaly detection
- Rate limiting

## Contributing

1. Fork repository
2. Tạo branch mới
3. Commit changes
4. Push to branch
5. Tạo Pull Request

## Documentation

- [Phase 1 Documentation](phase1/README.md)
- [Phase 2 Documentation](phase2/README.md)
- [Phase 3 Documentation](phase3/README.md)
- [Phase 4 Documentation](phase4/README.md)
- [API Documentation](docs/api.md)
- [Deployment Guide](docs/deployment.md)

## License

MIT License - Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## Contact

- Email: your-email@example.com
- GitHub: [your-username](https://github.com/your-username)
- Project Link: [https://github.com/your-username/ai-system](https://github.com/your-username/ai-system) 
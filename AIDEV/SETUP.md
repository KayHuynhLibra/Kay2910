# Hướng dẫn cài đặt và cấu hình AI System

## 1. Cài đặt Python 3.10

### Windows
1. Tải Python 3.10 từ [python.org](https://www.python.org/downloads/release/python-3109/)
2. Chọn "Windows installer (64-bit)"
3. Khi cài đặt, đánh dấu "Add Python 3.10 to PATH"

### Linux
```bash
sudo apt update
sudo apt install python3.10 python3.10-venv
```

## 2. Tạo môi trường ảo

### Windows
```bash
# Tạo môi trường ảo
python3.10 -m venv venv

# Kích hoạt môi trường
.\venv\Scripts\activate
```

### Linux
```bash
# Tạo môi trường ảo
python3.10 -m venv venv

# Kích hoạt môi trường
source venv/bin/activate
```

## 3. Cài đặt dependencies

```bash
# Cập nhật pip
python -m pip install --upgrade pip

# Cài đặt các package cần thiết
pip install -r requirements.txt
```

## 4. Cấu hình môi trường

1. Tạo file `.env` trong thư mục gốc:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///./ai_system.db
REDIS_URL=redis://localhost:6379
ELASTICSEARCH_URL=http://localhost:9200
SENTRY_DSN=your-sentry-dsn
```

2. Cấu hình các service:
   - Redis: Chạy Redis server
   - Elasticsearch: Chạy Elasticsearch server
   - Prometheus: Cấu hình monitoring

## 5. Chạy ứng dụng

```bash
# Chạy server
python main.py

# Chạy tests
pytest test_app.py -v
```

## 6. Kiểm tra

1. Truy cập API documentation: http://localhost:8000/docs
2. Kiểm tra health endpoint: http://localhost:8000/health
3. Test authentication:
   ```bash
   curl -X POST "http://localhost:8000/token" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "username=test&password=test"
   ```

## 7. Monitoring

1. Prometheus metrics: http://localhost:8000/metrics
2. Grafana dashboard: http://localhost:3000
3. Elasticsearch: http://localhost:9200

## 8. Troubleshooting

### Lỗi phổ biến

1. **ModuleNotFoundError**: Kiểm tra môi trường ảo đã được kích hoạt
2. **ConnectionError**: Kiểm tra các service (Redis, Elasticsearch) đã chạy
3. **ImportError**: Kiểm tra phiên bản Python (nên dùng 3.10)

### Giải pháp

1. Xóa và tạo lại môi trường ảo:
```bash
deactivate
rm -rf venv
python3.10 -m venv venv
source venv/bin/activate  # hoặc .\venv\Scripts\activate trên Windows
pip install -r requirements.txt
```

2. Kiểm tra logs:
```bash
tail -f app.log
```

## 9. Cấu trúc thư mục

```
ai_system/
├── core/
│   ├── __init__.py
│   ├── security.py
│   └── monitoring.py
├── tests/
│   └── test_app.py
├── main.py
├── requirements.txt
└── .env
```

## 10. Bảo mật

1. Thay đổi SECRET_KEY trong file .env
2. Cấu hình CORS trong main.py
3. Sử dụng HTTPS trong môi trường production
4. Bật rate limiting
5. Cấu hình logging và monitoring 
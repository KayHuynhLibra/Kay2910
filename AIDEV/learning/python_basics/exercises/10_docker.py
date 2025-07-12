"""
Bài tập 10: Docker

Mục tiêu:
- Hiểu cách containerize ứng dụng Python
- Thực hành với Dockerfile
- Sử dụng Docker Compose
"""

# TODO: Tạo Dockerfile
"""
# Dockerfile
FROM python:3.10-slim

# Cài đặt các dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

# TODO: Tạo requirements.txt
"""
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.4.2
python-multipart==0.0.6
python-jose==3.3.0
passlib==1.7.4
bcrypt==4.0.1
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
redis==5.0.1
"""

# TODO: Tạo docker-compose.yml
"""
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/dbname
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=dbname
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
"""

# TODO: Tạo .dockerignore
"""
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env
pip-log.txt
pip-delete-this-directory.txt
.tox
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.pytest_cache
.env
.venv
venv
ENV
"""

# TODO: Tạo script build và run
"""
#!/bin/bash

# Build image
docker build -t myapp .

# Run container
docker run -d -p 8000:8000 --name myapp-container myapp

# View logs
docker logs -f myapp-container

# Stop container
docker stop myapp-container

# Remove container
docker rm myapp-container

# Remove image
docker rmi myapp
"""

# TODO: Tạo script docker-compose
"""
#!/bin/bash

# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild services
docker-compose up -d --build

# Remove volumes
docker-compose down -v
"""

# TODO: Tạo healthcheck
"""
# Thêm vào Dockerfile
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1
"""

# TODO: Tạo multi-stage build
"""
# Dockerfile
# Build stage
FROM python:3.10-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run stage
FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

"""
Bài tập về nhà:
1. Tạo Dockerfile cho một ứng dụng FastAPI với PostgreSQL
2. Tạo docker-compose.yml cho một hệ thống microservices
3. Tạo Dockerfile cho một ứng dụng machine learning
4. Tạo docker-compose.yml cho một hệ thống monitoring
5. Tạo Dockerfile cho một ứng dụng web với Nginx
""" 
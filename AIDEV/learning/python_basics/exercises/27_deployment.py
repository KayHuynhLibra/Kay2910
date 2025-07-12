"""
Bài tập 27: Deployment

Mục tiêu:
- Hiểu cách deploy ứng dụng Python
- Thực hành với Docker và Kubernetes
- Sử dụng CI/CD tools
"""

import os
import sys
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import json
import re

# TODO: Dockerfile
"""
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
"""

# TODO: docker-compose.yml
"""
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/dbname
    depends_on:
      - db
  
  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=dbname
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
"""

# TODO: Kubernetes deployment
"""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
---
apiVersion: v1
kind: Service
metadata:
  name: my-app
spec:
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer
"""

# TODO: GitHub Actions workflow
"""
name: CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - uses: actions/checkout@v2
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v1
    - name: Login to DockerHub
      uses: docker/login-action@v1
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}
    - name: Build and push
      uses: docker/build-push-action@v2
      with:
        push: true
        tags: my-app:latest
"""

# TODO: Nginx configuration
"""
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /app/static;
    }

    location /media {
        alias /app/media;
    }
}
"""

# TODO: Systemd service
"""
[Unit]
Description=My Python Application
After=network.target

[Service]
User=appuser
WorkingDirectory=/app
Environment="PATH=/app/venv/bin"
ExecStart=/app/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
"""

# TODO: Environment variables
"""
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=example.com
"""

# TODO: Backup script
"""
#!/bin/bash

# Backup database
pg_dump -U user dbname > backup.sql

# Backup files
tar -czf files.tar.gz /app/media

# Upload to S3
aws s3 cp backup.sql s3://my-backups/
aws s3 cp files.tar.gz s3://my-backups/
"""

# TODO: Monitoring script
"""
#!/usr/bin/env python3

import psutil
import requests
import time

def check_cpu():
    return psutil.cpu_percent()

def check_memory():
    return psutil.virtual_memory().percent

def check_disk():
    return psutil.disk_usage('/').percent

def check_app():
    try:
        response = requests.get('http://localhost:8000/health')
        return response.status_code == 200
    except:
        return False

def main():
    while True:
        metrics = {
            'cpu': check_cpu(),
            'memory': check_memory(),
            'disk': check_disk(),
            'app': check_app()
        }
        print(metrics)
        time.sleep(60)

if __name__ == '__main__':
    main()
"""

# TODO: Logging configuration
"""
[loggers]
keys=root,app

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_app]
level=INFO
handlers=fileHandler
qualname=app
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=INFO
formatter=simpleFormatter
args=('app.log', 'a')

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
"""

# TODO: Example usage
def example_usage():
    """
    Example usage of deployment features.
    """
    # Create deployment files
    os.makedirs("deployment", exist_ok=True)
    
    # Create Dockerfile
    with open("deployment/Dockerfile", "w") as f:
        f.write('''
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
''')
    
    # Create docker-compose.yml
    with open("deployment/docker-compose.yml", "w") as f:
        f.write('''
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/dbname
    depends_on:
      - db
  
  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=dbname
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
''')
    
    # Create Kubernetes deployment
    with open("deployment/k8s-deployment.yaml", "w") as f:
        f.write('''
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
---
apiVersion: v1
kind: Service
metadata:
  name: my-app
spec:
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer
''')
    
    # Create GitHub Actions workflow
    with open("deployment/.github/workflows/ci-cd.yml", "w") as f:
        f.write('''
name: CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - uses: actions/checkout@v2
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v1
    - name: Login to DockerHub
      uses: docker/login-action@v1
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}
    - name: Build and push
      uses: docker/build-push-action@v2
      with:
        push: true
        tags: my-app:latest
''')
    
    # Create Nginx configuration
    with open("deployment/nginx.conf", "w") as f:
        f.write('''
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /app/static;
    }

    location /media {
        alias /app/media;
    }
}
''')
    
    # Create systemd service
    with open("deployment/my-app.service", "w") as f:
        f.write('''
[Unit]
Description=My Python Application
After=network.target

[Service]
User=appuser
WorkingDirectory=/app
Environment="PATH=/app/venv/bin"
ExecStart=/app/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
''')
    
    # Create environment variables
    with open("deployment/.env", "w") as f:
        f.write('''
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=example.com
''')
    
    # Create backup script
    with open("deployment/backup.sh", "w") as f:
        f.write('''
#!/bin/bash

# Backup database
pg_dump -U user dbname > backup.sql

# Backup files
tar -czf files.tar.gz /app/media

# Upload to S3
aws s3 cp backup.sql s3://my-backups/
aws s3 cp files.tar.gz s3://my-backups/
''')
    
    # Create monitoring script
    with open("deployment/monitor.py", "w") as f:
        f.write('''
#!/usr/bin/env python3

import psutil
import requests
import time

def check_cpu():
    return psutil.cpu_percent()

def check_memory():
    return psutil.virtual_memory().percent

def check_disk():
    return psutil.disk_usage('/').percent

def check_app():
    try:
        response = requests.get('http://localhost:8000/health')
        return response.status_code == 200
    except:
        return False

def main():
    while True:
        metrics = {
            'cpu': check_cpu(),
            'memory': check_memory(),
            'disk': check_disk(),
            'app': check_app()
        }
        print(metrics)
        time.sleep(60)

if __name__ == '__main__':
    main()
''')
    
    # Create logging configuration
    with open("deployment/logging.conf", "w") as f:
        f.write('''
[loggers]
keys=root,app

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_app]
level=INFO
handlers=fileHandler
qualname=app
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=INFO
formatter=simpleFormatter
args=('app.log', 'a')

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
''')
    
    print("Deployment files created successfully!")

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tạo deployment cho một ứng dụng FastAPI
2. Tạo deployment cho một ứng dụng machine learning
3. Tạo deployment cho một hệ thống microservices
4. Tạo deployment cho một ứng dụng web với Nginx
5. Tạo deployment cho một hệ thống database
""" 
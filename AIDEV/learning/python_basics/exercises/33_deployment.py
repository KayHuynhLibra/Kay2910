"""
Bài tập 33: Deployment

Mục tiêu:
- Hiểu cách deploy ứng dụng Python
- Thực hành với Docker và Kubernetes
- Sử dụng deployment tools
"""

import os
import sys
import time
import pytest
import unittest
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import json
import re

# TODO: Dockerfile
"""
Dockerfile example:

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
"""

# TODO: docker-compose.yml
"""
docker-compose.yml example:

version: '3'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/dbname
    depends_on:
      - db
    volumes:
      - .:/app
    command: uvicorn app:app --host 0.0.0.0 --port 8000 --reload

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
deployment.yaml example:

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
        resources:
          limits:
            cpu: "1"
            memory: "1Gi"
          requests:
            cpu: "500m"
            memory: "512Mi"
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
.github/workflows/deploy.yml example:

name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
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
    
    - name: Build and push Docker image
      uses: docker/build-push-action@v2
      with:
        context: .
        push: true
        tags: my-app:latest
    
    - name: Deploy to Kubernetes
      uses: azure/k8s-deploy@v1
      with:
        manifests: |
          deployment.yaml
        images: |
          my-app:latest
"""

# TODO: Nginx configuration
"""
nginx.conf example:

events {
    worker_connections 1024;
}

http {
    upstream my_app {
        server 127.0.0.1:8000;
        server 127.0.0.1:8001;
        server 127.0.0.1:8002;
    }

    server {
        listen 80;
        server_name example.com;

        location / {
            proxy_pass http://my_app;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
"""

# TODO: Systemd service
"""
my-app.service example:

[Unit]
Description=My Python Application
After=network.target

[Service]
User=myuser
WorkingDirectory=/opt/my-app
Environment="PATH=/opt/my-app/venv/bin"
ExecStart=/opt/my-app/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
"""

# TODO: Environment variables
"""
.env example:

DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=example.com,www.example.com
"""

# TODO: Backup script
"""
backup.sh example:

#!/bin/bash

# Backup database
pg_dump -U user -d dbname > backup_$(date +%Y%m%d).sql

# Backup files
tar -czf backup_$(date +%Y%m%d).tar.gz /opt/my-app

# Upload to S3
aws s3 cp backup_$(date +%Y%m%d).sql s3://my-backups/
aws s3 cp backup_$(date +%Y%m%d).tar.gz s3://my-backups/

# Clean up old backups
find . -name "backup_*.sql" -mtime +7 -delete
find . -name "backup_*.tar.gz" -mtime +7 -delete
"""

# TODO: Monitoring script
"""
monitor.sh example:

#!/bin/bash

# Check if application is running
if ! pgrep -f "python app.py" > /dev/null; then
    echo "Application is not running. Restarting..."
    systemctl restart my-app
fi

# Check disk space
if [ $(df -h / | awk 'NR==2 {print $5}' | sed 's/%//') -gt 90 ]; then
    echo "Disk space is running low. Sending alert..."
    curl -X POST -H "Content-Type: application/json" -d '{"message":"Disk space is running low"}' http://alert-service
fi

# Check memory usage
if [ $(free | awk 'NR==2 {print $3/$2 * 100.0}') -gt 90 ]; then
    echo "Memory usage is high. Sending alert..."
    curl -X POST -H "Content-Type: application/json" -d '{"message":"Memory usage is high"}' http://alert-service
fi
"""

# TODO: Logging configuration
"""
logging.conf example:

[loggers]
keys=root,myapp

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_myapp]
level=INFO
handlers=fileHandler
qualname=myapp
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
    # Dockerfile
    print("Dockerfile:")
    print("""
    FROM python:3.9-slim

    WORKDIR /app

    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    COPY . .

    CMD ["python", "app.py"]
    """)
    
    # docker-compose.yml
    print("\ndocker-compose.yml:")
    print("""
    version: '3'

    services:
      web:
        build: .
        ports:
          - "8000:8000"
        environment:
          - DATABASE_URL=postgresql://user:password@db:5432/dbname
        depends_on:
          - db
        volumes:
          - .:/app
        command: uvicorn app:app --host 0.0.0.0 --port 8000 --reload

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
    """)
    
    # Kubernetes deployment
    print("\nKubernetes deployment:")
    print("""
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
            resources:
              limits:
                cpu: "1"
                memory: "1Gi"
              requests:
                cpu: "500m"
                memory: "512Mi"
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
    """)
    
    # GitHub Actions workflow
    print("\nGitHub Actions workflow:")
    print("""
    name: Deploy

    on:
      push:
        branches: [ main ]

    jobs:
      deploy:
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
        
        - name: Build and push Docker image
          uses: docker/build-push-action@v2
          with:
            context: .
            push: true
            tags: my-app:latest
        
        - name: Deploy to Kubernetes
          uses: azure/k8s-deploy@v1
          with:
            manifests: |
              deployment.yaml
            images: |
              my-app:latest
    """)
    
    # Nginx configuration
    print("\nNginx configuration:")
    print("""
    events {
        worker_connections 1024;
    }

    http {
        upstream my_app {
            server 127.0.0.1:8000;
            server 127.0.0.1:8001;
            server 127.0.0.1:8002;
        }

        server {
            listen 80;
            server_name example.com;

            location / {
                proxy_pass http://my_app;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
        }
    }
    """)
    
    # Systemd service
    print("\nSystemd service:")
    print("""
    [Unit]
    Description=My Python Application
    After=network.target

    [Service]
    User=myuser
    WorkingDirectory=/opt/my-app
    Environment="PATH=/opt/my-app/venv/bin"
    ExecStart=/opt/my-app/venv/bin/python app.py
    Restart=always

    [Install]
    WantedBy=multi-user.target
    """)
    
    # Environment variables
    print("\nEnvironment variables:")
    print("""
    DATABASE_URL=postgresql://user:password@localhost:5432/dbname
    SECRET_KEY=your-secret-key
    DEBUG=False
    ALLOWED_HOSTS=example.com,www.example.com
    """)
    
    # Backup script
    print("\nBackup script:")
    print("""
    #!/bin/bash

    # Backup database
    pg_dump -U user -d dbname > backup_$(date +%Y%m%d).sql

    # Backup files
    tar -czf backup_$(date +%Y%m%d).tar.gz /opt/my-app

    # Upload to S3
    aws s3 cp backup_$(date +%Y%m%d).sql s3://my-backups/
    aws s3 cp backup_$(date +%Y%m%d).tar.gz s3://my-backups/

    # Clean up old backups
    find . -name "backup_*.sql" -mtime +7 -delete
    find . -name "backup_*.tar.gz" -mtime +7 -delete
    """)
    
    # Monitoring script
    print("\nMonitoring script:")
    print("""
    #!/bin/bash

    # Check if application is running
    if ! pgrep -f "python app.py" > /dev/null; then
        echo "Application is not running. Restarting..."
        systemctl restart my-app
    fi

    # Check disk space
    if [ $(df -h / | awk 'NR==2 {print $5}' | sed 's/%//') -gt 90 ]; then
        echo "Disk space is running low. Sending alert..."
        curl -X POST -H "Content-Type: application/json" -d '{"message":"Disk space is running low"}' http://alert-service
    fi

    # Check memory usage
    if [ $(free | awk 'NR==2 {print $3/$2 * 100.0}') -gt 90 ]; then
        echo "Memory usage is high. Sending alert..."
        curl -X POST -H "Content-Type: application/json" -d '{"message":"Memory usage is high"}' http://alert-service
    fi
    """)
    
    # Logging configuration
    print("\nLogging configuration:")
    print("""
    [loggers]
    keys=root,myapp

    [handlers]
    keys=consoleHandler,fileHandler

    [formatters]
    keys=simpleFormatter

    [logger_root]
    level=DEBUG
    handlers=consoleHandler

    [logger_myapp]
    level=INFO
    handlers=fileHandler
    qualname=myapp
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
    """)

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
"""
Bài tập 45: Deployment

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
from functools import wraps
from contextlib import contextmanager

# TODO: Dockerfile
def dockerfile():
    """
    Dockerfile example.
    
    # Use Python 3.9
    FROM python:3.9-slim
    
    # Set working directory
    WORKDIR /app
    
    # Copy requirements
    COPY requirements.txt .
    
    # Install dependencies
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy application
    COPY . .
    
    # Run application
    CMD ["python", "app.py"]
    """
    return "Dockerfile"

# TODO: docker-compose.yml
def docker_compose():
    """
    docker-compose.yml example.
    
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
    return "docker-compose.yml"

# TODO: Kubernetes deployment
def kubernetes_deployment():
    """
    Kubernetes deployment example.
    
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
                  name: my-app-secrets
                  key: database-url
            resources:
              limits:
                cpu: "1"
                memory: "1Gi"
              requests:
                cpu: "500m"
                memory: "512Mi"
    """
    return "kubernetes-deployment.yaml"

# TODO: Kubernetes service
def kubernetes_service():
    """
    Kubernetes service example.
    
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
    return "kubernetes-service.yaml"

# TODO: GitHub Actions workflow
def github_actions():
    """
    GitHub Actions workflow example.
    
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
              kubernetes/deployment.yaml
              kubernetes/service.yaml
            images: |
              my-app:latest
    """
    return "github-actions.yml"

# TODO: Nginx configuration
def nginx_config():
    """
    Nginx configuration example.
    
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
    return "nginx.conf"

# TODO: Systemd service
def systemd_service():
    """
    Systemd service example.
    
    [Unit]
    Description=My Python Application
    After=network.target
    
    [Service]
    User=myuser
    Group=mygroup
    WorkingDirectory=/app
    Environment="PATH=/app/venv/bin"
    ExecStart=/app/venv/bin/python app.py
    Restart=always
    
    [Install]
    WantedBy=multi-user.target
    """
    return "my-app.service"

# TODO: Environment variables
def environment_variables():
    """
    Environment variables example.
    
    DATABASE_URL=postgresql://user:password@localhost:5432/dbname
    SECRET_KEY=your-secret-key
    DEBUG=False
    ALLOWED_HOSTS=example.com,www.example.com
    """
    return ".env"

# TODO: Backup script
def backup_script():
    """
    Backup script example.
    
    #!/bin/bash
    
    # Backup database
    pg_dump -U user dbname > backup/db_$(date +%Y%m%d).sql
    
    # Backup media files
    tar -czf backup/media_$(date +%Y%m%d).tar.gz media/
    
    # Upload to S3
    aws s3 cp backup/db_$(date +%Y%m%d).sql s3://my-backups/
    aws s3 cp backup/media_$(date +%Y%m%d).tar.gz s3://my-backups/
    
    # Clean up old backups
    find backup/ -type f -mtime +7 -delete
    """
    return "backup.sh"

# TODO: Monitoring script
def monitoring_script():
    """
    Monitoring script example.
    
    #!/bin/bash
    
    # Check application status
    if ! curl -s http://localhost:8000/health > /dev/null; then
        echo "Application is down"
        exit 1
    fi
    
    # Check database status
    if ! pg_isready -h localhost -p 5432 > /dev/null; then
        echo "Database is down"
        exit 1
    fi
    
    # Check disk space
    if [ $(df -h / | awk 'NR==2 {print $5}' | sed 's/%//') -gt 90 ]; then
        echo "Disk space is low"
        exit 1
    fi
    
    # Check memory usage
    if [ $(free | awk 'NR==2 {print $3/$2 * 100.0}' | cut -d. -f1) -gt 90 ]; then
        echo "Memory usage is high"
        exit 1
    fi
    """
    return "monitor.sh"

# TODO: Logging configuration
def logging_config():
    """
    Logging configuration example.
    
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
    return "logging.conf"

# TODO: Example usage
def example_usage():
    """
    Example usage of deployment features.
    """
    # Dockerfile
    print("Dockerfile:")
    print(dockerfile())
    
    # docker-compose.yml
    print("\ndocker-compose.yml:")
    print(docker_compose())
    
    # Kubernetes deployment
    print("\nKubernetes deployment:")
    print(kubernetes_deployment())
    
    # Kubernetes service
    print("\nKubernetes service:")
    print(kubernetes_service())
    
    # GitHub Actions workflow
    print("\nGitHub Actions workflow:")
    print(github_actions())
    
    # Nginx configuration
    print("\nNginx configuration:")
    print(nginx_config())
    
    # Systemd service
    print("\nSystemd service:")
    print(systemd_service())
    
    # Environment variables
    print("\nEnvironment variables:")
    print(environment_variables())
    
    # Backup script
    print("\nBackup script:")
    print(backup_script())
    
    # Monitoring script
    print("\nMonitoring script:")
    print(monitoring_script())
    
    # Logging configuration
    print("\nLogging configuration:")
    print(logging_config())

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
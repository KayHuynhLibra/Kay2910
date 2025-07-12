"""
Bài tập 51: Deployment

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
import logging
import traceback
import pdb
import psutil
import numpy as np
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
    
    # Base image
    FROM python:3.9-slim
    
    # Working directory
    WORKDIR /app
    
    # Copy requirements
    COPY requirements.txt .
    
    # Install dependencies
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy application
    COPY . .
    
    # Expose port
    EXPOSE 8000
    
    # Run application
    CMD ["python", "app.py"]
    """
    return "Done"

# TODO: docker-compose.yml
def docker_compose():
    """
    docker-compose.yml example.
    
    version: '3'
    
    services:
      app:
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
        image: postgres:13
        environment:
          - POSTGRES_USER=user
          - POSTGRES_PASSWORD=password
          - POSTGRES_DB=dbname
        volumes:
          - postgres_data:/var/lib/postgresql/data
    
      redis:
        image: redis:6
        volumes:
          - redis_data:/data
    
    volumes:
      postgres_data:
      redis_data:
    """
    return "Done"

# TODO: Kubernetes deployment
def kubernetes_deployment():
    """
    Kubernetes deployment example.
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: myapp
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: myapp
      template:
        metadata:
          labels:
            app: myapp
        spec:
          containers:
          - name: myapp
            image: myapp:latest
            ports:
            - containerPort: 8000
            env:
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: myapp-secrets
                  key: database-url
            resources:
              limits:
                cpu: "1"
                memory: "1Gi"
              requests:
                cpu: "500m"
                memory: "512Mi"
            livenessProbe:
              httpGet:
                path: /health
                port: 8000
              initialDelaySeconds: 30
              periodSeconds: 10
            readinessProbe:
              httpGet:
                path: /ready
                port: 8000
              initialDelaySeconds: 5
              periodSeconds: 5
    """
    return "Done"

# TODO: Kubernetes service
def kubernetes_service():
    """
    Kubernetes service example.
    
    apiVersion: v1
    kind: Service
    metadata:
      name: myapp
    spec:
      type: LoadBalancer
      ports:
      - port: 80
        targetPort: 8000
      selector:
        app: myapp
    """
    return "Done"

# TODO: GitHub Actions workflow
def github_actions():
    """
    GitHub Actions workflow example.
    
    name: Deploy
    
    on:
      push:
        branches: [ main ]
    
    jobs:
      build-and-deploy:
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
        
        - name: Build Docker image
          run: |
            docker build -t myapp:${{ github.sha }} .
        
        - name: Push to Docker Hub
          uses: docker/build-push-action@v2
          with:
            push: true
            tags: myapp:${{ github.sha }}
        
        - name: Deploy to Kubernetes
          uses: azure/k8s-deploy@v1
          with:
            manifests: |
              k8s/deployment.yaml
              k8s/service.yaml
            images: |
              myapp:${{ github.sha }}
    """
    return "Done"

# TODO: Nginx configuration
def nginx_config():
    """
    Nginx configuration example.
    
    upstream myapp {
        server 127.0.0.1:8000;
        server 127.0.0.1:8001;
        server 127.0.0.1:8002;
    }
    
    server {
        listen 80;
        server_name example.com;
    
        location / {
            proxy_pass http://myapp;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    
        location /static {
            alias /var/www/static;
            expires 30d;
            add_header Cache-Control "public, no-transform";
        }
    
        location /media {
            alias /var/www/media;
            expires 30d;
            add_header Cache-Control "public, no-transform";
        }
    }
    """
    return "Done"

# TODO: Systemd service
def systemd_service():
    """
    Systemd service example.
    
    [Unit]
    Description=MyApp
    After=network.target
    
    [Service]
    User=myapp
    Group=myapp
    WorkingDirectory=/opt/myapp
    Environment="PATH=/opt/myapp/venv/bin"
    Environment="DATABASE_URL=postgresql://user:password@localhost:5432/dbname"
    Environment="REDIS_URL=redis://localhost:6379/0"
    ExecStart=/opt/myapp/venv/bin/python app.py
    Restart=always
    
    [Install]
    WantedBy=multi-user.target
    """
    return "Done"

# TODO: Environment variables
def environment_variables():
    """
    Environment variables example.
    
    DATABASE_URL=postgresql://user:password@localhost:5432/dbname
    REDIS_URL=redis://localhost:6379/0
    SECRET_KEY=your-secret-key
    DEBUG=False
    ALLOWED_HOSTS=example.com,www.example.com
    """
    return "Done"

# TODO: Backup script
def backup_script():
    """
    Backup script example.
    
    #!/bin/bash
    
    # Backup database
    pg_dump -U user -d dbname > backup/db_$(date +%Y%m%d).sql
    
    # Backup media files
    tar -czf backup/media_$(date +%Y%m%d).tar.gz /var/www/media
    
    # Upload to S3
    aws s3 cp backup/db_$(date +%Y%m%d).sql s3://myapp-backups/
    aws s3 cp backup/media_$(date +%Y%m%d).tar.gz s3://myapp-backups/
    
    # Cleanup old backups
    find backup -type f -mtime +7 -delete
    """
    return "Done"

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
    if [ $(free | awk 'NR==2 {print $3/$2 * 100.0}') -gt 90 ]; then
        echo "Memory usage is high"
        exit 1
    fi
    """
    return "Done"

# TODO: Logging configuration
def logging_config():
    """
    Logging configuration example.
    
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': '/var/log/myapp/app.log',
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 5,
                'formatter': 'verbose',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'myapp': {
                'handlers': ['file', 'console'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }
    """
    return "Done"

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
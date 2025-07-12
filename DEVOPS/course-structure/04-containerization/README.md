# Containerization
# Container hóa

## Overview / Tổng quan

This module covers container technologies and orchestration platforms. You'll learn about Docker, Kubernetes, and container best practices for building, deploying, and managing containerized applications.

Module này bao gồm các công nghệ container và nền tảng điều phối. Bạn sẽ học về Docker, Kubernetes và các thực hành tốt nhất về container để xây dựng, triển khai và quản lý các ứng dụng được container hóa.

## Learning Objectives / Mục tiêu học tập

### 1. Docker Fundamentals / Kiến thức cơ bản về Docker
- Container concepts
- Docker architecture
- Image management
- Container networking
- Best practices

*Vietnamese:*
- Khái niệm container
- Kiến trúc Docker
- Quản lý image
- Mạng container
- Thực hành tốt nhất

### 2. Kubernetes Essentials / Kiến thức cơ bản về Kubernetes
- Cluster architecture
- Pod management
- Service discovery
- Storage management
- Best practices

*Vietnamese:*
- Kiến trúc cluster
- Quản lý Pod
- Khám phá dịch vụ
- Quản lý lưu trữ
- Thực hành tốt nhất

## Lab Structure / Cấu trúc Lab

### 1. Docker Labs / Lab Docker

#### Lab 1: Dockerfile Creation / Tạo Dockerfile
```dockerfile
# Dockerfile
FROM node:14-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

#### Lab 2: Docker Compose Setup / Thiết lập Docker Compose
```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    depends_on:
      - db
  
  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### 2. Kubernetes Labs / Lab Kubernetes

#### Lab 1: Pod and Service / Pod và Service
```yaml
# pod-service.yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  containers:
  - name: myapp
    image: myapp:latest
    ports:
    - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer
```

#### Lab 2: Deployment and StatefulSet / Deployment và StatefulSet
```yaml
# deployment-statefulset.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
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
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: myapp-statefulset
spec:
  serviceName: myapp
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
        volumeMounts:
        - name: data
          mountPath: /data
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
```

## Projects / Dự án

### 1. Containerized Application / Ứng dụng container hóa
- Multi-container setup
- Service discovery
- Load balancing
- Monitoring

*Vietnamese:*
- Thiết lập đa container
- Khám phá dịch vụ
- Cân bằng tải
- Giám sát

### 2. Kubernetes Cluster / Cluster Kubernetes
- Cluster setup
- Application deployment
- Service mesh
- Monitoring

*Vietnamese:*
- Thiết lập cluster
- Triển khai ứng dụng
- Service mesh
- Giám sát

## Resources / Tài liệu

### 1. Documentation / Tài liệu
- Docker documentation
- Kubernetes guides
- Best practices
- Tutorials

*Vietnamese:*
- Tài liệu Docker
- Hướng dẫn Kubernetes
- Thực hành tốt nhất
- Hướng dẫn

### 2. Tools / Công cụ
- Docker
- Kubernetes
- Helm
- kubectl

*Vietnamese:*
- Docker
- Kubernetes
- Helm
- kubectl

## Assessment / Đánh giá

### 1. Knowledge Check / Kiểm tra kiến thức
- Container concepts
- Docker commands
- Kubernetes resources
- Best practices

*Vietnamese:*
- Khái niệm container
- Lệnh Docker
- Tài nguyên Kubernetes
- Thực hành tốt nhất

### 2. Practical Exercises / Bài tập thực hành
- Container creation
- Image management
- Cluster setup
- Application deployment

*Vietnamese:*
- Tạo container
- Quản lý image
- Thiết lập cluster
- Triển khai ứng dụng

## Certification Preparation / Chuẩn bị chứng chỉ

### 1. Available Certifications / Chứng chỉ có sẵn
- Docker Certified Associate
- Certified Kubernetes Administrator (CKA)
- Certified Kubernetes Application Developer (CKAD)
- AWS Certified DevOps Engineer

*Vietnamese:*
- Docker Certified Associate
- Certified Kubernetes Administrator (CKA)
- Certified Kubernetes Application Developer (CKAD)
- AWS Certified DevOps Engineer

### 2. Study Resources / Tài liệu học tập
- Official documentation
- Practice exams
- Study guides
- Online courses

*Vietnamese:*
- Tài liệu chính thức
- Bài thi thử
- Hướng dẫn học
- Khóa học trực tuyến

## Getting Started / Bắt đầu

1. **Prerequisites / Điều kiện tiên quyết**
   - Basic Linux knowledge
   - Networking concepts
   - Command line experience
   - System administration

2. **Setup / Thiết lập**
   ```bash
   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh

   # Install kubectl
   curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
   sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

   # Install minikube
   curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
   sudo install minikube-linux-amd64 /usr/local/bin/minikube
   ```

3. **Learning Path / Lộ trình học**
   - Start with Docker basics
   - Learn Kubernetes concepts
   - Practice with tools
   - Deploy applications

## Contributing / Đóng góp

We welcome contributions to improve the course materials:
Chúng tôi hoan nghênh đóng góp để cải thiện tài liệu khóa học:

1. **Content Updates / Cập nhật nội dung**
   - Technical accuracy
   - Best practices
   - New features
   - Workflow improvements

2. **Translation / Dịch thuật**
   - English to Vietnamese
   - Vietnamese to English
   - Technical terminology

3. **Lab Improvements / Cải thiện Lab**
   - New exercises
   - Real-world scenarios
   - Troubleshooting guides

## Support / Hỗ trợ

For support and questions:
Để được hỗ trợ và giải đáp thắc mắc:

1. **Documentation / Tài liệu**
   - Course materials
   - Lab guides
   - Troubleshooting guides

2. **Community / Cộng đồng**
   - Discussion forums
   - Q&A sessions
   - Knowledge sharing

3. **Technical Support / Hỗ trợ kỹ thuật**
   - Issue reporting
   - Bug fixes
   - Feature requests 
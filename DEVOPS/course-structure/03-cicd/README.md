# CI/CD (Continuous Integration/Continuous Deployment)
# CI/CD (Tích hợp liên tục/Triển khai liên tục)

## Overview / Tổng quan

This module covers the principles and practices of Continuous Integration and Continuous Deployment. You'll learn how to automate the software delivery process, implement CI/CD pipelines, and ensure reliable and efficient deployments.

Module này bao gồm các nguyên tắc và thực hành về Tích hợp liên tục và Triển khai liên tục. Bạn sẽ học cách tự động hóa quy trình phân phối phần mềm, triển khai pipeline CI/CD và đảm bảo các triển khai đáng tin cậy và hiệu quả.

## Learning Objectives / Mục tiêu học tập

### 1. CI Fundamentals / Kiến thức cơ bản về CI
- Build automation
- Test automation
- Code quality checks
- Artifact management
- Best practices

*Vietnamese:*
- Tự động hóa build
- Tự động hóa kiểm thử
- Kiểm tra chất lượng code
- Quản lý artifact
- Thực hành tốt nhất

### 2. CD Implementation / Triển khai CD
- Deployment strategies
- Environment management
- Release automation
- Rollback procedures
- Best practices

*Vietnamese:*
- Chiến lược triển khai
- Quản lý môi trường
- Tự động hóa phát hành
- Quy trình rollback
- Thực hành tốt nhất

## Lab Structure / Cấu trúc Lab

### 1. CI Labs / Lab CI

#### Lab 1: Jenkins Pipeline / Pipeline Jenkins
```groovy
// Jenkinsfile
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
        
        stage('Quality Check') {
            steps {
                sh 'sonar-scanner'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker build -t myapp:$BUILD_NUMBER .'
                sh 'docker push myapp:$BUILD_NUMBER'
            }
        }
    }
    
    post {
        always {
            junit '**/target/surefire-reports/*.xml'
            archiveArtifacts 'target/*.jar'
        }
    }
}
```

#### Lab 2: GitHub Actions Workflow / Quy trình GitHub Actions
```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up JDK
      uses: actions/setup-java@v2
      with:
        java-version: '11'
        
    - name: Build with Maven
      run: mvn clean package
      
    - name: Run Tests
      run: mvn test
      
    - name: Upload Artifacts
      uses: actions/upload-artifact@v2
      with:
        name: application
        path: target/*.jar
```

### 2. CD Labs / Lab CD

#### Lab 1: Kubernetes Deployment / Triển khai Kubernetes
```yaml
# deployment.yaml
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
        - containerPort: 8080
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
```

#### Lab 2: ArgoCD Application / Ứng dụng ArgoCD
```yaml
# application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/your-repo.git
    targetRevision: HEAD
    path: k8s
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

## Projects / Dự án

### 1. CI/CD Pipeline / Pipeline CI/CD
- Build automation
- Test automation
- Deployment automation
- Monitoring

*Vietnamese:*
- Tự động hóa build
- Tự động hóa kiểm thử
- Tự động hóa triển khai
- Giám sát

### 2. Release Management / Quản lý phát hành
- Version control
- Release planning
- Deployment strategies
- Rollback procedures

*Vietnamese:*
- Quản lý phiên bản
- Lập kế hoạch phát hành
- Chiến lược triển khai
- Quy trình rollback

## Resources / Tài liệu

### 1. Documentation / Tài liệu
- CI/CD guides
- Tool documentation
- Best practices
- Case studies

*Vietnamese:*
- Hướng dẫn CI/CD
- Tài liệu công cụ
- Thực hành tốt nhất
- Nghiên cứu tình huống

### 2. Tools / Công cụ
- Jenkins
- GitHub Actions
- ArgoCD
- Kubernetes

*Vietnamese:*
- Jenkins
- GitHub Actions
- ArgoCD
- Kubernetes

## Assessment / Đánh giá

### 1. Knowledge Check / Kiểm tra kiến thức
- CI/CD concepts
- Pipeline design
- Tool usage
- Best practices

*Vietnamese:*
- Khái niệm CI/CD
- Thiết kế pipeline
- Sử dụng công cụ
- Thực hành tốt nhất

### 2. Practical Exercises / Bài tập thực hành
- Pipeline setup
- Automation implementation
- Deployment configuration
- Monitoring setup

*Vietnamese:*
- Thiết lập pipeline
- Triển khai tự động hóa
- Cấu hình triển khai
- Thiết lập giám sát

## Certification Preparation / Chuẩn bị chứng chỉ

### 1. Available Certifications / Chứng chỉ có sẵn
- Jenkins Certified Engineer
- GitHub Actions Certified
- ArgoCD Certified
- AWS Certified DevOps Engineer

*Vietnamese:*
- Jenkins Certified Engineer
- GitHub Actions Certified
- ArgoCD Certified
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
   - Version control knowledge
   - Basic scripting
   - Container concepts
   - Cloud platform basics

2. **Setup / Thiết lập**
   ```bash
   # Install Jenkins
   wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
   sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
   sudo apt-get update
   sudo apt-get install jenkins

   # Install ArgoCD CLI
   curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
   sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
   rm argocd-linux-amd64
   ```

3. **Learning Path / Lộ trình học**
   - Start with CI basics
   - Learn CD concepts
   - Practice with tools
   - Implement pipelines

## Contributing / Đóng góp

We welcome contributions to improve the course materials:
Chúng tôi hoan nghênh đóng góp để cải thiện tài liệu khóa học:

1. **Content Updates / Cập nhật nội dung**
   - Technical accuracy
   - Best practices
   - New tools
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
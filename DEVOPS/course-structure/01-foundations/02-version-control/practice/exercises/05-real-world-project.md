# Bài tập 5: Dự án Thực tế - Microservices với DevOps

## Mục tiêu
Xây dựng và triển khai một ứng dụng microservices sử dụng các công nghệ và kỹ năng DevOps hiện đại.

## Yêu cầu

### 1. Kiến trúc Hệ thống
- Frontend: React.js
- Backend Services:
  - User Service (Node.js/Express)
  - Product Service (Node.js/Express)
  - Order Service (Node.js/Express)
- Database: PostgreSQL
- Message Queue: RabbitMQ
- Cache: Redis
- API Gateway: Nginx

### 2. Cấu trúc Repository
```
project/
├── .github/
│   └── workflows/
│       ├── frontend.yml
│       ├── backend.yml
│       └── infrastructure.yml
├── frontend/
│   ├── src/
│   ├── tests/
│   ├── Dockerfile
│   └── package.json
├── services/
│   ├── user-service/
│   ├── product-service/
│   └── order-service/
├── infrastructure/
│   ├── terraform/
│   ├── kubernetes/
│   └── ansible/
└── docs/
```

### 3. Các bước thực hiện

#### 3.1. Thiết lập Môi trường Phát triển
```bash
# Cài đặt các công cụ cần thiết
brew install docker docker-compose kubectl terraform ansible

# Clone repository
git clone https://github.com/your-org/microservices-project.git
cd microservices-project

# Tạo các branch
git checkout -b develop
git checkout -b feature/setup-infrastructure
```

#### 3.2. Cấu hình CI/CD
1. Tạo GitHub Actions workflows:
   - Kiểm tra code style
   - Chạy unit tests
   - Build Docker images
   - Push to container registry
   - Deploy to staging/production

2. Cấu hình GitLab CI/CD (nếu sử dụng GitLab):
   - Tương tự như GitHub Actions
   - Thêm các stage cho security scanning

#### 3.3. Infrastructure as Code
1. Terraform:
   - VPC và Networking
   - Kubernetes cluster
   - Database instances
   - Load balancers
   - Security groups

2. Kubernetes:
   - Deployments
   - Services
   - ConfigMaps
   - Secrets
   - Ingress rules

#### 3.4. Monitoring và Logging
1. Prometheus:
   - Service metrics
   - Node metrics
   - Custom metrics

2. Grafana:
   - Dashboards
   - Alerts

3. ELK Stack:
   - Log collection
   - Log analysis
   - Log visualization

#### 3.5. Security
1. Container Security:
   - Image scanning
   - Runtime security
   - Network policies

2. Application Security:
   - OWASP guidelines
   - Security headers
   - Rate limiting

3. Infrastructure Security:
   - IAM policies
   - Network security
   - Encryption

### 4. Quy trình làm việc

#### 4.1. Phát triển
1. Tạo feature branch
2. Phát triển tính năng
3. Viết tests
4. Tạo pull request
5. Code review
6. Merge vào develop

#### 4.2. Testing
1. Unit tests
2. Integration tests
3. End-to-end tests
4. Performance tests
5. Security tests

#### 4.3. Deployment
1. Staging deployment
2. UAT testing
3. Production deployment
4. Post-deployment verification

### 5. Các công nghệ sử dụng
- Version Control: Git, GitHub/GitLab
- CI/CD: GitHub Actions/GitLab CI
- Container: Docker, Docker Compose
- Orchestration: Kubernetes
- IaC: Terraform, Ansible
- Monitoring: Prometheus, Grafana
- Logging: ELK Stack
- Security: SonarQube, Trivy

### 6. Tài liệu cần tạo
1. Architecture Documentation
2. API Documentation
3. Deployment Guide
4. Monitoring Guide
5. Security Guidelines
6. Troubleshooting Guide

### 7. Deliverables
1. Source code với đầy đủ tests
2. Infrastructure code
3. CI/CD pipelines
4. Monitoring dashboards
5. Documentation
6. Security reports

### 8. Tiêu chí đánh giá
1. Code Quality
   - Test coverage > 80%
   - No critical security issues
   - Clean code practices

2. Infrastructure
   - IaC best practices
   - Security compliance
   - Scalability

3. DevOps Practices
   - Automated deployments
   - Monitoring coverage
   - Incident response

4. Documentation
   - Completeness
   - Clarity
   - Maintainability

## Tài liệu tham khảo
- [Microservices Architecture](https://microservices.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Terraform Documentation](https://www.terraform.io/docs/)
- [Prometheus Documentation](https://prometheus.io/docs/)
- [OWASP Security Guidelines](https://owasp.org/www-project-top-ten/) 
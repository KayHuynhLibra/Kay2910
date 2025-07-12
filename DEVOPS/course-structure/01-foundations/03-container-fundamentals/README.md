# Container Fundamentals

## Tổng quan
Module này cung cấp kiến thức về container và Docker, từ cơ bản đến nâng cao, tập trung vào việc xây dựng và quản lý container trong môi trường DevOps.

## Nội dung

### Tuần 1: Docker Basics
- Container concepts
  - What are containers
  - Container vs VM
  - Container lifecycle
  - Container architecture
- Docker installation
  - System requirements
  - Installation steps
  - Configuration
  - Verification
- Basic commands
  - docker run
  - docker build
  - docker ps
  - docker images
- Dockerfile
  - Basic syntax
  - Best practices
  - Multi-stage builds
  - Optimization

### Tuần 2: Docker Advanced
- Multi-stage builds
  - Build optimization
  - Size reduction
  - Security improvement
- Docker Compose
  - Compose file
  - Services
  - Networks
  - Volumes
- Docker networking
  - Network types
  - Network drivers
  - Network security
  - Service discovery
- Docker volumes
  - Volume types
  - Volume management
  - Data persistence
  - Backup strategies

### Tuần 3: Container Security
- Security best practices
  - Image security
  - Runtime security
  - Network security
  - Access control
- Image scanning
  - Vulnerability scanning
  - Dependency checking
  - Compliance scanning
  - Remediation
- Runtime security
  - Container isolation
  - Resource limits
  - Security profiles
  - Monitoring
- Compliance
  - Security standards
  - Compliance tools
  - Audit trails
  - Reporting

### Tuần 4: Container Orchestration
- Kubernetes basics
  - Architecture
  - Components
  - API resources
  - Basic concepts
- Pods và Services
  - Pod lifecycle
  - Service types
  - Service discovery
  - Load balancing
- Deployments
  - Deployment strategies
  - Rolling updates
  - Rollbacks
  - Scaling
- StatefulSets
  - Stateful applications
  - Storage management
  - Data persistence
  - High availability

## Cấu trúc thư mục
```
03-container-fundamentals/
├── theory/
│   ├── 01-docker-basics.md
│   ├── 02-docker-advanced.md
│   ├── 03-container-security.md
│   └── 04-container-orchestration.md
├── practice/
│   ├── exercises/
│   └── solutions/
├── labs/
│   ├── 01-docker-basics/
│   ├── 02-docker-compose/
│   └── 03-kubernetes-basics/
└── projects/
    ├── 01-containerized-app/
    └── 02-microservices/
```

## Dự án
1. Containerized Application
   - Mục tiêu: Containerize một ứng dụng web
   - Kỹ năng: Docker, Docker Compose
   - Thời gian: 1 tuần

2. Microservices Architecture
   - Mục tiêu: Xây dựng kiến trúc microservices
   - Kỹ năng: Docker, Kubernetes
   - Thời gian: 2 tuần

## Tài liệu tham khảo
- Docker Documentation
- Kubernetes Documentation
- Container Security Best Practices
- Microservices Patterns 
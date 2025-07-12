# Changelog - DevOps Course Development

## [1.0.0] - 2024-03-XX

### Added
- Tạo cấu trúc khóa học DevOps toàn diện
  - 4 phần chính: Foundations, Cloud & Infrastructure, CI/CD & Automation, Advanced Topics
  - Thời gian học: 18 tháng
  - Cấu trúc module rõ ràng với lý thuyết và thực hành
- Phát triển module Linux Fundamentals
  - 4 tuần học tập trung
  - Bài tập thực hành chi tiết
  - Lab system administration
  - Dự án thực tế: System Monitor
- Tạo các bài tập thực hành và lab
  - Bài tập về file system
  - Bài tập về process management
  - Bài tập về networking
  - Lab system administration
- Phát triển dự án System Monitor
  - Giám sát tài nguyên hệ thống
  - Hệ thống cảnh báo đa kênh
  - Báo cáo tự động
  - Tích hợp với systemd

### Technical Details

#### System Monitor Features
- **Resource Monitoring**
  - CPU usage tracking
  - Memory utilization
  - Disk space monitoring
  - Network connectivity checks
  - Process monitoring

- **Alert System**
  - Email notifications
  - Slack integration
  - SMS alerts (optional)
  - Alert escalation rules
  - Customizable thresholds

- **Reporting**
  - Daily HTML reports
  - Resource usage graphs
  - Alert history
  - System recommendations
  - Customizable templates

- **Security**
  - Secure configuration
  - Log rotation
  - Access control
  - Audit logging
  - Systemd integration

### Files Created

#### Course Structure
- `course-structure/README.md` - Cấu trúc tổng quan khóa học
  - Mô tả các module
  - Yêu cầu hệ thống
  - Hướng dẫn cài đặt
  - Cấu trúc thư mục
- `course-structure/CHANGELOG.md` - Lịch sử phát triển

#### Linux Fundamentals Module
- `course-structure/01-foundations/01-linux-fundamentals/README.md` - Tổng quan module
  - Mục tiêu học tập
  - Nội dung chi tiết
  - Yêu cầu tiên quyết
  - Tài nguyên học tập
- `course-structure/01-foundations/01-linux-fundamentals/theory/01-linux-basics.md` - Tài liệu lý thuyết
  - File system operations
  - Process management
  - Networking basics
  - System administration
- `course-structure/01-foundations/01-linux-fundamentals/assessment/quiz.md` - Bài kiểm tra
  - Câu hỏi trắc nghiệm
  - Bài tập thực hành
  - Kịch bản thực tế

#### Practice Exercises
- `course-structure/01-foundations/01-linux-fundamentals/practice/exercises/01-file-system.sh` - Bài tập về file system
  - Tạo và quản lý thư mục
  - Phân quyền file
  - Quản lý symbolic links
- `course-structure/01-foundations/01-linux-fundamentals/practice/exercises/02-process-management.sh` - Bài tập về quản lý process
  - Process creation và termination
  - Signal handling
  - Process monitoring
- `course-structure/01-foundations/01-linux-fundamentals/practice/exercises/03-networking.sh` - Bài tập về networking
  - Network configuration
  - Connectivity testing
  - Port scanning
  - DNS resolution

#### Labs
- `course-structure/01-foundations/01-linux-fundamentals/labs/01-system-admin-lab.sh` - Lab về system administration
  - User management
  - Service configuration
  - Log management
  - Security basics

#### Projects
- `course-structure/01-foundations/01-linux-fundamentals/projects/01-system-monitor.md` - Yêu cầu dự án System Monitor
  - Mục tiêu dự án
  - Yêu cầu kỹ thuật
  - Tiêu chí đánh giá
  - Timeline

#### Project Solutions
- `course-structure/01-foundations/01-linux-fundamentals/projects/solutions/monitor.sh` - Script giám sát hệ thống
  - Resource monitoring
  - Log management
  - Report generation
- `course-structure/01-foundations/01-linux-fundamentals/projects/solutions/alert.sh` - Script xử lý cảnh báo
  - Alert generation
  - Notification handling
  - Escalation rules
- `course-structure/01-foundations/01-linux-fundamentals/projects/solutions/thresholds.conf` - Cấu hình ngưỡng cảnh báo
  - Resource thresholds
  - Monitoring intervals
  - Alert settings
- `course-structure/01-foundations/01-linux-fundamentals/projects/solutions/system-monitor.service` - File service systemd
  - Service configuration
  - Security settings
  - Resource limits
- `course-structure/01-foundations/01-linux-fundamentals/projects/solutions/install.sh` - Script cài đặt
  - Directory creation
  - File copying
  - Dependency installation
  - Service setup
- `course-structure/01-foundations/01-linux-fundamentals/projects/solutions/test.sh` - Script kiểm thử
  - Unit tests
  - Integration tests
  - Performance tests
- `course-structure/01-foundations/01-linux-fundamentals/projects/solutions/report_template.html` - Template báo cáo
  - HTML structure
  - CSS styling
  - JavaScript functionality
- `course-structure/01-foundations/01-linux-fundamentals/projects/solutions/logrotate.conf` - Cấu hình log rotation
  - Log retention
  - Compression settings
  - Rotation schedule
- `course-structure/01-foundations/01-linux-fundamentals/projects/solutions/README.md` - Hướng dẫn sử dụng
  - Installation guide
  - Configuration guide
  - Usage examples
  - Troubleshooting

### Development History

1. Tạo cấu trúc khóa học cơ bản
   - Định nghĩa các module chính
     - Foundations (3 tháng)
     - Cloud & Infrastructure (4 tháng)
     - CI/CD & Automation (3 tháng)
     - Advanced Topics (2 tháng)
   - Tạo cấu trúc thư mục
     - Theory
     - Practice
     - Labs
     - Projects
   - Viết README tổng quan
     - Course overview
     - Prerequisites
     - Learning path
     - Resources

2. Phát triển module Linux Fundamentals
   - Viết tài liệu lý thuyết
     - File system operations
     - Process management
     - Networking basics
     - System administration
   - Tạo bài tập thực hành
     - File system exercises
     - Process management exercises
     - Networking exercises
   - Phát triển lab system administration
     - User management
     - Service configuration
     - Log management
     - Security basics

3. Phát triển dự án System Monitor
   - Thiết kế kiến trúc hệ thống
     - Monitoring components
     - Alert system
     - Reporting system
   - Viết các script chính
     - monitor.sh
     - alert.sh
     - install.sh
   - Tạo cấu hình và service
     - thresholds.conf
     - system-monitor.service
     - logrotate.conf
   - Viết tài liệu hướng dẫn
     - Installation guide
     - Configuration guide
     - Usage examples
     - Troubleshooting

4. Hoàn thiện tài liệu
   - Viết bài kiểm tra
     - Multiple choice questions
     - Practical exercises
     - Scenario-based questions
   - Tạo hướng dẫn sử dụng
     - Step-by-step instructions
     - Examples
     - Best practices
   - Viết tài liệu cài đặt
     - System requirements
     - Installation steps
     - Configuration options

### Next Steps
- Phát triển các module tiếp theo
  - Version Control
  - Container Fundamentals
  - Cloud Fundamentals
  - Infrastructure as Code
- Bổ sung bài tập và lab
  - Git exercises
  - Docker labs
  - Kubernetes labs
  - Terraform exercises
- Cập nhật tài liệu
  - Add more examples
  - Improve documentation
  - Add troubleshooting guides
  - Create video tutorials
- Thêm tính năng cho dự án System Monitor
  - Web interface
  - API integration
  - Custom metrics
  - Advanced reporting
  - Security features

### Build & Development

#### Build Process
- **Environment Setup**
  - Docker containerization
  - CI/CD pipeline với GitHub Actions
  - Automated testing
  - Documentation generation

- **Build Tools**
  - Makefile cho automation
  - Shell scripts cho deployment
  - Docker Compose cho development
  - Kubernetes cho production

- **Quality Assurance**
  - Unit testing với Bats
  - Integration testing
  - Performance testing
  - Security scanning

#### Technologies Stack

##### Core Technologies
- **Operating Systems**
  - Linux (Ubuntu 20.04+)
  - Windows with WSL2
  - macOS

- **Container & Orchestration**
  - Docker 24.0+
  - Kubernetes 1.28+
  - Docker Compose 2.20+

- **Version Control**
  - Git 2.40+
  - GitHub
  - GitLab

- **CI/CD Tools**
  - GitHub Actions
  - Jenkins
  - GitLab CI

##### Development Tools
- **IDE & Editors**
  - VS Code
  - Vim/Neovim
  - JetBrains IDEs

- **Terminal Tools**
  - tmux
  - zsh
  - oh-my-zsh

- **Monitoring Tools**
  - Prometheus
  - Grafana
  - ELK Stack

#### Development Workflow

##### Local Development
1. **Environment Setup**
   ```bash
   # Clone repository
   git clone https://github.com/your-username/devops-course.git
   cd devops-course

   # Setup development environment
   make setup-dev
   ```

2. **Development Process**
   ```bash
   # Start development environment
   make dev

   # Run tests
   make test

   # Build documentation
   make docs
   ```

3. **Testing**
   ```bash
   # Run all tests
   make test-all

   # Run specific test suite
   make test-unit
   make test-integration
   make test-performance
   ```

##### CI/CD Pipeline

1. **Build Pipeline**
   ```yaml
   name: Build & Test
   on: [push, pull_request]
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - name: Setup environment
           run: make setup
         - name: Run tests
           run: make test-all
         - name: Build documentation
           run: make docs
   ```

2. **Deployment Pipeline**
   ```yaml
   name: Deploy
   on:
     push:
       tags:
         - 'v*'
   jobs:
     deploy:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - name: Deploy to production
           run: make deploy
   ```

#### Build Scripts

##### Makefile
```makefile
.PHONY: setup dev test docs clean

setup:
	@echo "Setting up development environment..."
	./scripts/setup.sh

dev:
	@echo "Starting development environment..."
	docker-compose up -d

test:
	@echo "Running tests..."
	./scripts/run-tests.sh

docs:
	@echo "Building documentation..."
	./scripts/build-docs.sh

clean:
	@echo "Cleaning up..."
	./scripts/cleanup.sh
```

##### Docker Configuration
```dockerfile
# Development environment
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    vim \
    tmux \
    docker.io \
    kubectl

# Production environment
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y \
    docker.io \
    kubectl
```

#### Performance Optimization

##### Resource Limits
```yaml
# Docker resource limits
resources:
  limits:
    cpu: "2"
    memory: "4G"
  requests:
    cpu: "1"
    memory: "2G"
```

##### Caching Strategy
```yaml
# Docker layer caching
cache:
  paths:
    - node_modules/
    - .cache/
    - vendor/
```

#### Security Measures

##### Security Scanning
```yaml
# Security scan configuration
security:
  tools:
    - trivy
    - snyk
    - sonarqube
  schedule: "0 0 * * *"
```

##### Access Control
```yaml
# Access control configuration
access:
  roles:
    - admin
    - developer
    - student
  permissions:
    admin:
      - all
    developer:
      - read
      - write
    student:
      - read
```

#### Documentation

##### API Documentation
```yaml
# API documentation configuration
api-docs:
  format: openapi
  version: 3.0.0
  output: docs/api
```

##### Code Documentation
```yaml
# Code documentation configuration
code-docs:
  format: markdown
  output: docs/code
  languages:
    - bash
    - python
    - javascript
```

#### Monitoring & Logging

##### Monitoring Setup
```yaml
# Monitoring configuration
monitoring:
  tools:
    - prometheus
    - grafana
  metrics:
    - cpu
    - memory
    - disk
    - network
```

##### Logging Configuration
```yaml
# Logging configuration
logging:
  format: json
  level: info
  output:
    - file
    - stdout
  retention: 30d
```

### Release Management

#### Versioning Strategy
```yaml
# Semantic Versioning (MAJOR.MINOR.PATCH)
versioning:
  major: "Breaking changes"
  minor: "New features, backward compatible"
  patch: "Bug fixes, backward compatible"
  pre-release: "alpha, beta, rc"
```

#### Release Process
1. **Version Planning**
   ```bash
   # Check current version
   git describe --tags

   # Create new version
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

2. **Release Checklist**
   - [ ] Update version numbers
   - [ ] Update changelog
   - [ ] Run full test suite
   - [ ] Build documentation
   - [ ] Create release notes
   - [ ] Tag release
   - [ ] Deploy to production

3. **Release Automation**
   ```yaml
   # Release workflow
   name: Release
   on:
     push:
       tags:
         - 'v*'
   jobs:
     release:
       runs-on: ubuntu-latest
       steps:
         - name: Create Release
           uses: actions/create-release@v1
         - name: Build Assets
           run: make build-all
         - name: Upload Assets
           uses: actions/upload-release-asset@v1
   ```

### Contribution Guidelines

#### Development Setup
1. **Fork & Clone**
   ```bash
   # Fork repository
   # Clone your fork
   git clone https://github.com/your-username/devops-course.git
   cd devops-course

   # Add upstream
   git remote add upstream https://github.com/original/devops-course.git
   ```

2. **Branch Strategy**
   ```bash
   # Create feature branch
   git checkout -b feature/your-feature

   # Create bugfix branch
   git checkout -b fix/your-fix

   # Create release branch
   git checkout -b release/v1.0.0
   ```

3. **Commit Guidelines**
   ```bash
   # Commit format
   type(scope): description

   # Types
   - feat: New feature
   - fix: Bug fix
   - docs: Documentation
   - style: Formatting
   - refactor: Code restructuring
   - test: Testing
   - chore: Maintenance
   ```

#### Code Review Process
1. **Pull Request Template**
   ```markdown
   ## Description
   [Describe your changes]

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation
   - [ ] Breaking change

   ## Checklist
   - [ ] Tests added/updated
   - [ ] Documentation updated
   - [ ] Code follows style guide
   - [ ] Self-reviewed
   ```

2. **Review Guidelines**
   - Code quality
   - Test coverage
   - Documentation
   - Performance impact
   - Security considerations

### Troubleshooting Guide

#### Common Issues

1. **Build Failures**
   ```bash
   # Check build logs
   make build --debug

   # Clean and rebuild
   make clean
   make build

   # Check dependencies
   make check-deps
   ```

2. **Test Failures**
   ```bash
   # Run specific test
   make test TEST=test-name

   # Debug test
   make test-debug TEST=test-name

   # Check test coverage
   make coverage
   ```

3. **Deployment Issues**
   ```bash
   # Check deployment status
   kubectl get pods
   kubectl describe pod <pod-name>

   # Check logs
   kubectl logs <pod-name>
   kubectl logs <pod-name> --previous

   # Check events
   kubectl get events
   ```

#### Debug Tools
```yaml
# Debug configuration
debug:
  tools:
    - kubectl
    - docker
    - curl
    - netstat
    - tcpdump
  log_level: debug
  trace: true
```

### Performance Benchmarks

#### Resource Usage
```yaml
# Resource benchmarks
benchmarks:
  cpu:
    idle: "0.1%"
    normal: "5-10%"
    peak: "30-40%"
  memory:
    idle: "100MB"
    normal: "500MB"
    peak: "1GB"
  disk:
    read: "100MB/s"
    write: "50MB/s"
  network:
    latency: "<50ms"
    throughput: "100MB/s"
```

#### Load Testing
```yaml
# Load test configuration
load_test:
  tools:
    - k6
    - locust
    - jmeter
  scenarios:
    - name: "Normal load"
      users: 100
      duration: "5m"
    - name: "Peak load"
      users: 1000
      duration: "1h"
```

#### Performance Metrics
```yaml
# Performance metrics
metrics:
  response_time:
    p50: "<100ms"
    p90: "<200ms"
    p99: "<500ms"
  error_rate:
    threshold: "<0.1%"
  availability:
    target: "99.9%"
```

### Security Guidelines

#### Security Scanning
```yaml
# Security scan configuration
security:
  tools:
    - trivy
    - snyk
    - sonarqube
  schedule: "0 0 * * *"
  severity_threshold: "HIGH"
```

#### Access Control
```yaml
# Access control configuration
access:
  roles:
    - admin
    - developer
    - student
  permissions:
    admin:
      - all
    developer:
      - read
      - write
    student:
      - read
```

#### Security Best Practices
1. **Code Security**
   - Input validation
   - Output encoding
   - Secure dependencies
   - Regular updates

2. **Infrastructure Security**
   - Network policies
   - Pod security
   - Secret management
   - RBAC

3. **Monitoring & Alerting**
   - Security events
   - Anomaly detection
   - Audit logging
   - Incident response

### Documentation Standards

#### Code Documentation
```yaml
# Code documentation
code_docs:
  format: markdown
  required:
    - function description
    - parameters
    - return values
    - examples
    - error handling
```

#### API Documentation
```yaml
# API documentation
api_docs:
  format: openapi
  version: 3.0.0
  required:
    - endpoints
    - parameters
    - responses
    - examples
    - error codes
```

#### User Documentation
```yaml
# User documentation
user_docs:
  sections:
    - getting_started
    - installation
    - configuration
    - usage
    - troubleshooting
    - faq
  format: markdown
  examples: required
```

### Project Structure

#### Root Directory
```
course-structure/
├── README.md                 # Tổng quan khóa học
├── CHANGELOG.md             # Lịch sử phát triển
├── LICENSE                  # Giấy phép MIT
└── .gitignore              # Git ignore rules
```

#### Foundations Module
```
course-structure/01-foundations/
├── 01-linux-fundamentals/   # Module Linux cơ bản
├── 02-version-control/      # Module Version Control
├── 03-container-basics/     # Module Container cơ bản
└── 04-networking-basics/    # Module Networking cơ bản
```

#### Linux Fundamentals Module
```
course-structure/01-foundations/01-linux-fundamentals/
├── README.md               # Tổng quan module
├── theory/                 # Tài liệu lý thuyết
│   ├── 01-linux-basics.md
│   ├── 02-file-system.md
│   ├── 03-process-management.md
│   └── 04-networking.md
├── practice/              # Bài tập thực hành
│   ├── exercises/
│   │   ├── 01-file-system.sh
│   │   ├── 02-process-management.sh
│   │   └── 03-networking.sh
│   └── solutions/
│       ├── 01-file-system-solution.sh
│       ├── 02-process-management-solution.sh
│       └── 03-networking-solution.sh
├── labs/                  # Lab thực hành
│   ├── 01-system-admin-lab.sh
│   └── solutions/
│       └── 01-system-admin-lab-solution.sh
├── projects/             # Dự án thực tế
│   ├── 01-system-monitor.md
│   └── solutions/
│       ├── monitor.sh
│       ├── alert.sh
│       ├── thresholds.conf
│       ├── system-monitor.service
│       ├── install.sh
│       ├── test.sh
│       ├── report_template.html
│       ├── logrotate.conf
│       └── README.md
└── assessment/           # Đánh giá
    ├── quiz.md
    └── project-guidelines.md
```

#### Version Control Module
```
course-structure/01-foundations/02-version-control/
├── README.md
├── theory/
│   ├── 01-git-basics.md
│   ├── 02-branching-strategies.md
│   └── 03-collaboration.md
├── practice/
│   ├── exercises/
│   │   ├── 01-basic-commands.sh
│   │   ├── 02-branching.sh
│   │   └── 03-collaboration.sh
│   └── solutions/
├── labs/
│   ├── 01-team-workflow.sh
│   └── solutions/
└── assessment/
```

#### Container Basics Module
```
course-structure/01-foundations/03-container-basics/
├── README.md
├── theory/
│   ├── 01-docker-basics.md
│   ├── 02-container-lifecycle.md
│   └── 03-docker-compose.md
├── practice/
│   ├── exercises/
│   │   ├── 01-docker-commands.sh
│   │   ├── 02-dockerfile.sh
│   │   └── 03-docker-compose.sh
│   └── solutions/
├── labs/
│   ├── 01-container-app.sh
│   └── solutions/
└── assessment/
```

#### Networking Basics Module
```
course-structure/01-foundations/04-networking-basics/
├── README.md
├── theory/
│   ├── 01-network-fundamentals.md
│   ├── 02-protocols.md
│   └── 03-security.md
├── practice/
│   ├── exercises/
│   │   ├── 01-network-config.sh
│   │   ├── 02-protocol-testing.sh
│   │   └── 03-security.sh
│   └── solutions/
├── labs/
│   ├── 01-network-setup.sh
│   └── solutions/
└── assessment/
```

### File Content Guidelines

#### Theory Files
```markdown
# Module Title

## Overview
- Learning objectives
- Prerequisites
- Duration

## Content
1. Main topic
   - Sub-topic 1
   - Sub-topic 2
   - Examples
   - Best practices

2. Main topic
   - Sub-topic 1
   - Sub-topic 2
   - Examples
   - Best practices

## Summary
- Key points
- Further reading
- References
```

#### Exercise Files
```bash
#!/bin/bash

# Exercise Title
echo "Exercise: [Title]"

# Goal
echo "Goal: [Description]"

# Tasks
echo "Tasks:"
echo "1. [Task 1]"
echo "2. [Task 2]"
echo "3. [Task 3]"

# Instructions
echo "Instructions:"
echo "[Detailed instructions]"

# Verification
echo "Verification:"
echo "[How to verify completion]"

# Cleanup
echo "Cleanup:"
echo "[Cleanup instructions]"
```

#### Lab Files
```bash
#!/bin/bash

# Lab Title
echo "Lab: [Title]"

# Objectives
echo "Objectives:"
echo "1. [Objective 1]"
echo "2. [Objective 2]"
echo "3. [Objective 3]"

# Prerequisites
echo "Prerequisites:"
echo "- [Prerequisite 1]"
echo "- [Prerequisite 2]"

# Setup
echo "Setup:"
echo "[Setup instructions]"

# Tasks
echo "Tasks:"
echo "1. [Task 1]"
echo "2. [Task 2]"
echo "3. [Task 3]"

# Verification
echo "Verification:"
echo "[Verification steps]"

# Cleanup
echo "Cleanup:"
echo "[Cleanup instructions]"
```

#### Project Files
```markdown
# Project Title

## Overview
- Project description
- Learning objectives
- Prerequisites

## Requirements
1. Functional requirements
2. Technical requirements
3. Performance requirements

## Deliverables
1. Source code
2. Documentation
3. Test cases

## Timeline
- Start date
- Milestones
- Due date

## Evaluation Criteria
1. Functionality
2. Code quality
3. Documentation
4. Performance
```

#### Assessment Files
```markdown
# Assessment Title

## Quiz
1. Multiple choice questions
2. True/False questions
3. Short answer questions

## Practical Exercises
1. Exercise 1
   - Requirements
   - Evaluation criteria
2. Exercise 2
   - Requirements
   - Evaluation criteria

## Project
1. Project requirements
2. Evaluation criteria
3. Submission guidelines
```

### File Naming Conventions

#### Theory Files
- Use kebab-case: `01-topic-name.md`
- Include module number: `01-`, `02-`, etc.
- Use descriptive names

#### Exercise Files
- Use kebab-case: `01-exercise-name.sh`
- Include exercise number
- Use `.sh` extension for shell scripts

#### Lab Files
- Use kebab-case: `01-lab-name.sh`
- Include lab number
- Use `.sh` extension for shell scripts

#### Project Files
- Use kebab-case: `01-project-name.md`
- Include project number
- Use appropriate extensions

### Directory Structure Rules

1. **Module Structure**
   - Each module has its own directory
   - Follow consistent structure
   - Include README.md

2. **Practice Structure**
   - Separate exercises and solutions
   - Include verification steps
   - Include cleanup instructions

3. **Lab Structure**
   - Include setup instructions
   - Include verification steps
   - Include cleanup instructions

4. **Project Structure**
   - Include requirements
   - Include evaluation criteria
   - Include submission guidelines

### Detailed Content Guidelines

#### Module Content Structure

##### Linux Fundamentals Module
```markdown
# Linux Fundamentals

## Week 1: File System Operations
### Theory
- File system hierarchy
- Basic commands (ls, cd, pwd)
- File operations (cp, mv, rm)
- File permissions
- Links (hard and symbolic)

### Practice
- Directory navigation
- File manipulation
- Permission management
- Link creation

### Lab
- File system organization
- Permission setup
- Backup procedures

## Week 2: Process Management
### Theory
- Process lifecycle
- Process states
- Signals
- Job control
- Process monitoring

### Practice
- Process creation
- Signal handling
- Job management
- Resource monitoring

### Lab
- Service management
- Process automation
- Resource optimization

## Week 3: System Administration
### Theory
- User management
- Service management
- Log management
- Security basics

### Practice
- User administration
- Service configuration
- Log analysis
- Security setup

### Lab
- System setup
- Service deployment
- Security hardening

## Week 4: Networking
### Theory
- TCP/IP fundamentals
- Network configuration
- Firewall management
- Troubleshooting

### Practice
- Network setup
- Firewall rules
- Connectivity testing
- Problem resolution

### Lab
- Network configuration
- Service exposure
- Security implementation
```

##### Version Control Module
```markdown
# Version Control

## Week 1: Git Basics
### Theory
- Version control concepts
- Git workflow
- Basic commands
- Repository management

### Practice
- Repository creation
- Basic operations
- Branch management
- Remote operations

### Lab
- Project setup
- Collaboration workflow
- Conflict resolution

## Week 2: Advanced Git
### Theory
- Branching strategies
- Merge techniques
- Rebase operations
- Git hooks

### Practice
- Branch management
- Merge conflicts
- Rebase workflow
- Hook implementation

### Lab
- Team workflow
- Release management
- Automation setup
```

#### Exercise Content Structure

##### File System Exercise
```bash
#!/bin/bash

# Exercise: File System Operations
echo "Exercise: File System Operations"

# Goal
echo "Goal: Master basic file system operations in Linux"

# Tasks
echo "Tasks:"
echo "1. Create directory structure"
echo "2. Manage file permissions"
echo "3. Create and manage links"
echo "4. Implement backup strategy"

# Instructions
echo "Instructions:"
echo "1. Create ~/devops-practice directory"
echo "2. Create subdirectories: bin, etc, var/log, var/www, tmp"
echo "3. Set appropriate permissions"
echo "4. Create symbolic links"
echo "5. Implement backup script"

# Verification
echo "Verification:"
echo "1. Check directory structure"
echo "2. Verify permissions"
echo "3. Test links"
echo "4. Validate backup"

# Cleanup
echo "Cleanup:"
echo "1. Remove practice directory"
echo "2. Clean temporary files"
```

#### Lab Content Structure

##### System Administration Lab
```bash
#!/bin/bash

# Lab: System Administration
echo "Lab: System Administration"

# Objectives
echo "Objectives:"
echo "1. Configure system services"
echo "2. Implement security measures"
echo "3. Set up monitoring"
echo "4. Manage system resources"

# Prerequisites
echo "Prerequisites:"
echo "- Linux system access"
echo "- Root privileges"
echo "- Basic Linux knowledge"

# Setup
echo "Setup:"
echo "1. Install required packages"
echo "2. Configure system settings"
echo "3. Set up monitoring tools"

# Tasks
echo "Tasks:"
echo "1. Service Configuration"
echo "   - Install and configure web server"
echo "   - Set up database service"
echo "   - Configure firewall"
echo "2. Security Implementation"
echo "   - User management"
echo "   - File permissions"
echo "   - Security policies"
echo "3. Monitoring Setup"
echo "   - Install monitoring tools"
echo "   - Configure alerts"
echo "   - Set up logging"

# Verification
echo "Verification:"
echo "1. Service status"
echo "2. Security checks"
echo "3. Monitoring validation"

# Cleanup
echo "Cleanup:"
echo "1. Remove test data"
echo "2. Reset configurations"
echo "3. Clean logs"
```

### Documentation Process

#### Content Creation Workflow
1. **Planning Phase**
   ```markdown
   ## Content Planning
   - Define learning objectives
   - Outline content structure
   - Identify prerequisites
   - Plan practical exercises
   ```

2. **Development Phase**
   ```markdown
   ## Content Development
   - Write theoretical content
   - Create practical exercises
   - Develop lab scenarios
   - Prepare assessment materials
   ```

3. **Review Phase**
   ```markdown
   ## Content Review
   - Technical accuracy
   - Clarity and readability
   - Exercise effectiveness
   - Assessment validity
   ```

4. **Update Phase**
   ```markdown
   ## Content Updates
   - Incorporate feedback
   - Update based on student performance
   - Add new examples
   - Improve explanations
   ```

#### Documentation Standards

##### Code Documentation
```markdown
# Code Documentation Standards

## Function Documentation
```bash
# Function: function_name
# Description: Detailed description of function purpose
# Parameters:
#   $1 - Parameter 1 description
#   $2 - Parameter 2 description
# Returns:
#   Description of return value
# Examples:
#   function_name arg1 arg2
```

## Script Documentation
```bash
#!/bin/bash
# Script: script_name.sh
# Purpose: Main purpose of the script
# Author: Author name
# Date: Creation date
# Version: 1.0
# Usage: ./script_name.sh [options]
# Options:
#   -h: Show help
#   -v: Verbose mode
```

## Configuration Documentation
```yaml
# Configuration: config_name.conf
# Purpose: Configuration file purpose
# Sections:
#   [section1]: Section 1 description
#   [section2]: Section 2 description
# Options:
#   option1: Option 1 description
#   option2: Option 2 description
```
```

### Content Validation Process

#### Validation Checklist
1. **Technical Accuracy**
   - [ ] Command syntax
   - [ ] Configuration parameters
   - [ ] Security considerations
   - [ ] Best practices

2. **Content Completeness**
   - [ ] Learning objectives
   - [ ] Prerequisites
   - [ ] Examples
   - [ ] Exercises
   - [ ] Solutions

3. **Practical Effectiveness**
   - [ ] Exercise difficulty
   - [ ] Lab scenarios
   - [ ] Real-world relevance
   - [ ] Time requirements

4. **Documentation Quality**
   - [ ] Clarity
   - [ ] Consistency
   - [ ] Formatting
   - [ ] References

#### Validation Tools
```yaml
# Validation Tools Configuration
validation:
  tools:
    - markdownlint
    - shellcheck
    - yamllint
    - linkchecker
  checks:
    - syntax
    - style
    - links
    - references
  reports:
    format: html
    output: validation-reports/
```

### Review Process

#### Review Guidelines
1. **Technical Review**
   ```markdown
   ## Technical Review Checklist
   - [ ] Command accuracy
   - [ ] Configuration validity
   - [ ] Security compliance
   - [ ] Performance considerations
   ```

2. **Content Review**
   ```markdown
   ## Content Review Checklist
   - [ ] Learning objectives
   - [ ] Content structure
   - [ ] Examples quality
   - [ ] Exercise effectiveness
   ```

3. **Documentation Review**
   ```markdown
   ## Documentation Review Checklist
   - [ ] Clarity
   - [ ] Consistency
   - [ ] Completeness
   - [ ] Formatting
   ```

#### Review Workflow
1. **Initial Review**
   - Content completeness
   - Technical accuracy
   - Format compliance

2. **Peer Review**
   - Technical validation
   - Content effectiveness
   - Documentation quality

3. **Final Review**
   - Integration testing
   - Performance validation
   - Security assessment

### Update Process

#### Update Guidelines
1. **Content Updates**
   ```markdown
   ## Content Update Process
   1. Identify update needs
   2. Plan changes
   3. Implement updates
   4. Validate changes
   5. Document updates
   ```

2. **Version Control**
   ```markdown
   ## Version Control Process
   1. Create feature branch
   2. Implement changes
   3. Test updates
   4. Create pull request
   5. Merge after approval
   ```

3. **Documentation Updates**
   ```markdown
   ## Documentation Update Process
   1. Update content
   2. Update references
   3. Update examples
   4. Update changelog
   ```

#### Update Workflow
1. **Change Management**
   - Change request
   - Impact assessment
   - Implementation plan
   - Testing strategy

2. **Quality Assurance**
   - Technical validation
   - Content review
   - Documentation check
   - Integration testing

3. **Deployment**
   - Version update
   - Content deployment
   - Documentation update
   - Announcement

### Backup & Disaster Recovery

#### Backup Strategy
```yaml
# Backup Configuration
backup:
  types:
    - full: "Daily full backup"
    - incremental: "Hourly incremental"
    - differential: "Weekly differential"
  retention:
    full: "30 days"
    incremental: "7 days"
    differential: "14 days"
  storage:
    local: "/backup/local"
    remote: "s3://backup-bucket"
  schedule:
    full: "0 0 * * *"
    incremental: "0 * * * *"
    differential: "0 0 * * 0"
```

#### Disaster Recovery Plan
```markdown
# Disaster Recovery Plan

## Recovery Objectives
- RTO (Recovery Time Objective): 4 hours
- RPO (Recovery Point Objective): 1 hour

## Recovery Procedures
1. System Recovery
   - Restore from backup
   - Verify system integrity
   - Test functionality

2. Data Recovery
   - Restore databases
   - Verify data consistency
   - Test data access

3. Service Recovery
   - Restore configurations
   - Start services
   - Verify connectivity
```

### Scaling & High Availability

#### Scaling Strategy
```yaml
# Scaling Configuration
scaling:
  horizontal:
    min_replicas: 2
    max_replicas: 10
    metrics:
      - cpu: "70%"
      - memory: "80%"
      - requests: "1000/s"
  vertical:
    resources:
      cpu: "4"
      memory: "8Gi"
    limits:
      cpu: "8"
      memory: "16Gi"
```

#### High Availability Setup
```yaml
# High Availability Configuration
ha:
  components:
    - load_balancer:
        type: "nginx"
        health_check: "/health"
        timeout: "5s"
    - database:
        type: "postgresql"
        replication: true
        failover: "automatic"
    - cache:
        type: "redis"
        cluster: true
        persistence: true
  monitoring:
    - health_checks
    - failover_tests
    - performance_metrics
```

### Monitoring & Alerting

#### Monitoring Setup
```yaml
# Monitoring Configuration
monitoring:
  tools:
    - prometheus:
        scrape_interval: "15s"
        retention: "15d"
    - grafana:
        dashboards:
          - system
          - application
          - business
    - alertmanager:
        receivers:
          - email
          - slack
          - pagerduty
  metrics:
    system:
      - cpu_usage
      - memory_usage
      - disk_usage
      - network_traffic
    application:
      - response_time
      - error_rate
      - request_rate
      - queue_size
    business:
      - active_users
      - transaction_rate
      - conversion_rate
```

#### Alerting Rules
```yaml
# Alerting Configuration
alerting:
  rules:
    - name: "High CPU Usage"
      condition: "cpu_usage > 80%"
      duration: "5m"
      severity: "warning"
    - name: "High Memory Usage"
      condition: "memory_usage > 85%"
      duration: "5m"
      severity: "warning"
    - name: "High Error Rate"
      condition: "error_rate > 1%"
      duration: "1m"
      severity: "critical"
  notifications:
    channels:
      - email:
          recipients:
            - "admin@example.com"
            - "oncall@example.com"
      - slack:
          channels:
            - "#alerts"
            - "#critical"
      - pagerduty:
          service_key: "your-service-key"
    routing:
      critical: ["pagerduty", "slack", "email"]
      warning: ["slack", "email"]
      info: ["slack"]
```

### Migration & Upgrade

#### Migration Strategy
```yaml
# Migration Configuration
migration:
  phases:
    - planning:
        - assessment
        - risk_analysis
        - timeline
    - preparation:
        - backup
        - testing
        - documentation
    - execution:
        - data_migration
        - service_migration
        - verification
    - validation:
        - testing
        - monitoring
        - rollback_plan
  rollback:
    triggers:
      - error_rate > 5%
      - response_time > 1s
      - data_inconsistency
    procedures:
      - stop_new_services
      - restore_backup
      - start_old_services
```

#### Upgrade Process
```yaml
# Upgrade Configuration
upgrade:
  strategy: "rolling"
  steps:
    - pre_upgrade:
        - backup
        - health_check
        - dependency_check
    - upgrade:
        - update_packages
        - update_configurations
        - update_dependencies
    - post_upgrade:
        - verification
        - monitoring
        - documentation
  validation:
    - functionality
    - performance
    - security
    - compatibility
```

### Performance Optimization

#### Resource Optimization
```yaml
# Resource Optimization
optimization:
  cpu:
    - process_prioritization
    - load_balancing
    - cache_optimization
  memory:
    - garbage_collection
    - memory_pooling
    - cache_management
  disk:
    - i/o_optimization
    - storage_tiering
    - compression
  network:
    - connection_pooling
    - load_balancing
    - compression
```

#### Performance Monitoring
```yaml
# Performance Monitoring
performance:
  metrics:
    - response_time:
        p50: "<100ms"
        p90: "<200ms"
        p99: "<500ms"
    - throughput:
        requests_per_second: ">1000"
        transactions_per_second: ">100"
    - resource_usage:
        cpu: "<70%"
        memory: "<80%"
        disk: "<70%"
  alerts:
    - high_latency
    - low_throughput
    - resource_exhaustion
```

### Security & Compliance

#### Security Measures
```yaml
# Security Configuration
security:
  authentication:
    - mfa:
        - methods:
            - authenticator_app
            - sms
            - email
        - enforcement:
            - admin_access
            - sensitive_operations
            - remote_access
    - sso:
        - providers:
            - oauth2
            - saml
            - ldap
        - features:
            - session_management
            - token_handling
            - role_mapping
    - oauth:
        - flows:
            - authorization_code
            - client_credentials
            - password
        - security:
            - token_encryption
            - scope_validation
            - rate_limiting
  authorization:
    - rbac:
        - roles:
            - admin
            - developer
            - user
        - permissions:
            - read
            - write
            - execute
        - inheritance:
            - role_hierarchy
            - permission_inheritance
    - abac:
        - attributes:
            - user
            - resource
            - environment
        - policies:
            - access_rules
            - conditions
            - obligations
    - policy_engine:
        - evaluation:
            - real_time
            - cached
            - batch
        - enforcement:
            - allow
            - deny
            - audit
  encryption:
    - at_rest:
        - algorithms:
            - aes_256
            - rsa_4096
        - key_management:
            - rotation
            - backup
            - recovery
    - in_transit:
        - protocols:
            - tls_1.3
            - ssh
        - certificates:
            - management
            - validation
            - revocation
    - key_management:
        - storage:
            - hsm
            - kms
        - lifecycle:
            - generation
            - rotation
            - destruction
  monitoring:
    - audit_logs:
        - events:
            - authentication
            - authorization
            - data_access
        - storage:
            - retention
            - encryption
            - backup
    - security_events:
        - detection:
            - siem
            - ids
            - ips
        - analysis:
            - correlation
            - investigation
            - response
    - anomaly_detection:
        - patterns:
            - behavior
            - traffic
            - access
        - alerts:
            - thresholds
            - notifications
            - escalation
```

#### Compliance Requirements
```yaml
# Compliance Configuration
compliance:
  frameworks:
    - iso27001:
        - controls:
            - access_control
            - cryptography
            - operations_security
        - documentation:
            - policies
            - procedures
            - records
    - gdpr:
        - requirements:
            - data_protection
            - privacy_rights
            - breach_notification
        - documentation:
            - privacy_policy
            - data_processing
            - consent_management
    - hipaa:
        - requirements:
            - data_security
            - privacy_rule
            - breach_notification
        - documentation:
            - security_measures
            - privacy_practices
            - incident_response
    - pci_dss:
        - requirements:
            - network_security
            - data_protection
            - access_control
        - documentation:
            - security_policy
            - procedures
            - evidence
  controls:
    - access_control:
        - authentication:
            - mfa
            - password_policy
            - session_management
        - authorization:
            - rbac
            - least_privilege
            - separation_of_duties
    - data_protection:
        - encryption:
            - at_rest
            - in_transit
            - key_management
        - backup:
            - frequency
            - retention
            - recovery
    - audit_trail:
        - logging:
            - events
            - changes
            - access
        - monitoring:
            - real_time
            - analysis
            - alerts
    - incident_response:
        - detection:
            - monitoring
            - alerts
            - investigation
        - response:
            - containment
            - eradication
            - recovery
  monitoring:
    - compliance_checks:
        - automated:
            - daily
            - weekly
            - monthly
        - manual:
            - quarterly
            - annual
            - ad_hoc
    - audit_reviews:
        - internal:
            - monthly
            - quarterly
            - annual
        - external:
            - annual
            - certification
            - regulatory
    - violation_tracking:
        - detection:
            - automated
            - manual
            - reported
        - remediation:
            - immediate
            - planned
            - preventive
    - remediation_planning:
        - assessment:
            - risk
            - impact
            - priority
        - implementation:
            - timeline
            - resources
            - verification
```

### Incident Response & Troubleshooting

#### Incident Response Plan
```yaml
# Incident Response Configuration
incident_response:
  severity_levels:
    - critical:
        - response_time: "15m"
        - resolution_time: "1h"
        - notification:
            - pagerduty
            - slack
            - email
        - impact:
            - service_outage
            - data_breach
            - security_breach
    - high:
        - response_time: "1h"
        - resolution_time: "4h"
        - notification:
            - slack
            - email
        - impact:
            - degraded_service
            - partial_outage
            - security_incident
    - medium:
        - response_time: "4h"
        - resolution_time: "8h"
        - notification:
            - slack
        - impact:
            - minor_issues
            - performance_degradation
            - security_warning
    - low:
        - response_time: "8h"
        - resolution_time: "24h"
        - notification:
            - email
        - impact:
            - cosmetic_issues
            - minor_bugs
            - documentation_updates
  procedures:
    - detection:
        - monitoring:
            - system_metrics
            - application_logs
            - security_events
        - alerts:
            - automated
            - manual
            - user_reported
        - classification:
            - severity
            - impact
            - scope
    - classification:
        - assessment:
            - impact_analysis
            - scope_determination
            - priority_setting
        - categorization:
            - type
            - severity
            - affected_systems
        - documentation:
            - incident_details
            - initial_findings
            - action_items
    - containment:
        - immediate_actions:
            - service_isolation
            - access_restriction
            - backup_creation
        - communication:
            - stakeholders
            - users
            - management
        - documentation:
            - actions_taken
            - current_state
            - next_steps
    - eradication:
        - root_cause:
            - investigation
            - analysis
            - verification
        - remediation:
            - fixes
            - patches
            - configuration
        - validation:
            - testing
            - verification
            - monitoring
    - recovery:
        - service_restoration:
            - gradual
            - controlled
            - monitored
        - data_restoration:
            - backup_verification
            - data_integrity
            - consistency_check
        - validation:
            - functionality
            - performance
            - security
    - lessons_learned:
        - analysis:
            - timeline
            - actions
            - decisions
        - documentation:
            - incident_report
            - recommendations
            - improvements
        - implementation:
            - preventive_measures
            - process_updates
            - training
```

#### Troubleshooting Guide
```yaml
# Troubleshooting Configuration
troubleshooting:
  tools:
    - logging:
        - elk_stack:
            - elasticsearch:
                - indices
                - mappings
                - queries
            - logstash:
                - inputs
                - filters
                - outputs
            - kibana:
                - dashboards
                - visualizations
                - alerts
    - monitoring:
        - prometheus:
            - metrics
            - alerts
            - rules
        - grafana:
            - dashboards
            - alerts
            - annotations
    - tracing:
        - jaeger:
            - traces
            - spans
            - tags
        - zipkin:
            - traces
            - dependencies
            - latency
    - debugging:
        - debugger:
            - breakpoints
            - variables
            - call_stack
        - profiler:
            - cpu
            - memory
            - i/o
  procedures:
    - problem_identification:
        - symptoms:
            - error_messages
            - behavior_changes
            - performance_issues
        - scope:
            - affected_systems
            - impacted_users
            - business_impact
        - priority:
            - severity
            - urgency
            - resources
    - root_cause_analysis:
        - investigation:
            - logs
            - metrics
            - traces
        - analysis:
            - patterns
            - correlations
            - dependencies
        - verification:
            - testing
            - validation
            - documentation
    - solution_implementation:
        - planning:
            - approach
            - resources
            - timeline
        - execution:
            - changes
            - testing
            - validation
        - monitoring:
            - results
            - impact
            - stability
    - verification:
        - testing:
            - functionality
            - performance
            - security
        - validation:
            - requirements
            - standards
            - compliance
        - documentation:
            - changes
            - procedures
            - lessons
  documentation:
    - known_issues:
        - description:
            - problem
            - impact
            - workaround
        - resolution:
            - steps
            - verification
            - prevention
        - tracking:
            - status
            - updates
            - closure
    - solutions:
        - procedures:
            - steps
            - commands
            - configurations
        - verification:
            - tests
            - checks
            - validation
        - maintenance:
            - updates
            - monitoring
            - prevention
    - workarounds:
        - temporary:
            - steps
            - limitations
            - risks
        - permanent:
            - implementation
            - validation
            - documentation
        - communication:
            - users
            - stakeholders
            - support
```

### Practical Examples & Checklists

#### Module 1: Linux Fundamentals

##### File System Management Examples
```bash
# Example 1: Advanced File System Operations
# Task: Implement a secure file backup system

# 1. Create backup structure
mkdir -p /backup/{daily,weekly,monthly}
chmod 750 /backup
chown root:backup /backup

# 2. Create backup script
cat > /usr/local/bin/backup-system.sh << 'EOF'
#!/bin/bash
# Advanced backup script with encryption and rotation

# Configuration
BACKUP_DIR="/backup"
DATE=$(date +%Y%m%d)
RETENTION_DAYS=7
RETENTION_WEEKS=4
RETENTION_MONTHS=12

# Create encrypted backup
create_backup() {
    local source=$1
    local dest=$2
    tar -czf - "$source" | gpg -e -r backup-key > "$dest"
}

# Rotate backups
rotate_backups() {
    local dir=$1
    local pattern=$2
    local retention=$3
    find "$dir" -name "$pattern" -mtime +$retention -delete
}

# Perform backups
create_backup /etc "/backup/daily/etc-$DATE.tar.gz.gpg"
create_backup /var/www "/backup/daily/www-$DATE.tar.gz.gpg"

# Rotate old backups
rotate_backups "/backup/daily" "*.tar.gz.gpg" $RETENTION_DAYS
rotate_backups "/backup/weekly" "*.tar.gz.gpg" $RETENTION_WEEKS
rotate_backups "/backup/monthly" "*.tar.gz.gpg" $RETENTION_MONTHS
EOF
chmod +x /usr/local/bin/backup-system.sh

# 3. Setup cron job
echo "0 2 * * * /usr/local/bin/backup-system.sh" | sudo tee -a /etc/crontab
```

##### Process Management Examples
```bash
# Example 2: Advanced Process Management
# Task: Create a process monitoring and auto-recovery system

# 1. Create monitoring script
cat > /usr/local/bin/process-monitor.sh << 'EOF'
#!/bin/bash
# Advanced process monitoring with auto-recovery and alerting

# Configuration
SERVICES=("nginx" "mysql" "redis")
ALERT_EMAIL="admin@example.com"
LOG_FILE="/var/log/process-monitor.log"
MAX_RESTARTS=3
COOLDOWN=300  # 5 minutes

# Alert function
send_alert() {
    local service=$1
    local message=$2
    echo "$(date): $message" >> $LOG_FILE
    echo "$message" | mail -s "Service Alert: $service" $ALERT_EMAIL
}

# Monitor service
monitor_service() {
    local service=$1
    local restarts=0
    local last_restart=0

    while true; do
        if ! systemctl is-active --quiet $service; then
            current_time=$(date +%s)
            if [ $((current_time - last_restart)) -gt $COOLDOWN ]; then
                restarts=0
            fi

            if [ $restarts -lt $MAX_RESTARTS ]; then
                systemctl restart $service
                restarts=$((restarts + 1))
                last_restart=$current_time
                send_alert $service "Service $service was down and has been restarted (Attempt $restarts/$MAX_RESTARTS)"
            else
                send_alert $service "Service $service is down and max restart attempts reached"
            fi
        fi
        sleep 60
    done
}

# Start monitoring for each service
for service in "${SERVICES[@]}"; do
    monitor_service $service &
done
EOF
chmod +x /usr/local/bin/process-monitor.sh

# 2. Create systemd service
cat > /etc/systemd/system/process-monitor.service << 'EOF'
[Unit]
Description=Process Monitoring Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/process-monitor.sh
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

# 3. Enable and start service
systemctl daemon-reload
systemctl enable process-monitor
systemctl start process-monitor
```

##### System Administration Examples
```bash
# Example 3: Advanced System Administration
# Task: Implement a secure web server with monitoring

# 1. Install and configure nginx with security
cat > /etc/nginx/conf.d/security.conf << 'EOF'
# Security headers
add_header X-Frame-Options "SAMEORIGIN";
add_header X-XSS-Protection "1; mode=block";
add_header X-Content-Type-Options "nosniff";
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline';";

# SSL configuration
ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers on;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 1d;
ssl_session_tickets off;
ssl_stapling on;
ssl_stapling_verify on;
resolver 8.8.8.8 8.8.4.4 valid=300s;
resolver_timeout 5s;
EOF

# 2. Setup monitoring with Prometheus
cat > /etc/prometheus/prometheus.yml << 'EOF'
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'nginx'
    static_configs:
      - targets: ['localhost:9113']
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
EOF

# 3. Configure log rotation
cat > /etc/logrotate.d/nginx << 'EOF'
/var/log/nginx/*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 www-data adm
    sharedscripts
    postrotate
        [ -f /var/run/nginx.pid ] && kill -USR1 `cat /var/run/nginx.pid`
    endscript
}
EOF

# 4. Setup firewall rules
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw allow 'Nginx Full'
ufw allow 9100/tcp  # Prometheus Node Exporter
ufw allow 9113/tcp  # Nginx Exporter
ufw enable
```

#### Module 2: Version Control

##### Advanced Git Workflow Examples
```bash
# Example 1: Feature Development Workflow
# Task: Implement a new feature with proper Git workflow

# 1. Setup development environment
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global core.editor vim
git config --global init.defaultBranch main

# 2. Create feature branch with proper naming
git checkout -b feature/JIRA-123-user-authentication

# 3. Implement feature with atomic commits
git add src/auth/login.js
git commit -m "feat(auth): Add login form component

- Create login form with email/password fields
- Add form validation
- Implement error handling
- Add loading state"

git add src/auth/api.js
git commit -m "feat(auth): Add authentication API integration

- Implement login API call
- Add token storage
- Handle API errors
- Add refresh token logic"

# 4. Rebase and squash commits
git rebase -i HEAD~2

# 5. Push changes and create pull request
git push origin feature/JIRA-123-user-authentication
gh pr create --title "Add user authentication" --body "
## Description
Implements user authentication feature including login form and API integration.

## Changes
- Add login form component
- Implement authentication API
- Add token management
- Add error handling

## Testing
- [ ] Unit tests added
- [ ] Integration tests added
- [ ] Manual testing completed

## Screenshots
[Add screenshots if applicable]"
```

##### Git Collaboration Examples
```bash
# Example 2: Code Review and Collaboration
# Task: Review and merge a pull request

# 1. Review changes locally
git fetch origin pull/123/head:pr-123
git checkout pr-123

# 2. Run tests and checks
npm run test
npm run lint
npm run build

# 3. Review code
git diff main

# 4. Add review comments
gh pr review 123 --body "
## Code Review

### Positive
- Good code organization
- Clear variable names
- Proper error handling

### Suggestions
- Consider adding more comments
- Add input validation
- Consider using constants for magic numbers

### Questions
- Why was this approach chosen?
- Have you considered edge cases?
- Is there a reason for this implementation?"

# 5. Approve and merge
gh pr review 123 --approve
gh pr merge 123 --squash --delete-branch
```

#### Module 3: Container Basics

##### Advanced Docker Examples
```bash
# Example 1: Multi-stage Docker Build
# Task: Create an optimized production Docker image

# 1. Create Dockerfile
cat > Dockerfile << 'EOF'
# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
EOF

# 2. Create nginx configuration
cat > nginx.conf << 'EOF'
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Content-Type-Options "nosniff";

    # Gzip compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    # Cache control
    location /static/ {
        expires 1y;
        add_header Cache-Control "public, no-transform";
    }

    # Error pages
    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;
}
EOF

# 3. Build and run
docker build -t myapp:prod .
docker run -d -p 8080:80 --name myapp myapp:prod
```

##### Advanced Docker Compose Examples
```bash
# Example 2: Production-ready Docker Compose
# Task: Create a production environment with multiple services

# 1. Create docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - NODE_ENV=production
      - DB_HOST=db
      - REDIS_HOST=redis
    depends_on:
      - db
      - redis
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
    networks:
      - frontend
      - backend

  db:
    image: postgres:13-alpine
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    secrets:
      - db_password
    networks:
      - backend

  redis:
    image: redis:6-alpine
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    networks:
      - backend

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - app
    networks:
      - frontend

networks:
  frontend:
  backend:

volumes:
  postgres_data:
  redis_data:

secrets:
  db_password:
    file: ./secrets/db_password.txt
EOF

# 2. Create nginx configuration
cat > nginx.conf << 'EOF'
upstream app {
    server app:3000;
}

server {
    listen 80;
    server_name example.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com;

    ssl_certificate /etc/nginx/ssl/example.com.crt;
    ssl_certificate_key /etc/nginx/ssl/example.com.key;

    location / {
        proxy_pass http://app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
EOF

# 3. Start services
docker-compose up -d

# 4. Monitor services
docker-compose ps
docker-compose logs -f
```

### Advanced Checklists

#### Production Environment Checklist
```markdown
# Production Environment Checklist

## Infrastructure
- [ ] High availability setup
  - [ ] Load balancer configured
  - [ ] Multiple availability zones
  - [ ] Auto-scaling configured
  - [ ] Failover testing completed

## Security
- [ ] Network security
  - [ ] Firewall rules configured
  - [ ] Security groups set up
  - [ ] VPN access configured
  - [ ] DDoS protection enabled
- [ ] Access control
  - [ ] IAM roles configured
  - [ ] Least privilege principle applied
  - [ ] Access logging enabled
  - [ ] Regular access reviews

## Monitoring
- [ ] System monitoring
  - [ ] CPU/Memory monitoring
  - [ ] Disk space monitoring
  - [ ] Network monitoring
  - [ ] Custom metrics configured
- [ ] Application monitoring
  - [ ] Error tracking
  - [ ] Performance monitoring
  - [ ] User analytics
  - [ ] Business metrics

## Backup & Recovery
- [ ] Backup strategy
  - [ ] Automated backups configured
  - [ ] Backup verification
  - [ ] Retention policy
  - [ ] Off-site storage
- [ ] Disaster recovery
  - [ ] Recovery procedures documented
  - [ ] Recovery testing completed
  - [ ] RTO/RPO defined
  - [ ] Regular DR testing
```

#### Security Implementation Checklist
```markdown
# Security Implementation Checklist

## Application Security
- [ ] Input validation
  - [ ] Form validation
  - [ ] API input validation
  - [ ] File upload validation
  - [ ] SQL injection prevention
- [ ] Authentication
  - [ ] MFA implemented
  - [ ] Password policies
  - [ ] Session management
  - [ ] OAuth/SSO configured
- [ ] Authorization
  - [ ] Role-based access control
  - [ ] Resource-level permissions
  - [ ] API authorization
  - [ ] Regular permission audits

## Infrastructure Security
- [ ] Network security
  - [ ] Firewall configuration
  - [ ] VPN setup
  - [ ] Network segmentation
  - [ ] Intrusion detection
- [ ] System security
  - [ ] OS hardening
  - [ ] Regular updates
  - [ ] Antivirus/malware
  - [ ] File integrity monitoring

## Data Security
- [ ] Encryption
  - [ ] Data at rest
  - [ ] Data in transit
  - [ ] Key management
  - [ ] Certificate management
- [ ] Data protection
  - [ ] Backup encryption
  - [ ] Data classification
  - [ ] Data retention
  - [ ] Data disposal
```

### Advanced Procedures

#### Production Deployment Procedure
```markdown
# Production Deployment Procedure

## Pre-deployment
1. Code Review
   - [ ] All changes reviewed
   - [ ] Security review completed
   - [ ] Performance review completed
   - [ ] Documentation updated

2. Testing
   - [ ] Unit tests passing
   - [ ] Integration tests passing
   - [ ] Performance tests completed
   - [ ] Security tests completed
   - [ ] User acceptance testing

3. Environment Preparation
   - [ ] Backup current version
   - [ ] Update dependencies
   - [ ] Check system resources
   - [ ] Verify configurations
   - [ ] Prepare rollback plan

## Deployment
1. Database Migration
   - [ ] Backup database
   - [ ] Run migrations
   - [ ] Verify data integrity
   - [ ] Update indexes
   - [ ] Test queries

2. Application Deployment
   - [ ] Deploy new version
   - [ ] Update configurations
   - [ ] Start services
   - [ ] Verify health checks
   - [ ] Monitor metrics

3. Post-deployment
   - [ ] Monitor logs
   - [ ] Check metrics
   - [ ] Verify functionality
   - [ ] Update documentation
   - [ ] Notify stakeholders

## Rollback Procedure
1. Identify Issues
   - [ ] Check error logs
   - [ ] Monitor metrics
   - [ ] User reports
   - [ ] System alerts

2. Execute Rollback
   - [ ] Stop new version
   - [ ] Restore backup
   - [ ] Start previous version
   - [ ] Verify functionality
   - [ ] Notify stakeholders

3. Post-rollback
   - [ ] Document issues
   - [ ] Update procedures
   - [ ] Schedule fix
   - [ ] Update monitoring
```

#### Security Audit Procedure
```markdown
# Security Audit Procedure

## Preparation
1. Scope Definition
   - [ ] Identify systems
   - [ ] Define boundaries
   - [ ] Set objectives
   - [ ] Schedule audit
   - [ ] Prepare tools

2. Tool Setup
   - [ ] Install scanners
   - [ ] Configure tools
   - [ ] Update signatures
   - [ ] Test tools
   - [ ] Prepare documentation

## Execution
1. Vulnerability Scan
   - [ ] Run automated scans
   - [ ] Check configurations
   - [ ] Review permissions
   - [ ] Test authentication
   - [ ] Document findings

2. Manual Testing
   - [ ] Penetration testing
   - [ ] Social engineering
   - [ ] Physical security
   - [ ] Access control
   - [ ] Document results

3. Documentation
   - [ ] Record findings
   - [ ] Take screenshots
   - [ ] Document procedures
   - [ ] Note recommendations
   - [ ] Prepare report

## Reporting
1. Analysis
   - [ ] Categorize findings
   - [ ] Assess risks
   - [ ] Prioritize fixes
   - [ ] Plan remediation
   - [ ] Set timelines

2. Report Generation
   - [ ] Executive summary
   - [ ] Technical details
   - [ ] Risk assessment
   - [ ] Recommendations
   - [ ] Action items

3. Follow-up
   - [ ] Track fixes
   - [ ] Verify remediation
   - [ ] Update procedures
   - [ ] Schedule next audit
   - [ ] Update documentation
```

[Previous content remains unchanged...] 
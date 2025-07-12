# Version Control
# Quản lý phiên bản

## Overview / Tổng quan

This module covers essential version control concepts and practices using Git and GitHub. You'll learn how to manage code versions, collaborate with teams, and implement best practices for version control in DevOps environments.

Module này bao gồm các khái niệm và thực hành cơ bản về quản lý phiên bản sử dụng Git và GitHub. Bạn sẽ học cách quản lý phiên bản mã nguồn, cộng tác với nhóm và triển khai các thực hành tốt nhất cho quản lý phiên bản trong môi trường DevOps.

## Learning Objectives / Mục tiêu học tập

### 1. Git Fundamentals / Kiến thức cơ bản về Git
- Version control concepts
- Git workflow
- Branching strategies
- Merge and rebase
- Best practices

*Vietnamese:*
- Khái niệm quản lý phiên bản
- Quy trình làm việc với Git
- Chiến lược phân nhánh
- Merge và rebase
- Thực hành tốt nhất

### 2. GitHub Advanced / GitHub nâng cao
- Repository management
- Pull requests
- Code review
- GitHub Actions
- Best practices

*Vietnamese:*
- Quản lý repository
- Pull requests
- Review code
- GitHub Actions
- Thực hành tốt nhất

## Lab Structure / Cấu trúc Lab

### 1. Git Labs / Lab Git

#### Lab 1: Basic Git Operations / Thao tác Git cơ bản
```bash
# Initialize repository
git init

# Configure user
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Create and switch to branch
git checkout -b feature/new-feature

# Add and commit changes
git add .
git commit -m "Add new feature"

# Push changes
git push origin feature/new-feature
```

#### Lab 2: Branch Management / Quản lý nhánh
```bash
# Create development branch
git checkout -b develop

# Create feature branch
git checkout -b feature/user-authentication

# Merge feature branch
git checkout develop
git merge feature/user-authentication

# Delete feature branch
git branch -d feature/user-authentication
```

### 2. GitHub Labs / Lab GitHub

#### Lab 1: GitHub Workflow / Quy trình GitHub
```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python -m pytest
```

#### Lab 2: Pull Request Template / Mẫu Pull Request
```markdown
# .github/PULL_REQUEST_TEMPLATE.md
## Description
<!-- Describe your changes in detail -->

## Type of change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have added tests
- [ ] Documentation has been updated
```

## Projects / Dự án

### 1. Collaborative Development / Phát triển cộng tác
- Branch strategy implementation
- Code review process
- CI/CD integration
- Documentation

*Vietnamese:*
- Triển khai chiến lược nhánh
- Quy trình review code
- Tích hợp CI/CD
- Tài liệu

### 2. Automated Workflow / Quy trình tự động
- GitHub Actions setup
- Automated testing
- Deployment automation
- Monitoring

*Vietnamese:*
- Thiết lập GitHub Actions
- Kiểm thử tự động
- Tự động hóa triển khai
- Giám sát

## Resources / Tài liệu

### 1. Documentation / Tài liệu
- Git documentation
- GitHub guides
- Best practices
- Tutorials

*Vietnamese:*
- Tài liệu Git
- Hướng dẫn GitHub
- Thực hành tốt nhất
- Hướng dẫn

### 2. Tools / Công cụ
- Git
- GitHub CLI
- Git GUI clients
- IDE integrations

*Vietnamese:*
- Git
- GitHub CLI
- Git GUI clients
- Tích hợp IDE

## Assessment / Đánh giá

### 1. Knowledge Check / Kiểm tra kiến thức
- Version control concepts
- Git commands
- GitHub features
- Best practices

*Vietnamese:*
- Khái niệm quản lý phiên bản
- Lệnh Git
- Tính năng GitHub
- Thực hành tốt nhất

### 2. Practical Exercises / Bài tập thực hành
- Repository setup
- Branch management
- Pull requests
- CI/CD implementation

*Vietnamese:*
- Thiết lập repository
- Quản lý nhánh
- Pull requests
- Triển khai CI/CD

## Certification Preparation / Chuẩn bị chứng chỉ

### 1. Available Certifications / Chứng chỉ có sẵn
- GitHub Certified Developer
- GitLab Certified Associate
- DevOps Institute GitOps Foundation
- AWS Certified DevOps Engineer

*Vietnamese:*
- GitHub Certified Developer
- GitLab Certified Associate
- DevOps Institute GitOps Foundation
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
   - Basic command line knowledge
   - Understanding of software development
   - Familiarity with text editors
   - Team collaboration experience

2. **Setup / Thiết lập**
   ```bash
   # Install Git
   sudo apt-get update
   sudo apt-get install git

   # Install GitHub CLI
   curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   sudo apt update
   sudo apt install gh
   ```

3. **Learning Path / Lộ trình học**
   - Start with Git basics
   - Learn GitHub features
   - Practice with labs
   - Work on projects

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
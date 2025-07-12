# Version Control - Phần 3: GitHub và GitLab

## 1. GitHub
### 1.1. Giới thiệu
- GitHub là gì?
- Các tính năng chính
- Pricing plans
- GitHub Enterprise

### 1.2. Repository Management
```bash
# Tạo repository
# Sử dụng GitHub CLI
gh repo create my-project --public
gh repo create my-project --private

# Fork repository
gh repo fork username/repo

# Clone repository
gh repo clone username/repo
```

### 1.3. Issues và Projects
- Tạo và quản lý issues
- Labels và milestones
- Projects boards
- GitHub Actions

### 1.4. Pull Requests
```bash
# Tạo pull request
gh pr create --title "Feature X" --body "Description"

# Review pull request
gh pr review 123 --approve
gh pr review 123 --request-changes
gh pr review 123 --comment

# Merge pull request
gh pr merge 123 --merge
gh pr merge 123 --squash
gh pr merge 123 --rebase
```

### 1.5. GitHub Actions
```yaml
# Example workflow
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Setup Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'
    - name: Install dependencies
      run: npm install
    - name: Run tests
      run: npm test
    - name: Build
      run: npm run build
```

### 1.6. GitHub Packages
```bash
# Publish package
npm publish --registry=https://npm.pkg.github.com

# Install package
npm install @username/package-name
```

### 1.7. GitHub Security
- Security alerts
- Dependency scanning
- Code scanning
- Secret scanning

## 2. GitLab
### 2.1. Giới thiệu
- GitLab là gì?
- Các tính năng chính
- Pricing plans
- GitLab Self-hosted

### 2.2. Repository Management
```bash
# Tạo project
# Sử dụng GitLab CLI
glab repo create my-project --public
glab repo create my-project --private

# Fork project
glab repo fork username/project

# Clone project
glab repo clone username/project
```

### 2.3. Issues và Projects
- Tạo và quản lý issues
- Labels và milestones
- Project boards
- GitLab CI/CD

### 2.4. Merge Requests
```bash
# Tạo merge request
glab mr create --title "Feature X" --description "Description"

# Review merge request
glab mr review 123 --approve
glab mr review 123 --request-changes
glab mr review 123 --comment

# Merge request
glab mr merge 123
```

### 2.5. GitLab CI/CD
```yaml
# Example pipeline
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - npm install
    - npm run build
  artifacts:
    paths:
      - dist/

test:
  stage: test
  script:
    - npm test

deploy:
  stage: deploy
  script:
    - echo "Deploy to production"
  only:
    - main
```

### 2.6. GitLab Packages
```bash
# Publish package
npm publish --registry=https://gitlab.com/api/v4/projects/1/packages/npm/

# Install package
npm install @scope/package-name
```

### 2.7. GitLab Security
- Security scanning
- Dependency scanning
- Container scanning
- Secret detection

## 3. So sánh GitHub và GitLab
- Tính năng
- Pricing
- Performance
- Community
- Enterprise features

## 4. Best Practices
### 4.1. Repository Management
- Branch protection rules
- Code review requirements
- Automated testing
- Documentation

### 4.2. CI/CD
- Pipeline optimization
- Caching strategies
- Artifact management
- Deployment strategies

### 4.3. Security
- Access control
- Secret management
- Security scanning
- Compliance

## Bài tập thực hành
1. Tạo và quản lý repository
2. Thiết lập CI/CD pipeline
3. Quản lý issues và projects
4. Tạo và review pull/merge requests

## Tài liệu tham khảo
- GitHub Documentation
- GitLab Documentation
- GitHub Actions Documentation
- GitLab CI/CD Documentation 
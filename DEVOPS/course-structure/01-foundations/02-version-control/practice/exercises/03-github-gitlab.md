# Bài tập 3: GitHub và GitLab

## Mục tiêu
- Thực hành sử dụng GitHub và GitLab
- Quản lý repository
- Thiết lập CI/CD pipeline
- Quản lý issues và projects
- Tạo và review pull/merge requests

## Yêu cầu
1. Tạo và quản lý repository:
- Tạo repository trên GitHub và GitLab
- Cấu hình branch protection rules
- Thiết lập webhooks
- Quản lý collaborators

2. Thiết lập CI/CD pipeline:
- GitHub Actions workflow
- GitLab CI/CD pipeline
- Automated testing
- Automated deployment

3. Quản lý issues và projects:
- Tạo và quản lý issues
- Tạo project board
- Sử dụng labels và milestones
- Tạo templates

4. Tạo và review pull/merge requests:
- Tạo feature branch
- Tạo pull/merge request
- Review code
- Merge changes

## Hướng dẫn

### 1. Tạo và quản lý repository
```bash
# Tạo repository trên GitHub
gh repo create devops-practice \
    --public \
    --description "DevOps practice repository" \
    --add-readme \
    --gitignore Node

# Tạo repository trên GitLab
glab repo create devops-practice \
    --public \
    --description "DevOps practice repository" \
    --add-readme \
    --gitignore Node

# Cấu hình branch protection
# GitHub
gh api repos/:owner/:repo/branches/main/protection \
    -X PUT \
    -H "Accept: application/vnd.github.v3+json" \
    -f required_status_checks='{"strict":true,"contexts":["ci"]}' \
    -f enforce_admins=true \
    -f required_pull_request_reviews='{"dismissal_restrictions":{},"dismiss_stale_reviews":true,"require_code_owner_reviews":true}' \
    -f restrictions=null

# GitLab
glab api projects/:id/protected_branches \
    -X POST \
    -F name=main \
    -F push_access_level=0 \
    -F merge_access_level=30

# Thiết lập webhook
# GitHub
gh api repos/:owner/:repo/hooks \
    -X POST \
    -H "Accept: application/vnd.github.v3+json" \
    -f name=web \
    -f config='{"url":"http://example.com/webhook","content_type":"json"}' \
    -f events='["push","pull_request"]' \
    -f active=true

# GitLab
glab api projects/:id/hooks \
    -X POST \
    -F url=http://example.com/webhook \
    -F push_events=true \
    -F merge_requests_events=true
```

### 2. Thiết lập CI/CD pipeline
```yaml
# GitHub Actions (.github/workflows/ci.yml)
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
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

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - uses: actions/checkout@v2
    - name: Deploy to production
      run: echo "Deploy to production"
```

```yaml
# GitLab CI/CD (.gitlab-ci.yml)
stages:
  - test
  - build
  - deploy

test:
  stage: test
  script:
    - npm install
    - npm test
  artifacts:
    paths:
      - node_modules/

build:
  stage: build
  script:
    - npm run build
  artifacts:
    paths:
      - dist/

deploy:
  stage: deploy
  script:
    - echo "Deploy to production"
  only:
    - main
```

### 3. Quản lý issues và projects
```bash
# Tạo issue template
mkdir -p .github/ISSUE_TEMPLATE
cat > .github/ISSUE_TEMPLATE/bug_report.md << EOF
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. iOS]
 - Browser [e.g. chrome, safari]
 - Version [e.g. 22]

**Additional context**
Add any other context about the problem here.
EOF

# Tạo project board
# GitHub
gh api repos/:owner/:repo/projects \
    -X POST \
    -H "Accept: application/vnd.github.v3+json" \
    -f name="DevOps Practice" \
    -f body="Project board for DevOps practice"

# GitLab
glab api projects/:id/boards \
    -X POST \
    -F name="DevOps Practice"
```

### 4. Tạo và review pull/merge requests
```bash
# Tạo feature branch
git checkout -b feature/new-feature

# Tạo pull request
gh pr create \
    --title "Add new feature" \
    --body "This PR adds a new feature" \
    --base main \
    --head feature/new-feature

# Tạo merge request
glab mr create \
    --title "Add new feature" \
    --description "This MR adds a new feature" \
    --source-branch feature/new-feature \
    --target-branch main

# Review pull request
gh pr review 123 \
    --approve \
    --body "LGTM"

# Review merge request
glab mr review 123 \
    --approve \
    --comment "LGTM"
```

## Kiểm tra
1. Kiểm tra repository:
```bash
# GitHub
gh repo view
gh repo view --web

# GitLab
glab repo view
glab repo view --web
```

2. Kiểm tra CI/CD:
```bash
# GitHub
gh run list
gh run view

# GitLab
glab pipeline list
glab pipeline view
```

3. Kiểm tra issues:
```bash
# GitHub
gh issue list
gh issue view

# GitLab
glab issue list
glab issue view
```

4. Kiểm tra pull/merge requests:
```bash
# GitHub
gh pr list
gh pr view

# GitLab
glab mr list
glab mr view
```

## Gợi ý
- Sử dụng `gh help` để xem hướng dẫn GitHub CLI
- Sử dụng `glab help` để xem hướng dẫn GitLab CLI
- Sử dụng web interface để quản lý projects
- Sử dụng templates để chuẩn hóa quy trình

## Tài liệu tham khảo
- GitHub Documentation
- GitLab Documentation
- GitHub Actions Documentation
- GitLab CI/CD Documentation 
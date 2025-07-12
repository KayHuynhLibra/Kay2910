# Bài tập 4: Version Control Tổng hợp

## Mục tiêu
- Thực hành toàn diện các kỹ năng Version Control
- Kết hợp Git, GitHub và GitLab
- Áp dụng các best practices
- Xây dựng quy trình làm việc hiệu quả

## Yêu cầu
1. Thiết lập môi trường phát triển:
- Cấu hình Git
- Thiết lập SSH keys
- Cài đặt GitHub CLI và GitLab CLI
- Cấu hình Git hooks

2. Tạo và quản lý dự án:
- Tạo repository trên GitHub và GitLab
- Thiết lập branch protection
- Cấu hình CI/CD pipeline
- Tạo project board

3. Phát triển tính năng:
- Tạo và quản lý branches
- Sử dụng Git workflow
- Xử lý conflicts
- Code review

4. Quản lý releases:
- Tạo và quản lý tags
- Tạo releases
- Quản lý changelog
- Tự động hóa release process

## Hướng dẫn

### 1. Thiết lập môi trường
```bash
# Cấu hình Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global core.editor "vim"
git config --global init.defaultBranch main

# Tạo SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"
ssh-add ~/.ssh/id_ed25519

# Cài đặt GitHub CLI
# Windows
winget install GitHub.cli

# Cài đặt GitLab CLI
# Windows
winget install GitLab.cli

# Cấu hình Git hooks
mkdir -p .git/hooks
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh
# Check code style
npm run lint

# Run tests
npm test

# Check for sensitive data
if git diff --cached | grep -i "password\|secret\|key"; then
    echo "Error: Sensitive data found in staged files"
    exit 1
fi
EOF

chmod +x .git/hooks/pre-commit
```

### 2. Tạo và quản lý dự án
```bash
# Tạo repository trên GitHub
gh repo create devops-project \
    --public \
    --description "DevOps project with comprehensive version control" \
    --add-readme \
    --gitignore Node

# Tạo repository trên GitLab
glab repo create devops-project \
    --public \
    --description "DevOps project with comprehensive version control" \
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

# Tạo project board
# GitHub
gh api repos/:owner/:repo/projects \
    -X POST \
    -H "Accept: application/vnd.github.v3+json" \
    -f name="DevOps Project" \
    -f body="Project board for DevOps project"

# GitLab
glab api projects/:id/boards \
    -X POST \
    -F name="DevOps Project"
```

### 3. Phát triển tính năng
```bash
# Tạo branch mới
git checkout -b feature/user-management

# Tạo file mới
cat > src/user.js << EOF
class User {
    constructor(id, name, email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }

    validate() {
        if (!this.email.includes('@')) {
            throw new Error('Invalid email');
        }
        return true;
    }
}

module.exports = User;
EOF

# Tạo test
cat > tests/user.test.js << EOF
const assert = require('assert');
const User = require('../src/user');

describe('User', function() {
    it('should validate email', function() {
        const user = new User(1, 'John Doe', 'john@example.com');
        assert.equal(user.validate(), true);
    });

    it('should throw error for invalid email', function() {
        const user = new User(1, 'John Doe', 'invalid-email');
        assert.throws(() => user.validate(), Error);
    });
});
EOF

# Commit changes
git add src/user.js tests/user.test.js
git commit -m "Add user management feature"

# Tạo pull request
gh pr create \
    --title "Add user management feature" \
    --body "This PR adds user management functionality" \
    --base main \
    --head feature/user-management
```

### 4. Quản lý releases
```bash
# Tạo tag
git tag -a v1.0.0 -m "First release"

# Tạo changelog
cat > CHANGELOG.md << EOF
# Changelog

## [1.0.0] - $(date +%Y-%m-%d)

### Added
- User management feature
- Basic authentication
- Unit tests

### Changed
- Updated project structure
- Improved documentation

### Fixed
- Email validation
- Test coverage
EOF

# Tạo release
gh release create v1.0.0 \
    --title "Version 1.0.0" \
    --notes-file CHANGELOG.md \
    --target main

# GitLab
glab release create v1.0.0 \
    --name "Version 1.0.0" \
    --notes-file CHANGELOG.md \
    --tag-name v1.0.0
```

## Kiểm tra
1. Kiểm tra môi trường:
```bash
# Git config
git config --list

# SSH keys
ssh-add -l

# CLI tools
gh --version
glab --version
```

2. Kiểm tra repository:
```bash
# GitHub
gh repo view
gh repo view --web

# GitLab
glab repo view
glab repo view --web
```

3. Kiểm tra CI/CD:
```bash
# GitHub
gh run list
gh run view

# GitLab
glab pipeline list
glab pipeline view
```

4. Kiểm tra releases:
```bash
# GitHub
gh release list
gh release view v1.0.0

# GitLab
glab release list
glab release view v1.0.0
```

## Gợi ý
- Sử dụng Git flow hoặc GitHub flow
- Tự động hóa quy trình với CI/CD
- Sử dụng semantic versioning
- Duy trì changelog
- Code review kỹ lưỡng
- Tự động hóa release process

## Tài liệu tham khảo
- Pro Git Book
- GitHub Documentation
- GitLab Documentation
- Git Flow Documentation
- Semantic Versioning Specification 
# Bài tập 1: Git Basics

## Mục tiêu
- Thực hành các lệnh Git cơ bản
- Quản lý repository
- Làm việc với branches
- Xử lý conflicts

## Yêu cầu
1. Tạo repository mới:
- Tên: `devops-practice`
- Mô tả: "Repository for DevOps practice"
- Public repository
- Thêm README.md
- Thêm .gitignore cho Node.js

2. Tạo cấu trúc thư mục:
```
devops-practice/
├── src/
│   ├── app.js
│   └── config.js
├── tests/
│   └── app.test.js
├── docs/
│   └── README.md
├── .gitignore
└── README.md
```

3. Tạo và quản lý branches:
- Branch `main`: chứa code ổn định
- Branch `develop`: branch phát triển
- Branch `feature/user-auth`: phát triển tính năng xác thực
- Branch `bugfix/login-error`: sửa lỗi đăng nhập

4. Tạo các commits:
- Commit 1: "Initial commit"
- Commit 2: "Add basic project structure"
- Commit 3: "Implement user authentication"
- Commit 4: "Fix login error"

## Hướng dẫn

### 1. Tạo repository
```bash
# Tạo thư mục
mkdir devops-practice
cd devops-practice

# Khởi tạo Git repository
git init

# Tạo .gitignore
cat > .gitignore << EOF
# Dependencies
node_modules/
npm-debug.log
yarn-debug.log
yarn-error.log

# Environment
.env
.env.local
.env.*.local

# Build
dist/
build/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
EOF

# Tạo README.md
cat > README.md << EOF
# DevOps Practice

Repository for DevOps practice exercises.

## Structure
- \`src/\`: Source code
- \`tests/\`: Test files
- \`docs/\`: Documentation

## Setup
\`\`\`bash
npm install
npm test
\`\`\`
EOF
```

### 2. Tạo cấu trúc thư mục
```bash
# Tạo thư mục
mkdir -p src tests docs

# Tạo file app.js
cat > src/app.js << EOF
const config = require('./config');

function main() {
    console.log('Application started');
    console.log('Config:', config);
}

main();
EOF

# Tạo file config.js
cat > src/config.js << EOF
module.exports = {
    appName: 'DevOps Practice',
    version: '1.0.0',
    environment: process.env.NODE_ENV || 'development'
};
EOF

# Tạo file test
cat > tests/app.test.js << EOF
const assert = require('assert');
const config = require('../src/config');

describe('App', function() {
    it('should have correct config', function() {
        assert.equal(config.appName, 'DevOps Practice');
        assert.equal(config.version, '1.0.0');
    });
});
EOF

# Tạo file docs
cat > docs/README.md << EOF
# Documentation

## API Reference
- GET /api/users
- POST /api/users
- GET /api/users/:id
- PUT /api/users/:id
- DELETE /api/users/:id

## Authentication
- POST /api/auth/login
- POST /api/auth/logout
- GET /api/auth/me
EOF
```

### 3. Tạo và quản lý branches
```bash
# Tạo branch develop
git checkout -b develop

# Tạo branch feature
git checkout -b feature/user-auth

# Tạo branch bugfix
git checkout -b bugfix/login-error
```

### 4. Tạo commits
```bash
# Commit 1: Initial commit
git add .
git commit -m "Initial commit"

# Commit 2: Add basic project structure
git add src/ tests/ docs/
git commit -m "Add basic project structure"

# Commit 3: Implement user authentication
cat > src/auth.js << EOF
function login(username, password) {
    // TODO: Implement login
    return true;
}

function logout() {
    // TODO: Implement logout
    return true;
}

module.exports = {
    login,
    logout
};
EOF

git add src/auth.js
git commit -m "Implement user authentication"

# Commit 4: Fix login error
cat > src/auth.js << EOF
function login(username, password) {
    if (!username || !password) {
        throw new Error('Username and password are required');
    }
    // TODO: Implement login
    return true;
}

function logout() {
    // TODO: Implement logout
    return true;
}

module.exports = {
    login,
    logout
};
EOF

git add src/auth.js
git commit -m "Fix login error"
```

## Kiểm tra
1. Kiểm tra repository:
```bash
git status
git log --oneline --graph --all
```

2. Kiểm tra branches:
```bash
git branch -a
```

3. Kiểm tra cấu trúc thư mục:
```bash
tree
```

4. Kiểm tra nội dung file:
```bash
cat src/app.js
cat src/config.js
cat tests/app.test.js
```

## Gợi ý
- Sử dụng `git status` để kiểm tra trạng thái
- Sử dụng `git log` để xem lịch sử
- Sử dụng `git branch` để quản lý branches
- Sử dụng `git checkout` để chuyển branch
- Sử dụng `git merge` để merge branches

## Tài liệu tham khảo
- Pro Git Book
- Git Documentation
- GitHub Guides 
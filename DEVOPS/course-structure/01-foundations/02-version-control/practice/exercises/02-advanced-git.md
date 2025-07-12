# Bài tập 2: Advanced Git

## Mục tiêu
- Thực hành các tính năng nâng cao của Git
- Sử dụng Git hooks
- Quản lý submodules
- Debug với Git bisect
- Tối ưu hóa repository

## Yêu cầu
1. Thiết lập Git hooks:
- Pre-commit hook: Kiểm tra code style
- Pre-push hook: Chạy tests
- Post-commit hook: Tạo documentation

2. Quản lý submodules:
- Thêm submodule cho shared library
- Cập nhật submodule
- Xử lý conflicts

3. Debug với Git bisect:
- Tìm commit gây ra bug
- Sửa bug
- Tạo test case

4. Tối ưu hóa repository:
- Clean up repository
- Compress repository
- Verify repository

## Hướng dẫn

### 1. Thiết lập Git hooks
```bash
# Tạo thư mục hooks
mkdir -p .git/hooks

# Tạo pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/sh

# Check code style
echo "Running ESLint..."
npm run lint

# Check if linting passed
if [ $? -ne 0 ]; then
    echo "Linting failed. Please fix the issues before committing."
    exit 1
fi

# Check for console.log statements
if git diff --cached | grep -i "console.log"; then
    echo "Error: console.log statements found in staged files"
    exit 1
fi
EOF

# Tạo pre-push hook
cat > .git/hooks/pre-push << 'EOF'
#!/bin/sh

# Run tests
echo "Running tests..."
npm test

# Check if tests passed
if [ $? -ne 0 ]; then
    echo "Tests failed. Please fix the issues before pushing."
    exit 1
fi
EOF

# Tạo post-commit hook
cat > .git/hooks/post-commit << 'EOF'
#!/bin/sh

# Generate documentation
echo "Generating documentation..."
npm run docs

# Commit documentation if changed
if git diff --quiet docs/; then
    echo "No documentation changes"
else
    git add docs/
    git commit -m "Update documentation [skip ci]"
fi
EOF

# Cấp quyền thực thi
chmod +x .git/hooks/*
```

### 2. Quản lý submodules
```bash
# Thêm submodule
git submodule add https://github.com/username/shared-lib.git lib/shared

# Cập nhật submodule
git submodule update --init --recursive
git submodule update --remote

# Tạo file sử dụng submodule
cat > src/shared.js << EOF
const shared = require('../lib/shared');

function useSharedFunction() {
    return shared.doSomething();
}

module.exports = {
    useSharedFunction
};
EOF

# Commit changes
git add src/shared.js
git commit -m "Add shared library integration"
```

### 3. Debug với Git bisect
```bash
# Tạo test case
cat > tests/bug.test.js << EOF
const assert = require('assert');
const app = require('../src/app');

describe('Bug Test', function() {
    it('should not throw error', function() {
        assert.doesNotThrow(() => {
            app.processData();
        });
    });
});
EOF

# Start bisect
git bisect start
git bisect bad
git bisect good v1.0.0

# Run bisect
git bisect run npm test

# Fix bug
cat > src/app.js << EOF
function processData() {
    try {
        // Process data
        return true;
    } catch (error) {
        console.error('Error processing data:', error);
        return false;
    }
}

module.exports = {
    processData
};
EOF

# Commit fix
git add src/app.js
git commit -m "Fix data processing bug"
```

### 4. Tối ưu hóa repository
```bash
# Clean up
git gc
git prune
git fsck

# Compress repository
git repack -a -d --depth=250 --window=250

# Verify repository
git fsck --full
git count-objects -v
```

## Kiểm tra
1. Kiểm tra hooks:
```bash
# Test pre-commit
git add .
git commit -m "Test commit"

# Test pre-push
git push origin main

# Test post-commit
git log -1
```

2. Kiểm tra submodules:
```bash
git submodule status
ls -la lib/shared
```

3. Kiểm tra bisect:
```bash
git bisect log
git log --oneline -n 5
```

4. Kiểm tra repository:
```bash
git count-objects -v
du -sh .git
```

## Gợi ý
- Sử dụng `git help` để xem hướng dẫn
- Sử dụng `git submodule help` để xem hướng dẫn submodule
- Sử dụng `git bisect help` để xem hướng dẫn bisect
- Sử dụng `git gc --help` để xem hướng dẫn tối ưu hóa

## Tài liệu tham khảo
- Pro Git Book
- Git Documentation
- Git Hooks Documentation
- Git Submodules Documentation 
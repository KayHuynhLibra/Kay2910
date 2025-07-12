# Version Control - Phần 1: Git Basics

## 1. Giới thiệu về Version Control
- Version Control là gì?
- Lợi ích của Version Control
- Các loại Version Control Systems
- Git vs các hệ thống khác

## 2. Cài đặt và Cấu hình Git
```bash
# Cài đặt Git
sudo apt update
sudo apt install git

# Cấu hình Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global core.editor "vim"
git config --list
```

## 3. Khởi tạo Repository
```bash
# Tạo repository mới
git init my-project
cd my-project

# Clone repository từ remote
git clone https://github.com/username/repo.git
git clone -b branch_name https://github.com/username/repo.git
```

## 4. Các lệnh cơ bản
```bash
# Kiểm tra trạng thái
git status

# Thêm file vào staging area
git add file.txt
git add .
git add -p

# Commit changes
git commit -m "Initial commit"
git commit -am "Update with message"

# Xem lịch sử
git log
git log --oneline
git log --graph --oneline --all
```

## 5. Làm việc với Branches
```bash
# Tạo và chuyển branch
git branch feature-branch
git checkout feature-branch
git checkout -b feature-branch

# Liệt kê branches
git branch
git branch -a

# Merge branch
git checkout main
git merge feature-branch

# Xóa branch
git branch -d feature-branch
git branch -D feature-branch
```

## 6. Remote Repository
```bash
# Thêm remote
git remote add origin https://github.com/username/repo.git
git remote -v

# Push changes
git push origin main
git push -u origin main

# Pull changes
git pull origin main
git fetch origin
git merge origin/main
```

## 7. Stashing và Reset
```bash
# Stash changes
git stash
git stash list
git stash pop
git stash apply

# Reset changes
git reset HEAD file.txt
git reset --hard HEAD
git reset --soft HEAD~1
```

## 8. Tags và Releases
```bash
# Tạo tag
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"

# Push tags
git push origin v1.0.0
git push origin --tags

# Xóa tag
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0
```

## 9. Git Workflow
- Centralized Workflow
- Feature Branch Workflow
- Gitflow Workflow
- Forking Workflow

## 10. Best Practices
- Commit messages rõ ràng
- Branch naming conventions
- Regular commits
- Code review process
- Documentation
- .gitignore file

## Bài tập thực hành
1. Tạo repository mới
2. Tạo và merge branches
3. Làm việc với remote repository
4. Tạo và quản lý tags

## Tài liệu tham khảo
- Pro Git Book
- Git Documentation
- GitHub Guides 
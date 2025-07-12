#!/bin/bash

# Bài tập 1: File System Operations
# Mục tiêu: Thực hành các lệnh cơ bản về file system

echo "=== Bài tập File System ==="

# 1. Tạo cấu trúc thư mục
echo "1. Tạo cấu trúc thư mục..."
mkdir -p ~/devops-practice/{bin,etc,var/{log,www},tmp}

# 2. Tạo và quản lý file
echo "2. Tạo và quản lý file..."
echo "Creating test files..."
touch ~/devops-practice/var/log/app.log
echo "Test log entry $(date)" > ~/devops-practice/var/log/app.log
echo "Another log entry" >> ~/devops-practice/var/log/app.log

# 3. Quản lý permissions
echo "3. Quản lý permissions..."
chmod 644 ~/devops-practice/var/log/app.log
chmod 755 ~/devops-practice/bin
chmod 750 ~/devops-practice/etc

# 4. Kiểm tra kết quả
echo "4. Kiểm tra kết quả..."
echo "Directory structure:"
tree ~/devops-practice

echo "File permissions:"
ls -l ~/devops-practice/var/log/app.log
ls -ld ~/devops-practice/{bin,etc}

echo "File content:"
cat ~/devops-practice/var/log/app.log

# 5. Dọn dẹp
echo "5. Dọn dẹp..."
read -p "Bạn có muốn xóa thư mục practice? (y/n) " answer
if [ "$answer" = "y" ]; then
    rm -rf ~/devops-practice
    echo "Đã xóa thư mục practice"
else
    echo "Giữ lại thư mục practice"
fi

echo "=== Hoàn thành bài tập ===" 
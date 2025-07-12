#!/bin/bash

# Lab 1: Basic File Operations
# Mục tiêu: Thực hành các lệnh cơ bản để làm việc với file và thư mục
# Objective: Practice basic commands for working with files and directories

echo "=== Lab 1: Basic File Operations ==="

# Create lab directory structure
# Tạo cấu trúc thư mục cho lab
LAB_DIR=~/linux-lab
mkdir -p $LAB_DIR/{files,docs,backup}

# 1. File Creation and Navigation
# 1. Tạo và điều hướng file
echo "1. Creating and navigating files..."
cd $LAB_DIR

# Create sample files
# Tạo các file mẫu
echo "Hello World" > files/hello.txt
echo "This is a test file" > files/test.txt
echo "Sample content" > docs/notes.txt

# List files and directories
# Liệt kê file và thư mục
echo "Listing files in current directory:"
ls -la

# 2. File Operations
# 2. Thao tác với file
echo "2. Performing file operations..."

# Copy files
# Sao chép file
cp files/hello.txt backup/
cp files/test.txt backup/

# Move files
# Di chuyển file
mv docs/notes.txt files/

# Create symbolic link
# Tạo liên kết tượng trưng
ln -s files/hello.txt docs/hello_link.txt

# 3. File Permissions
# 3. Phân quyền file
echo "3. Managing file permissions..."

# Change file permissions
# Thay đổi quyền file
chmod 644 files/hello.txt
chmod 755 files/test.txt

# Change file ownership
# Thay đổi chủ sở hữu file
sudo chown $USER:$USER files/*

# 4. File Content Operations
# 4. Thao tác với nội dung file
echo "4. Working with file content..."

# View file content
# Xem nội dung file
echo "Content of hello.txt:"
cat files/hello.txt

# Append content
# Thêm nội dung
echo "Additional content" >> files/hello.txt

# Search in files
# Tìm kiếm trong file
echo "Searching for 'test' in files:"
grep -r "test" $LAB_DIR

# 5. Cleanup
# 5. Dọn dẹp
echo "5. Cleaning up..."

# Create backup
# Tạo bản sao lưu
tar -czf $LAB_DIR/backup.tar.gz $LAB_DIR/files

# Remove test files
# Xóa file test
rm -f files/test.txt

echo "=== Lab completed ==="
echo "Check the following locations:"
echo "- Lab directory: $LAB_DIR"
echo "- Backup files: $LAB_DIR/backup"
echo "- Backup archive: $LAB_DIR/backup.tar.gz" 
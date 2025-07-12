#!/bin/bash

# Bài tập 1: Các lệnh cơ bản
# Tác giả: DevOps Team
# Ngày: 2024-03-15

# Tạo cấu trúc thư mục
echo "1. Tạo cấu trúc thư mục..."
mkdir -p ~/devops-practice/{bin,etc,var/{log,www},tmp}

# Tạo file config
echo "2. Tạo file config..."
cat > ~/devops-practice/etc/config.txt << EOF
# Configuration file
APP_NAME=MyApp
DEBUG=true
PORT=8080
EOF

# Tạo file log
echo "3. Tạo file log..."
cat > ~/devops-practice/var/log/app.log << EOF
[2024-03-15 10:00:00] INFO: Application started
[2024-03-15 10:01:00] INFO: User logged in
[2024-03-15 10:02:00] ERROR: Database connection failed
EOF

# Tạo nhóm
echo "4. Tạo nhóm..."
sudo groupadd devops-group

# Tạo người dùng
echo "5. Tạo người dùng..."
sudo useradd -m -s /bin/bash -g devops-group devops-user

# Cấu hình quyền truy cập
echo "6. Cấu hình quyền truy cập..."

# Thư mục devops-practice
chmod 755 ~/devops-practice

# File config.txt
chmod 644 ~/devops-practice/etc/config.txt

# File app.log
chmod 640 ~/devops-practice/var/log/app.log

# Thư mục bin
chmod 750 ~/devops-practice/bin

# Thư mục tmp
chmod 1777 ~/devops-practice/tmp

# Kiểm tra kết quả
echo "7. Kiểm tra kết quả..."
echo "Cấu trúc thư mục:"
tree ~/devops-practice

echo "Nội dung file config:"
cat ~/devops-practice/etc/config.txt

echo "Nội dung file log:"
cat ~/devops-practice/var/log/app.log

echo "Thông tin người dùng:"
id devops-user

echo "Quyền truy cập:"
ls -l ~/devops-practice
ls -l ~/devops-practice/etc/config.txt
ls -l ~/devops-practice/var/log/app.log

echo "Hoàn thành!" 
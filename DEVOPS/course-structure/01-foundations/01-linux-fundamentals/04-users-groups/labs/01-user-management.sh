#!/bin/bash

# Lab 1: User and Group Management
# Mục tiêu: Thực hành quản lý người dùng và nhóm trong Linux
# Objective: Practice user and group management in Linux

echo "=== Lab 1: User and Group Management ==="

# 1. User Information
# 1. Thông tin người dùng
echo "1. Getting user information..."

# List all users
# Liệt kê tất cả người dùng
echo "All users:"
cat /etc/passwd

# List current user
# Liệt kê người dùng hiện tại
echo "Current user:"
whoami
id

# 2. User Management
# 2. Quản lý người dùng
echo "2. Managing users..."

# Create test user
# Tạo người dùng test
TEST_USER="testuser"
echo "Creating test user: $TEST_USER"
sudo useradd -m -s /bin/bash $TEST_USER

# Set password
# Đặt mật khẩu
echo "Setting password for $TEST_USER"
echo "$TEST_USER:password" | sudo chpasswd

# 3. Group Management
# 3. Quản lý nhóm
echo "3. Managing groups..."

# Create test group
# Tạo nhóm test
TEST_GROUP="testgroup"
echo "Creating test group: $TEST_GROUP"
sudo groupadd $TEST_GROUP

# Add user to group
# Thêm người dùng vào nhóm
echo "Adding $TEST_USER to $TEST_GROUP"
sudo usermod -aG $TEST_GROUP $TEST_USER

# 4. File Permissions
# 4. Phân quyền file
echo "4. Managing file permissions..."

# Create test directory
# Tạo thư mục test
TEST_DIR="/tmp/test_dir"
echo "Creating test directory: $TEST_DIR"
sudo mkdir -p $TEST_DIR

# Set ownership
# Đặt quyền sở hữu
echo "Setting ownership of $TEST_DIR"
sudo chown $TEST_USER:$TEST_GROUP $TEST_DIR

# Set permissions
# Đặt quyền
echo "Setting permissions for $TEST_DIR"
sudo chmod 770 $TEST_DIR

# 5. User Environment
# 5. Môi trường người dùng
echo "5. Managing user environment..."

# Create user profile
# Tạo profile người dùng
echo "Creating user profile"
sudo bash -c "echo 'export PATH=\$PATH:/usr/local/bin' >> /home/$TEST_USER/.bashrc"
sudo bash -c "echo 'alias ll=\"ls -la\"' >> /home/$TEST_USER/.bashrc"

# 6. User Limits
# 6. Giới hạn người dùng
echo "6. Setting user limits..."

# Set user limits
# Đặt giới hạn người dùng
echo "Setting limits for $TEST_USER"
sudo bash -c "echo '$TEST_USER soft nofile 1024' >> /etc/security/limits.conf"
sudo bash -c "echo '$TEST_USER hard nofile 2048' >> /etc/security/limits.conf"

# 7. Verification
# 7. Xác minh
echo "7. Verifying setup..."

# Check user
# Kiểm tra người dùng
echo "Checking user:"
id $TEST_USER

# Check group
# Kiểm tra nhóm
echo "Checking group:"
getent group $TEST_GROUP

# Check directory
# Kiểm tra thư mục
echo "Checking directory:"
ls -ld $TEST_DIR

# 8. Cleanup
# 8. Dọn dẹp
echo "8. Cleaning up..."

# Remove test user and group
# Xóa người dùng và nhóm test
echo "Removing test user and group"
sudo userdel -r $TEST_USER
sudo groupdel $TEST_GROUP
sudo rm -rf $TEST_DIR

echo "=== Lab completed ==="
echo "You have learned:"
echo "- User and group creation"
echo "- File permissions and ownership"
echo "- User environment configuration"
echo "- System limits and security" 
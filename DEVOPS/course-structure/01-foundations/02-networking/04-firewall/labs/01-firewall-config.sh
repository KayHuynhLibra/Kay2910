#!/bin/bash

# Lab 1: Firewall Configuration
# Mục tiêu: Thực hành cấu hình tường lửa trong Linux
# Objective: Practice firewall configuration in Linux

echo "=== Lab 1: Firewall Configuration ==="

# 1. Firewall Status
# 1. Trạng thái tường lửa
echo "1. Checking firewall status..."

# Check UFW status
# Kiểm tra trạng thái UFW
echo "UFW status:"
sudo ufw status verbose

# 2. Basic Firewall Rules
# 2. Quy tắc tường lửa cơ bản
echo "2. Configuring basic firewall rules..."

# Allow SSH
# Cho phép SSH
echo "Allowing SSH..."
sudo ufw allow 22/tcp

# Allow HTTP
# Cho phép HTTP
echo "Allowing HTTP..."
sudo ufw allow 80/tcp

# Allow HTTPS
# Cho phép HTTPS
echo "Allowing HTTPS..."
sudo ufw allow 443/tcp

# 3. Advanced Firewall Rules
# 3. Quy tắc tường lửa nâng cao
echo "3. Configuring advanced firewall rules..."

# Allow specific IP
# Cho phép IP cụ thể
echo "Allowing specific IP..."
sudo ufw allow from 192.168.1.100 to any port 22

# Allow specific network
# Cho phép mạng cụ thể
echo "Allowing specific network..."
sudo ufw allow from 192.168.1.0/24 to any port 80

# 4. Firewall Logging
# 4. Ghi log tường lửa
echo "4. Configuring firewall logging..."

# Enable logging
# Bật ghi log
echo "Enabling firewall logging..."
sudo ufw logging on

# Check log file
# Kiểm tra file log
echo "Checking firewall logs:"
sudo tail -f /var/log/ufw.log

# 5. Firewall Rules Management
# 5. Quản lý quy tắc tường lửa
echo "5. Managing firewall rules..."

# List rules
# Liệt kê quy tắc
echo "Listing firewall rules:"
sudo ufw status numbered

# Delete rule
# Xóa quy tắc
echo "Deleting a rule..."
sudo ufw delete 1

# 6. Firewall Testing
# 6. Kiểm tra tường lửa
echo "6. Testing firewall configuration..."

# Test SSH access
# Kiểm tra truy cập SSH
echo "Testing SSH access:"
nc -zv localhost 22

# Test HTTP access
# Kiểm tra truy cập HTTP
echo "Testing HTTP access:"
nc -zv localhost 80

# 7. Firewall Security
# 7. Bảo mật tường lửa
echo "7. Firewall security..."

# Set default policies
# Đặt chính sách mặc định
echo "Setting default policies..."
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Enable firewall
# Bật tường lửa
echo "Enabling firewall..."
sudo ufw enable

# 8. Firewall Monitoring
# 8. Giám sát tường lửa
echo "8. Monitoring firewall..."

# Monitor connections
# Giám sát kết nối
echo "Monitoring connections:"
sudo watch -n 1 'netstat -tuln'

# Check blocked connections
# Kiểm tra kết nối bị chặn
echo "Checking blocked connections:"
sudo grep "UFW BLOCK" /var/log/ufw.log

echo "=== Lab completed ==="
echo "You have learned:"
echo "- Basic firewall configuration"
echo "- Advanced firewall rules"
echo "- Firewall logging"
echo "- Rule management"
echo "- Firewall testing"
echo "- Security best practices"
echo "- Firewall monitoring" 
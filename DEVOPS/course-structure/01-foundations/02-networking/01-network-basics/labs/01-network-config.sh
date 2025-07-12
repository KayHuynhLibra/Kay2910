#!/bin/bash

# Lab 1: Basic Network Configuration
# Mục tiêu: Thực hành cấu hình mạng cơ bản trong Linux
# Objective: Practice basic network configuration in Linux

echo "=== Lab 1: Basic Network Configuration ==="

# 1. Network Interface Information
# 1. Thông tin giao diện mạng
echo "1. Getting network interface information..."

# List network interfaces
# Liệt kê các giao diện mạng
echo "Network interfaces:"
ip addr show

# Show routing table
# Hiển thị bảng định tuyến
echo "Routing table:"
ip route show

# 2. Network Configuration
# 2. Cấu hình mạng
echo "2. Configuring network..."

# Get current interface
# Lấy giao diện hiện tại
INTERFACE=$(ip route | grep default | awk '{print $5}')
echo "Current interface: $INTERFACE"

# Show current IP configuration
# Hiển thị cấu hình IP hiện tại
echo "Current IP configuration:"
ip addr show $INTERFACE

# 3. Network Testing
# 3. Kiểm tra mạng
echo "3. Testing network connectivity..."

# Test local connectivity
# Kiểm tra kết nối cục bộ
echo "Testing local connectivity:"
ping -c 4 127.0.0.1

# Test DNS resolution
# Kiểm tra phân giải DNS
echo "Testing DNS resolution:"
nslookup google.com

# Test internet connectivity
# Kiểm tra kết nối internet
echo "Testing internet connectivity:"
ping -c 4 8.8.8.8

# 4. Network Services
# 4. Dịch vụ mạng
echo "4. Checking network services..."

# Check listening ports
# Kiểm tra các cổng đang lắng nghe
echo "Listening ports:"
netstat -tuln

# Check active connections
# Kiểm tra các kết nối đang hoạt động
echo "Active connections:"
netstat -tun

# 5. Network Troubleshooting
# 5. Xử lý sự cố mạng
echo "5. Network troubleshooting..."

# Trace route
# Theo dõi đường đi
echo "Tracing route to google.com:"
traceroute google.com

# Check DNS servers
# Kiểm tra máy chủ DNS
echo "DNS servers:"
cat /etc/resolv.conf

# 6. Network Security
# 6. Bảo mật mạng
echo "6. Basic network security..."

# Check firewall status
# Kiểm tra trạng thái tường lửa
echo "Firewall status:"
sudo ufw status

# Check open ports
# Kiểm tra các cổng mở
echo "Open ports:"
sudo nmap localhost

# 7. Network Monitoring
# 7. Giám sát mạng
echo "7. Network monitoring..."

# Monitor network traffic
# Giám sát lưu lượng mạng
echo "Network traffic (press Ctrl+C to stop):"
sudo tcpdump -i $INTERFACE -c 10

# Check network statistics
# Kiểm tra thống kê mạng
echo "Network statistics:"
netstat -s

echo "=== Lab completed ==="
echo "You have learned:"
echo "- Network interface configuration"
echo "- Network connectivity testing"
echo "- Network service management"
echo "- Basic network troubleshooting"
echo "- Network security basics"
echo "- Network monitoring" 
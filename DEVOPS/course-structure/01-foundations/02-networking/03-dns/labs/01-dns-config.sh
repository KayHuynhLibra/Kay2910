#!/bin/bash

# Lab 1: DNS Configuration
# Mục tiêu: Thực hành cấu hình DNS trong Linux
# Objective: Practice DNS configuration in Linux

echo "=== Lab 1: DNS Configuration ==="

# 1. DNS Information
# 1. Thông tin DNS
echo "1. Getting DNS information..."

# Check current DNS servers
# Kiểm tra máy chủ DNS hiện tại
echo "Current DNS servers:"
cat /etc/resolv.conf

# Check DNS resolution
# Kiểm tra phân giải DNS
echo "Testing DNS resolution:"
nslookup google.com

# 2. DNS Configuration
# 2. Cấu hình DNS
echo "2. Configuring DNS..."

# Create DNS configuration
# Tạo cấu hình DNS
echo "Creating DNS configuration..."
sudo bash -c 'cat > /etc/resolv.conf << EOF
nameserver 8.8.8.8
nameserver 8.8.4.4
search localdomain
EOF'

# 3. DNS Testing
# 3. Kiểm tra DNS
echo "3. Testing DNS configuration..."

# Test DNS resolution
# Kiểm tra phân giải DNS
echo "Testing DNS resolution:"
dig google.com

# Test reverse DNS
# Kiểm tra DNS ngược
echo "Testing reverse DNS:"
dig -x 8.8.8.8

# 4. DNS Records
# 4. Bản ghi DNS
echo "4. Working with DNS records..."

# Query A record
# Truy vấn bản ghi A
echo "Querying A record:"
dig A google.com

# Query MX record
# Truy vấn bản ghi MX
echo "Querying MX record:"
dig MX google.com

# Query NS record
# Truy vấn bản ghi NS
echo "Querying NS record:"
dig NS google.com

# 5. DNS Caching
# 5. Bộ nhớ đệm DNS
echo "5. DNS caching..."

# Check DNS cache
# Kiểm tra bộ nhớ đệm DNS
echo "Checking DNS cache:"
systemd-resolve --statistics

# Flush DNS cache
# Xóa bộ nhớ đệm DNS
echo "Flushing DNS cache:"
sudo systemd-resolve --flush-caches

# 6. DNS Security
# 6. Bảo mật DNS
echo "6. DNS security..."

# Test DNSSEC
# Kiểm tra DNSSEC
echo "Testing DNSSEC:"
dig +dnssec google.com

# Check DNS over TLS
# Kiểm tra DNS qua TLS
echo "Checking DNS over TLS:"
dig @8.8.8.8 google.com +tls

# 7. DNS Monitoring
# 7. Giám sát DNS
echo "7. DNS monitoring..."

# Monitor DNS queries
# Giám sát truy vấn DNS
echo "Monitoring DNS queries:"
sudo tcpdump -i any port 53

# Check DNS performance
# Kiểm tra hiệu suất DNS
echo "Checking DNS performance:"
dig +stats google.com

# 8. DNS Troubleshooting
# 8. Xử lý sự cố DNS
echo "8. DNS troubleshooting..."

# Check DNS propagation
# Kiểm tra lan truyền DNS
echo "Checking DNS propagation:"
dig +trace google.com

# Test DNS timeout
# Kiểm tra timeout DNS
echo "Testing DNS timeout:"
time dig @8.8.8.8 google.com

echo "=== Lab completed ==="
echo "You have learned:"
echo "- DNS server configuration"
echo "- DNS record types"
echo "- DNS caching"
echo "- DNS security"
echo "- DNS monitoring"
echo "- DNS troubleshooting"
echo "- DNS performance testing" 
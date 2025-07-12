#!/bin/bash

# Bài tập 3: Networking
# Mục tiêu: Thực hành các lệnh networking cơ bản

echo "=== Bài tập Networking ==="

# 1. Network Interface Information
echo "1. Network Interface Information..."
echo "IP Addresses:"
ip addr show

echo "Network Interfaces:"
ifconfig

# 2. Network Connectivity
echo "2. Network Connectivity..."
echo "Testing connectivity to Google..."
ping -c 4 google.com

echo "Tracing route to Google..."
traceroute google.com

# 3. DNS Resolution
echo "3. DNS Resolution..."
echo "DNS lookup for google.com:"
dig google.com

echo "Reverse DNS lookup:"
dig -x 8.8.8.8

# 4. Port Scanning
echo "4. Port Scanning..."
echo "Checking common ports on localhost:"
for port in 22 80 443 3306 5432; do
    nc -zv localhost $port 2>&1 | grep "open" || echo "Port $port is closed"
done

# 5. Network Statistics
echo "5. Network Statistics..."
echo "Active connections:"
netstat -tuln

echo "Listening ports:"
ss -tuln

# 6. Network Configuration
echo "6. Network Configuration..."
echo "Current routing table:"
ip route show

echo "DNS configuration:"
cat /etc/resolv.conf

# 7. Network Troubleshooting
echo "7. Network Troubleshooting..."
echo "Checking network connectivity..."
ping -c 1 8.8.8.8 >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "Internet connectivity: OK"
else
    echo "Internet connectivity: Failed"
fi

echo "Checking DNS resolution..."
host google.com >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "DNS resolution: OK"
else
    echo "DNS resolution: Failed"
fi

echo "=== Hoàn thành bài tập ===" 
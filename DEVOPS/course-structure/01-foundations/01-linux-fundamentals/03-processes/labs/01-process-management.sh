#!/bin/bash

# Lab 1: Process Management
# Mục tiêu: Thực hành quản lý tiến trình trong Linux
# Objective: Practice process management in Linux

echo "=== Lab 1: Process Management ==="

# 1. Process Information
# 1. Thông tin tiến trình
echo "1. Getting process information..."

# List all processes
# Liệt kê tất cả tiến trình
echo "All processes:"
ps aux

# List processes for current user
# Liệt kê tiến trình của người dùng hiện tại
echo "Current user processes:"
ps -u $USER

# 2. Process Control
# 2. Điều khiển tiến trình
echo "2. Controlling processes..."

# Start a background process
# Khởi động tiến trình nền
sleep 100 &
SLEEP_PID=$!

# Show process details
# Hiển thị chi tiết tiến trình
echo "Sleep process details:"
ps -p $SLEEP_PID -o pid,ppid,cmd,%cpu,%mem

# 3. Process Monitoring
# 3. Giám sát tiến trình
echo "3. Monitoring processes..."

# Monitor CPU usage
# Giám sát sử dụng CPU
echo "Top CPU consuming processes:"
ps aux --sort=-%cpu | head -n 5

# Monitor memory usage
# Giám sát sử dụng bộ nhớ
echo "Top memory consuming processes:"
ps aux --sort=-%mem | head -n 5

# 4. Process Signals
# 4. Tín hiệu tiến trình
echo "4. Working with process signals..."

# Send SIGSTOP to sleep process
# Gửi SIGSTOP đến tiến trình sleep
kill -SIGSTOP $SLEEP_PID
echo "Process $SLEEP_PID stopped"

# Send SIGCONT to resume
# Gửi SIGCONT để tiếp tục
kill -SIGCONT $SLEEP_PID
echo "Process $SLEEP_PID resumed"

# 5. Process Termination
# 5. Kết thúc tiến trình
echo "5. Terminating processes..."

# Terminate sleep process
# Kết thúc tiến trình sleep
kill $SLEEP_PID
echo "Process $SLEEP_PID terminated"

# 6. System Resource Monitoring
# 6. Giám sát tài nguyên hệ thống
echo "6. Monitoring system resources..."

# CPU information
# Thông tin CPU
echo "CPU Information:"
lscpu

# Memory information
# Thông tin bộ nhớ
echo "Memory Information:"
free -h

# Disk usage
# Sử dụng ổ đĩa
echo "Disk Usage:"
df -h

# 7. Process Scheduling
# 7. Lập lịch tiến trình
echo "7. Process scheduling..."

# Show process scheduling policy
# Hiển thị chính sách lập lịch tiến trình
echo "Process scheduling policy:"
ps -eo pid,cmd,cls | grep -v "ps -eo"

# Change process priority
# Thay đổi độ ưu tiên tiến trình
echo "Changing process priority..."
nice -n 10 sleep 10 &
NICE_PID=$!
ps -p $NICE_PID -o pid,ni,cmd

# Cleanup
# Dọn dẹp
kill $NICE_PID 2>/dev/null

echo "=== Lab completed ==="
echo "You have learned:"
echo "- Process listing and monitoring"
echo "- Process control and signals"
echo "- System resource monitoring"
echo "- Process scheduling and priorities" 
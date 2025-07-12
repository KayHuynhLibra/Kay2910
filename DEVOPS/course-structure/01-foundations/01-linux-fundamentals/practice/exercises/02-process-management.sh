#!/bin/bash

# Bài tập 2: Process Management
# Mục tiêu: Thực hành quản lý processes và jobs

echo "=== Bài tập Process Management ==="

# 1. Tạo và quản lý background processes
echo "1. Tạo và quản lý background processes..."
echo "Starting test processes..."

# Tạo một số processes
sleep 100 &
PID1=$!
echo "Started sleep process with PID: $PID1"

sleep 200 &
PID2=$!
echo "Started another sleep process with PID: $PID2"

# 2. Kiểm tra processes
echo "2. Kiểm tra processes..."
echo "Running processes:"
ps aux | grep sleep

echo "Process tree:"
pstree -p

# 3. Quản lý jobs
echo "3. Quản lý jobs..."
echo "Current jobs:"
jobs

# 4. Process signals
echo "4. Process signals..."
echo "Available signals:"
kill -l

echo "Sending SIGTERM to first process..."
kill $PID1
sleep 1
ps -p $PID1 >/dev/null && echo "Process still running" || echo "Process terminated"

echo "Sending SIGKILL to second process..."
kill -9 $PID2
sleep 1
ps -p $PID2 >/dev/null && echo "Process still running" || echo "Process terminated"

# 5. Process monitoring
echo "5. Process monitoring..."
echo "System process summary:"
ps aux --sort=-%cpu | head -n 5

echo "Memory usage:"
free -h

echo "=== Hoàn thành bài tập ===" 
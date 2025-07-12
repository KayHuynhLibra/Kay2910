#!/bin/bash

# Lab 1: System Administration Lab
# Mục tiêu: Tạo một hệ thống giám sát đơn giản kết hợp các kỹ năng đã học
# Objective: Create a simple monitoring system combining learned skills

echo "=== Lab 1: System Administration Lab ==="

# Create directory structure for the lab
# Tạo cấu trúc thư mục cho lab
LAB_DIR=~/devops-lab
mkdir -p $LAB_DIR/{bin,etc,var/{log,www},tmp}

# 1. Create system monitoring script
# 1. Tạo script giám sát hệ thống
echo "1. Tạo script giám sát hệ thống..."
cat > $LAB_DIR/bin/monitor.sh << 'EOF'
#!/bin/bash

# Configuration variables
# Các biến cấu hình
LOG_FILE="$HOME/devops-lab/var/log/system.log"
ALERT_THRESHOLD=80  # Alert threshold in percentage / Ngưỡng cảnh báo theo phần trăm

# Function to log messages with timestamp
# Hàm ghi log với thời gian
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
}

# Function to check disk usage
# Hàm kiểm tra sử dụng ổ đĩa
check_disk_usage() {
    # Get disk usage percentage for root partition
    # Lấy phần trăm sử dụng ổ đĩa cho phân vùng gốc
    local usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
    if [ $usage -gt $ALERT_THRESHOLD ]; then
        log_message "WARNING: Disk usage is $usage%"
    else
        log_message "INFO: Disk usage is $usage%"
    fi
}

# Function to check memory usage
# Hàm kiểm tra sử dụng bộ nhớ
check_memory_usage() {
    # Calculate memory usage percentage
    # Tính toán phần trăm sử dụng bộ nhớ
    local usage=$(free | awk '/Mem:/ {print int($3/$2 * 100)}')
    if [ $usage -gt $ALERT_THRESHOLD ]; then
        log_message "WARNING: Memory usage is $usage%"
    else
        log_message "INFO: Memory usage is $usage%"
    fi
}

# Function to check network connectivity
# Hàm kiểm tra kết nối mạng
check_network() {
    # Test connectivity to Google's DNS (8.8.8.8)
    # Kiểm tra kết nối đến DNS của Google (8.8.8.8)
    if ping -c 1 8.8.8.8 >/dev/null 2>&1; then
        log_message "INFO: Network connectivity OK"
    else
        log_message "ERROR: Network connectivity failed"
    fi
}

# Function to check top CPU-consuming processes
# Hàm kiểm tra các tiến trình sử dụng CPU nhiều nhất
check_processes() {
    # Get top 5 CPU-consuming processes
    # Lấy 5 tiến trình sử dụng CPU nhiều nhất
    local high_cpu=$(ps aux | sort -nrk 3,3 | head -n 5)
    log_message "Top 5 CPU consuming processes:\n$high_cpu"
}

# Main monitoring loop
# Vòng lặp giám sát chính
while true; do
    check_disk_usage
    check_memory_usage
    check_network
    check_processes
    sleep 300  # Check every 5 minutes / Kiểm tra mỗi 5 phút
done
EOF

# 2. Create systemd service file
# 2. Tạo file service systemd
echo "2. Tạo systemd service..."
cat > $LAB_DIR/etc/system-monitor.service << EOF
[Unit]
Description=System Monitoring Service
After=network.target

[Service]
Type=simple
User=$USER
ExecStart=$LAB_DIR/bin/monitor.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# 3. Installation and configuration
# 3. Cài đặt và cấu hình
echo "3. Cài đặt và cấu hình..."
chmod +x $LAB_DIR/bin/monitor.sh

# Create symbolic link for service
# Tạo liên kết tượng trưng cho service
sudo ln -sf $LAB_DIR/etc/system-monitor.service /etc/systemd/system/
sudo systemctl daemon-reload

# 4. Create report generation script
# 4. Tạo script tạo báo cáo
echo "4. Tạo script báo cáo..."
cat > $LAB_DIR/bin/generate-report.sh << 'EOF'
#!/bin/bash

# Configuration variables
# Các biến cấu hình
LOG_FILE="$HOME/devops-lab/var/log/system.log"
REPORT_DIR="$HOME/devops-lab/var/www/reports"

# Create report directory if it doesn't exist
# Tạo thư mục báo cáo nếu chưa tồn tại
mkdir -p $REPORT_DIR

# Function to generate HTML report
# Hàm tạo báo cáo HTML
generate_report() {
    local report_file="$REPORT_DIR/system-report-$(date +%Y%m%d).html"
    
    # Create HTML header
    # Tạo phần đầu HTML
    echo "<html><body>" > $report_file
    echo "<h1>System Report - $(date)</h1>" >> $report_file
    
    # Generate disk usage table
    # Tạo bảng sử dụng ổ đĩa
    echo "<h2>Disk Usage</h2>" >> $report_file
    df -h | awk 'BEGIN{print "<table border=1>"} 
                 {print "<tr><td>" $1 "</td><td>" $2 "</td><td>" $3 "</td><td>" $4 "</td><td>" $5 "</td></tr>"} 
                 END{print "</table>"}' >> $report_file
    
    # Generate memory usage table
    # Tạo bảng sử dụng bộ nhớ
    echo "<h2>Memory Usage</h2>" >> $report_file
    free -h | awk 'BEGIN{print "<table border=1>"} 
                   {print "<tr><td>" $1 "</td><td>" $2 "</td><td>" $3 "</td><td>" $4 "</td></tr>"} 
                   END{print "</table>"}' >> $report_file
    
    # Add recent log entries
    # Thêm các mục log gần đây
    echo "<h2>Recent Log Entries</h2>" >> $report_file
    echo "<pre>" >> $report_file
    tail -n 20 $LOG_FILE >> $report_file
    echo "</pre>" >> $report_file
    
    echo "</body></html>" >> $report_file
}

generate_report
EOF

chmod +x $LAB_DIR/bin/generate-report.sh

# 5. Create cron job for report generation
# 5. Tạo cron job cho việc tạo báo cáo
echo "5. Tạo cron job cho báo cáo..."
(crontab -l 2>/dev/null; echo "0 0 * * * $LAB_DIR/bin/generate-report.sh") | crontab -

# 6. Start the monitoring service
# 6. Khởi động service giám sát
echo "6. Khởi động service..."
sudo systemctl enable system-monitor
sudo systemctl start system-monitor

# 7. Check service status
# 7. Kiểm tra trạng thái service
echo "7. Kiểm tra trạng thái..."
echo "Service status:"
sudo systemctl status system-monitor

echo "Log file location: $LAB_DIR/var/log/system.log"
echo "Report location: $LAB_DIR/var/www/reports"

echo "=== Lab hoàn thành ==="
echo "Hãy kiểm tra các file và thư mục đã tạo trong $LAB_DIR" 
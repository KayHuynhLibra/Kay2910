# System Administration Lab Explanation
# Giải thích Lab Quản trị Hệ thống

## Overview / Tổng quan

This lab demonstrates how to create a basic system monitoring solution using shell scripts and systemd services. The system monitors various aspects of the Linux system including disk usage, memory usage, network connectivity, and process status.

Lab này minh họa cách tạo một giải pháp giám sát hệ thống cơ bản sử dụng shell script và systemd service. Hệ thống giám sát các khía cạnh khác nhau của hệ thống Linux bao gồm sử dụng ổ đĩa, sử dụng bộ nhớ, kết nối mạng và trạng thái tiến trình.

## Directory Structure / Cấu trúc thư mục

```
~/devops-lab/
├── bin/                    # Executable scripts / Script thực thi
│   ├── monitor.sh         # Main monitoring script / Script giám sát chính
│   └── generate-report.sh # Report generation script / Script tạo báo cáo
├── etc/                   # Configuration files / File cấu hình
│   └── system-monitor.service  # Systemd service file / File service systemd
├── var/
│   ├── log/              # Log files / File log
│   │   └── system.log    # System monitoring logs / Log giám sát hệ thống
│   └── www/
│       └── reports/      # Generated HTML reports / Báo cáo HTML được tạo
└── tmp/                  # Temporary files / File tạm thời
```

## Components / Các thành phần

### 1. Monitor Script (monitor.sh) / Script Giám sát

The main monitoring script performs the following functions:
Script giám sát chính thực hiện các chức năng sau:

#### Configuration / Cấu hình
```bash
LOG_FILE="$HOME/devops-lab/var/log/system.log"
ALERT_THRESHOLD=80  # Alert threshold in percentage / Ngưỡng cảnh báo theo phần trăm
```

#### Functions / Các hàm

1. **log_message()**
   - Purpose / Mục đích: Logs messages with timestamps
   - Chức năng: Ghi log với thời gian
   ```bash
   log_message() {
       echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
   }
   ```

2. **check_disk_usage()**
   - Purpose / Mục đích: Monitors disk usage and alerts if above threshold
   - Chức năng: Giám sát sử dụng ổ đĩa và cảnh báo nếu vượt ngưỡng
   ```bash
   check_disk_usage() {
       local usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
       if [ $usage -gt $ALERT_THRESHOLD ]; then
           log_message "WARNING: Disk usage is $usage%"
       else
           log_message "INFO: Disk usage is $usage%"
       fi
   }
   ```

3. **check_memory_usage()**
   - Purpose / Mục đích: Monitors memory usage and alerts if above threshold
   - Chức năng: Giám sát sử dụng bộ nhớ và cảnh báo nếu vượt ngưỡng
   ```bash
   check_memory_usage() {
       local usage=$(free | awk '/Mem:/ {print int($3/$2 * 100)}')
       if [ $usage -gt $ALERT_THRESHOLD ]; then
           log_message "WARNING: Memory usage is $usage%"
       else
           log_message "INFO: Memory usage is $usage%"
       fi
   }
   ```

4. **check_network()**
   - Purpose / Mục đích: Tests network connectivity to Google's DNS
   - Chức năng: Kiểm tra kết nối mạng đến DNS của Google
   ```bash
   check_network() {
       if ping -c 1 8.8.8.8 >/dev/null 2>&1; then
           log_message "INFO: Network connectivity OK"
       else
           log_message "ERROR: Network connectivity failed"
       fi
   }
   ```

5. **check_processes()**
   - Purpose / Mục đích: Monitors top CPU-consuming processes
   - Chức năng: Giám sát các tiến trình sử dụng CPU nhiều nhất
   ```bash
   check_processes() {
       local high_cpu=$(ps aux | sort -nrk 3,3 | head -n 5)
       log_message "Top 5 CPU consuming processes:\n$high_cpu"
   }
   ```

### 2. Report Generation Script (generate-report.sh) / Script Tạo Báo cáo

This script generates HTML reports with system information:
Script này tạo báo cáo HTML với thông tin hệ thống:

#### Features / Tính năng
- Creates daily HTML reports / Tạo báo cáo HTML hàng ngày
- Includes disk usage tables / Bao gồm bảng sử dụng ổ đĩa
- Includes memory usage tables / Bao gồm bảng sử dụng bộ nhớ
- Shows recent log entries / Hiển thị các mục log gần đây

### 3. Systemd Service / Dịch vụ Systemd

The systemd service file ensures the monitoring script runs as a system service:
File service systemd đảm bảo script giám sát chạy như một dịch vụ hệ thống:

```ini
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
```

## Usage / Cách sử dụng

1. **Installation / Cài đặt**
   ```bash
   # Create directory structure / Tạo cấu trúc thư mục
   mkdir -p ~/devops-lab/{bin,etc,var/{log,www},tmp}
   
   # Copy scripts / Sao chép script
   cp monitor.sh ~/devops-lab/bin/
   cp generate-report.sh ~/devops-lab/bin/
   
   # Set permissions / Đặt quyền
   chmod +x ~/devops-lab/bin/*.sh
   ```

2. **Service Setup / Thiết lập Service**
   ```bash
   # Create service file / Tạo file service
   sudo cp system-monitor.service /etc/systemd/system/
   
   # Enable and start service / Kích hoạt và khởi động service
   sudo systemctl daemon-reload
   sudo systemctl enable system-monitor
   sudo systemctl start system-monitor
   ```

3. **Schedule Reports / Lên lịch báo cáo**
   ```bash
   # Add to crontab / Thêm vào crontab
   (crontab -l 2>/dev/null; echo "0 0 * * * $LAB_DIR/bin/generate-report.sh") | crontab -
   ```

## Monitoring / Giám sát

- Log files are stored in: `~/devops-lab/var/log/system.log`
- File log được lưu tại: `~/devops-lab/var/log/system.log`
- Reports are generated in: `~/devops-lab/var/www/reports/`
- Báo cáo được tạo tại: `~/devops-lab/var/www/reports/`

## Customization / Tùy chỉnh

You can customize the monitoring system by:
Bạn có thể tùy chỉnh hệ thống giám sát bằng cách:

1. Adjusting `ALERT_THRESHOLD` in monitor.sh
   Điều chỉnh `ALERT_THRESHOLD` trong monitor.sh

2. Modifying the check interval (currently 5 minutes)
   Sửa đổi khoảng thời gian kiểm tra (hiện tại là 5 phút)

3. Adding new monitoring functions
   Thêm các hàm giám sát mới

4. Customizing the report format
   Tùy chỉnh định dạng báo cáo

## Security Considerations / Cân nhắc bảo mật

1. The monitoring script runs with user privileges
   Script giám sát chạy với quyền người dùng

2. Log files should be regularly rotated
   File log nên được luân chuyển thường xuyên

3. Reports should be protected from unauthorized access
   Báo cáo nên được bảo vệ khỏi truy cập trái phép

## Troubleshooting / Xử lý sự cố

1. Check service status:
   Kiểm tra trạng thái service:
   ```bash
   sudo systemctl status system-monitor
   ```

2. View logs:
   Xem log:
   ```bash
   tail -f ~/devops-lab/var/log/system.log
   ```

3. Check report generation:
   Kiểm tra tạo báo cáo:
   ```bash
   ls -l ~/devops-lab/var/www/reports/
   ``` 
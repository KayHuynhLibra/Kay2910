# Linux Fundamentals - Phần 3: System Administration

## 1. Quản lý hệ thống
- Khởi động và tắt máy
- Quản lý dịch vụ
- Quản lý người dùng và nhóm
- Quản lý gói phần mềm

## 2. Quản lý tiến trình
```bash
# Xem danh sách tiến trình
ps aux
top
htop

# Quản lý tiến trình
kill PID
killall process_name
nice -n 10 command
renice 10 PID

# Quản lý dịch vụ
systemctl start service_name
systemctl stop service_name
systemctl restart service_name
systemctl status service_name
systemctl enable service_name
systemctl disable service_name
```

## 3. Quản lý tài nguyên
```bash
# CPU
top
htop
vmstat 1
mpstat 1

# Memory
free -h
vmstat 1
cat /proc/meminfo

# Disk
df -h
du -sh *
iostat 1
iotop

# Network
netstat -tuln
ss -tuln
iftop
nethogs
```

## 4. Quản lý log
```bash
# System logs
tail -f /var/log/syslog
tail -f /var/log/auth.log
journalctl -f

# Log rotation
logrotate -d /etc/logrotate.conf
logrotate -f /etc/logrotate.d/application

# Log analysis
grep "ERROR" /var/log/syslog
awk '/ERROR/ {print $0}' /var/log/syslog
```

## 5. Bảo mật hệ thống
```bash
# Firewall
ufw enable
ufw allow 22/tcp
ufw deny 23/tcp
ufw status

# SELinux
getenforce
setenforce 1
sestatus

# File permissions
chmod 755 file
chown user:group file
chattr +i file
```

## 6. Backup và Recovery
```bash
# Backup files
tar -czf backup.tar.gz /path/to/files
rsync -avz source/ destination/

# Backup system
dd if=/dev/sda of=/path/to/backup.img
clonezilla

# Recovery
tar -xzf backup.tar.gz
rsync -avz backup/ /path/to/restore/
```

## 7. Monitoring và Alerting
```bash
# System monitoring
sar -u 1
sar -r 1
sar -d 1

# Alerting
echo "Alert: High CPU usage" | mail -s "System Alert" admin@example.com
curl -X POST -H "Content-Type: application/json" -d '{"message":"Alert"}' http://alert-server

# Custom monitoring script
#!/bin/bash
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')
if [ $(echo "$CPU_USAGE > 80" | bc) -eq 1 ]; then
    echo "High CPU usage: $CPU_USAGE%" | mail -s "CPU Alert" admin@example.com
fi
```

## 8. Performance Tuning
```bash
# Kernel parameters
sysctl -a
sysctl -w net.ipv4.tcp_syncookies=1
echo "net.ipv4.tcp_syncookies=1" >> /etc/sysctl.conf

# Resource limits
ulimit -a
ulimit -n 65535
echo "* soft nofile 65535" >> /etc/security/limits.conf

# Process priority
nice -n -20 command
renice -20 PID
```

## 9. Troubleshooting
```bash
# System logs
dmesg
journalctl -xb
tail -f /var/log/syslog

# Network
ping google.com
traceroute google.com
netstat -tuln
ss -tuln

# Disk
df -h
du -sh *
iostat 1
```

## 10. Best Practices
- Regular system updates
- Security patches
- Backup strategy
- Monitoring setup
- Documentation
- Change management
- Disaster recovery plan

## Bài tập thực hành
1. Cấu hình và quản lý dịch vụ
2. Thiết lập monitoring và alerting
3. Tạo và quản lý backup
4. Xử lý sự cố hệ thống

## Tài liệu tham khảo
- Linux System Administration Handbook
- Red Hat Enterprise Linux Documentation
- Ubuntu Server Guide 
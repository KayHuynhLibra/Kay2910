# Linux Reference Guide / Hướng Dẫn Tham Khảo Linux

## System Information / Thông Tin Hệ Thống
### Hardware Information / Thông Tin Phần Cứng
```bash
# CPU information / Thông tin CPU
lscpu
cat /proc/cpuinfo

# Memory information / Thông tin bộ nhớ
free -h
cat /proc/meminfo

# Disk information / Thông tin ổ đĩa
df -h
lsblk
```

### System Status / Trạng Thái Hệ Thống
```bash
# System uptime / Thời gian hoạt động
uptime

# System load / Tải hệ thống
top
htop

# System logs / Nhật ký hệ thống
dmesg
journalctl
```

## File System / Hệ Thống File
### Directory Structure / Cấu Trúc Thư Mục
```
/           # Root directory / Thư mục gốc
/bin        # Essential commands / Lệnh cơ bản
/boot       # Boot files / File khởi động
/dev        # Device files / File thiết bị
/etc        # Configuration files / File cấu hình
/home       # User home directories / Thư mục home người dùng
/lib        # System libraries / Thư viện hệ thống
/media      # Removable media / Phương tiện tháo lắp
/mnt        # Mount points / Điểm gắn kết
/opt        # Optional software / Phần mềm tùy chọn
/proc       # Process information / Thông tin tiến trình
/root       # Root user home / Thư mục home root
/sbin       # System binaries / File thực thi hệ thống
/tmp        # Temporary files / File tạm
/usr        # User programs / Chương trình người dùng
/var        # Variable files / File biến đổi
```

### File Operations / Thao Tác File
```bash
# Create directory / Tạo thư mục
mkdir dirname

# Create file / Tạo file
touch filename

# Copy file / Sao chép file
cp source destination

# Move file / Di chuyển file
mv source destination

# Remove file / Xóa file
rm filename

# Remove directory / Xóa thư mục
rm -r dirname
```

## User Management / Quản Lý Người Dùng
### User Commands / Lệnh Người Dùng
```bash
# Add user / Thêm người dùng
useradd username

# Set password / Đặt mật khẩu
passwd username

# Delete user / Xóa người dùng
userdel username

# Add user to group / Thêm người dùng vào nhóm
usermod -aG groupname username
```

### Group Commands / Lệnh Nhóm
```bash
# Create group / Tạo nhóm
groupadd groupname

# Delete group / Xóa nhóm
groupdel groupname

# List groups / Liệt kê nhóm
groups username
```

## Process Management / Quản Lý Tiến Trình
### Process Commands / Lệnh Tiến Trình
```bash
# List processes / Liệt kê tiến trình
ps aux

# Kill process / Kết thúc tiến trình
kill PID

# Kill process forcefully / Kết thúc tiến trình cưỡng bức
kill -9 PID

# Process priority / Độ ưu tiên tiến trình
nice -n 10 command
renice -n 10 PID
```

### System Services / Dịch Vụ Hệ Thống
```bash
# List services / Liệt kê dịch vụ
systemctl list-units --type=service

# Start service / Khởi động dịch vụ
systemctl start service

# Stop service / Dừng dịch vụ
systemctl stop service

# Enable service / Bật dịch vụ
systemctl enable service

# Disable service / Tắt dịch vụ
systemctl disable service
```

## Networking / Mạng
### Network Configuration / Cấu Hình Mạng
```bash
# Network interfaces / Giao diện mạng
ifconfig
ip addr

# Network connections / Kết nối mạng
netstat -tuln
ss -tuln

# Network routing / Định tuyến mạng
route
ip route
```

### Network Tools / Công Cụ Mạng
```bash
# Test connectivity / Kiểm tra kết nối
ping hostname

# Trace route / Theo dõi tuyến đường
traceroute hostname

# DNS lookup / Tra cứu DNS
nslookup hostname
dig hostname

# Network scanner / Quét mạng
nmap hostname
```

## Security / Bảo Mật
### File Permissions / Phân Quyền File
```bash
# Change permissions / Thay đổi phân quyền
chmod 755 filename
chmod u+x filename

# Change ownership / Thay đổi quyền sở hữu
chown user:group filename

# Set ACL / Đặt ACL
setfacl -m u:user:rwx filename
getfacl filename
```

### Security Tools / Công Cụ Bảo Mật
```bash
# Firewall / Tường lửa
iptables -L
ufw status

# SELinux / SELinux
getenforce
setenforce 1

# Audit / Kiểm toán
auditctl -l
ausearch -i
```

## Package Management / Quản Lý Gói
### Debian/Ubuntu / Debian/Ubuntu
```bash
# Update package list / Cập nhật danh sách gói
apt update

# Upgrade packages / Nâng cấp gói
apt upgrade

# Install package / Cài đặt gói
apt install package

# Remove package / Gỡ gói
apt remove package
```

### Red Hat/CentOS / Red Hat/CentOS
```bash
# Update packages / Cập nhật gói
yum update

# Install package / Cài đặt gói
yum install package

# Remove package / Gỡ gói
yum remove package
```

## System Maintenance / Bảo Trì Hệ Thống
### Backup / Sao Lưu
```bash
# Create backup / Tạo bản sao lưu
tar -czf backup.tar.gz directory

# Restore backup / Khôi phục bản sao lưu
tar -xzf backup.tar.gz
```

### System Updates / Cập Nhật Hệ Thống
```bash
# Update system / Cập nhật hệ thống
apt update && apt upgrade
yum update

# Clean package cache / Dọn bộ nhớ đệm gói
apt clean
yum clean all
```

## Troubleshooting / Xử Lý Sự Cố
### System Logs / Nhật Ký Hệ Thống
```bash
# System log / Nhật ký hệ thống
tail -f /var/log/syslog
journalctl -f

# Authentication log / Nhật ký xác thực
tail -f /var/log/auth.log

# Application log / Nhật ký ứng dụng
tail -f /var/log/application.log
```

### System Recovery / Khôi Phục Hệ Thống
```bash
# Check disk / Kiểm tra ổ đĩa
fsck /dev/sda1

# Repair filesystem / Sửa hệ thống file
e2fsck -f /dev/sda1

# Recover deleted files / Khôi phục file đã xóa
extundelete /dev/sda1
```

## Resources / Tài Nguyên
- Linux Documentation Project
- Ubuntu Documentation
- Red Hat Documentation
- Linux Kernel Documentation 
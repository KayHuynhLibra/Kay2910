# Linux Fundamentals / Cơ Bản Linux

## Introduction / Giới Thiệu

### What is Linux? / Linux là gì?
- Open-source operating system / Hệ điều hành mã nguồn mở
- Unix-like system / Hệ thống giống Unix
- Kernel + GNU tools / Nhân + Công cụ GNU
- Community-driven development / Phát triển dựa trên cộng đồng

### History / Lịch Sử
- Created by Linus Torvalds / Được tạo bởi Linus Torvalds
- First release in 1991 / Phát hành lần đầu năm 1991
- Based on MINIX / Dựa trên MINIX
- GNU Project influence / Ảnh hưởng từ Dự án GNU

### Distributions / Phân Phối
- Ubuntu / Ubuntu
- Debian / Debian
- Red Hat / Red Hat
- CentOS / CentOS
- Kali Linux / Kali Linux

## Linux File System / Hệ Thống File Linux

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

### Important Directories / Thư Mục Quan Trọng
- /etc: System configuration / Cấu hình hệ thống
- /var: Variable data / Dữ liệu biến đổi
- /home: User data / Dữ liệu người dùng
- /bin: Essential commands / Lệnh cơ bản

### File Types / Loại File
- Regular files / File thông thường
- Directories / Thư mục
- Symbolic links / Liên kết tượng trưng
- Device files / File thiết bị
- Named pipes / Ống có tên
- Sockets / Ổ cắm

## Basic Commands / Lệnh Cơ Bản

### Navigation Commands / Lệnh Điều Hướng
```bash
pwd         # Print working directory / In thư mục hiện tại
cd          # Change directory / Thay đổi thư mục
ls          # List directory contents / Liệt kê nội dung thư mục
```

### File Operations / Thao Tác File
```bash
touch       # Create empty file / Tạo file trống
cp          # Copy files / Sao chép file
mv          # Move files / Di chuyển file
rm          # Remove files / Xóa file
```

### Text Processing / Xử Lý Văn Bản
```bash
cat         # Concatenate files / Nối file
grep        # Search text / Tìm kiếm văn bản
sed         # Stream editor / Trình soạn thảo luồng
awk         # Text processing / Xử lý văn bản
```

## User Management / Quản Lý Người Dùng

### User Accounts / Tài Khoản Người Dùng
- Root user / Người dùng root
- Regular users / Người dùng thông thường
- System users / Người dùng hệ thống

### Groups / Nhóm
- Primary group / Nhóm chính
- Secondary groups / Nhóm phụ
- System groups / Nhóm hệ thống

### Permissions / Phân Quyền
```bash
# Permission types / Loại phân quyền
r           # Read / Đọc
w           # Write / Ghi
x           # Execute / Thực thi

# Permission categories / Phân loại phân quyền
u           # User / Người dùng
g           # Group / Nhóm
o           # Others / Khác
```

### sudo / sudo
- Superuser do / Thực thi với quyền siêu người dùng
- Configuration / Cấu hình
- Best practices / Thực hành tốt nhất

## Process Management / Quản Lý Tiến Trình

### Viewing Processes / Xem Tiến Trình
```bash
ps          # Process status / Trạng thái tiến trình
top         # Process viewer / Trình xem tiến trình
htop        # Interactive process viewer / Trình xem tiến trình tương tác
```

### Managing Processes / Quản Lý Tiến Trình
```bash
kill        # Terminate process / Kết thúc tiến trình
nice        # Set process priority / Đặt độ ưu tiên tiến trình
renice      # Change process priority / Thay đổi độ ưu tiên tiến trình
```

### Background Processes / Tiến Trình Nền
```bash
&           # Run in background / Chạy trong nền
bg          # Continue in background / Tiếp tục trong nền
fg          # Bring to foreground / Đưa lên nền trước
```

## Networking / Mạng

### Network Configuration / Cấu Hình Mạng
```bash
ifconfig    # Network interface configuration / Cấu hình giao diện mạng
ip          # IP command / Lệnh IP
netstat     # Network statistics / Thống kê mạng
```

### Network Tools / Công Cụ Mạng
```bash
ping        # Test connectivity / Kiểm tra kết nối
traceroute  # Trace route / Theo dõi tuyến đường
nslookup    # DNS lookup / Tra cứu DNS
```

### Firewall / Tường Lửa
- iptables / iptables
- ufw / ufw
- firewalld / firewalld

### SSH / SSH
- Secure shell / Shell an toàn
- Configuration / Cấu hình
- Key-based authentication / Xác thực dựa trên khóa

## Security / Bảo Mật

### File Permissions / Phân Quyền File
```bash
chmod       # Change mode / Thay đổi chế độ
chown       # Change owner / Thay đổi chủ sở hữu
chgrp       # Change group / Thay đổi nhóm
```

### User Authentication / Xác Thực Người Dùng
- Password policies / Chính sách mật khẩu
- PAM / PAM
- sudoers / sudoers

### Access Control / Kiểm Soát Truy Cập
- ACL / ACL
- SELinux / SELinux
- AppArmor / AppArmor

### Security Tools / Công Cụ Bảo Mật
- fail2ban / fail2ban
- rkhunter / rkhunter
- chkrootkit / chkrootkit

## Shell Scripting / Lập Trình Shell

### Basic Syntax / Cú Pháp Cơ Bản
```bash
#!/bin/bash  # Shebang / Shebang
# Comments   # Chú thích
variables    # Biến
```

### Variables / Biến
```bash
# Variable assignment / Gán biến
name="value"

# Variable usage / Sử dụng biến
$name
${name}
```

### Control Structures / Cấu Trúc Điều Khiển
```bash
# If statement / Câu lệnh if
if [ condition ]; then
    # code
fi

# For loop / Vòng lặp for
for item in list; do
    # code
done

# While loop / Vòng lặp while
while [ condition ]; do
    # code
done
```

### Functions / Hàm
```bash
# Function definition / Định nghĩa hàm
function_name() {
    # code
}

# Function call / Gọi hàm
function_name
```

## System Administration / Quản Trị Hệ Thống

### Package Management / Quản Lý Gói
```bash
# Debian/Ubuntu
apt update
apt upgrade
apt install
apt remove

# Red Hat/CentOS
yum update
yum install
yum remove
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

### Logs / Nhật Ký
```bash
# System logs / Nhật ký hệ thống
/var/log/syslog
/var/log/auth.log
journalctl
```

### Backup / Sao Lưu
```bash
# Create backup / Tạo bản sao lưu
tar -czf backup.tar.gz directory

# Restore backup / Khôi phục bản sao lưu
tar -xzf backup.tar.gz
```

## Best Practices / Thực Hành Tốt Nhất

### Security Practices / Thực Hành Bảo Mật
- Regular updates / Cập nhật thường xuyên
- Strong passwords / Mật khẩu mạnh
- Minimal permissions / Phân quyền tối thiểu
- Security monitoring / Giám sát bảo mật

### System Maintenance / Bảo Trì Hệ Thống
- Regular backups / Sao lưu thường xuyên
- Disk space management / Quản lý không gian đĩa
- Performance monitoring / Giám sát hiệu suất
- System logs / Nhật ký hệ thống

### Documentation / Tài Liệu
- System configuration / Cấu hình hệ thống
- Change management / Quản lý thay đổi
- Incident response / Ứng phó sự cố
- Knowledge base / Cơ sở kiến thức

### Troubleshooting / Xử Lý Sự Cố
- Problem identification / Xác định vấn đề
- Information gathering / Thu thập thông tin
- Solution implementation / Triển khai giải pháp
- Documentation / Tài liệu

## Resources / Tài Nguyên

### Online Documentation / Tài Liệu Trực Tuyến
- Linux Documentation Project
- Ubuntu Documentation
- Red Hat Documentation
- Linux Kernel Documentation

### Books / Sách
- "The Linux Command Line"
- "Linux System Administration"
- "Linux Security Cookbook"
- "Advanced Linux Programming"

### Communities / Cộng Đồng
- Stack Overflow
- Linux Forums
- Reddit /r/linux
- Linux Foundation

### Training / Đào Tạo
- Linux Foundation
- Red Hat Training
- Ubuntu Training
- Online Courses

## Lab Exercises / Bài Tập Thực Hành

### Basic Commands / Lệnh Cơ Bản
1. File system navigation / Điều hướng hệ thống file
2. File operations / Thao tác file
3. Text processing / Xử lý văn bản
4. User management / Quản lý người dùng

### System Administration / Quản Trị Hệ Thống
1. Package management / Quản lý gói
2. System updates / Cập nhật hệ thống
3. Log analysis / Phân tích nhật ký
4. Backup and restore / Sao lưu và khôi phục

### Security / Bảo Mật
1. File permissions / Phân quyền file
2. User authentication / Xác thực người dùng
3. Access control / Kiểm soát truy cập
4. Security tools / Công cụ bảo mật

### Shell Scripting / Lập Trình Shell
1. Basic scripts / Script cơ bản
2. Control structures / Cấu trúc điều khiển
3. Functions / Hàm
4. Automation / Tự động hóa

## Assessment / Đánh Giá

### Quizzes / Kiểm Tra
- Multiple choice / Trắc nghiệm
- True/False / Đúng/Sai
- Short answer / Trả lời ngắn
- Practical questions / Câu hỏi thực hành

### Lab Assignments / Bài Tập Thực Hành
- Command line exercises / Bài tập dòng lệnh
- System administration tasks / Tác vụ quản trị hệ thống
- Security configurations / Cấu hình bảo mật
- Scripting projects / Dự án lập trình

### Projects / Dự Án
- System setup / Thiết lập hệ thống
- Security implementation / Triển khai bảo mật
- Automation scripts / Script tự động hóa
- Documentation / Tài liệu

### Final Exam / Thi Cuối Kỳ
- Theoretical knowledge / Kiến thức lý thuyết
- Practical skills / Kỹ năng thực hành
- Problem solving / Giải quyết vấn đề
- Best practices / Thực hành tốt nhất

## Next Steps / Bước Tiếp Theo

### Advanced Topics / Chủ Đề Nâng Cao
- Kernel programming / Lập trình nhân
- System programming / Lập trình hệ thống
- Network programming / Lập trình mạng
- Security programming / Lập trình bảo mật

### Security Tools / Công Cụ Bảo Mật
- Penetration testing / Kiểm thử xâm nhập
- Vulnerability assessment / Đánh giá lỗ hổng
- Security monitoring / Giám sát bảo mật
- Incident response / Ứng phó sự cố

### System Administration / Quản Trị Hệ Thống
- High availability / Tính sẵn sàng cao
- Load balancing / Cân bằng tải
- Containerization / Ảo hóa container
- Cloud integration / Tích hợp đám mây

### Professional Certification / Chứng Chỉ Chuyên Nghiệp
- Linux Foundation
- Red Hat
- CompTIA Linux+
- LPIC 
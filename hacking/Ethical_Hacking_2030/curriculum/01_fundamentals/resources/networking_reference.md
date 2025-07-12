# Networking Reference Guide / Hướng Dẫn Tham Khảo Mạng

## TCP/IP Protocol Suite / Bộ Giao Thức TCP/IP

### Application Layer / Tầng Ứng Dụng
```
HTTP (80)    - Web browsing / Duyệt web
HTTPS (443)  - Secure web browsing / Duyệt web an toàn
FTP (21)     - File transfer / Truyền file
SSH (22)     - Secure shell / Shell an toàn
Telnet (23)  - Remote access / Truy cập từ xa
SMTP (25)    - Email sending / Gửi email
DNS (53)     - Domain name resolution / Phân giải tên miền
DHCP (67,68) - IP address assignment / Cấp phát địa chỉ IP
```

### Transport Layer / Tầng Giao Vận
```
TCP - Transmission Control Protocol
- Connection-oriented / Hướng kết nối
- Reliable delivery / Giao tin cậy
- Flow control / Điều khiển luồng
- Error checking / Kiểm tra lỗi

UDP - User Datagram Protocol
- Connectionless / Không kết nối
- Fast delivery / Giao nhanh
- No flow control / Không điều khiển luồng
- Basic error checking / Kiểm tra lỗi cơ bản
```

### Network Layer / Tầng Mạng
```
IPv4 - Internet Protocol version 4
- 32-bit addresses / Địa chỉ 32-bit
- Classes A, B, C, D, E / Các lớp A, B, C, D, E
- Subnetting / Phân mạng con
- NAT / Chuyển đổi địa chỉ mạng

IPv6 - Internet Protocol version 6
- 128-bit addresses / Địa chỉ 128-bit
- Improved security / Bảo mật tốt hơn
- Auto-configuration / Tự cấu hình
- Better routing / Định tuyến tốt hơn
```

### Link Layer / Tầng Liên Kết
```
Ethernet
- MAC addresses / Địa chỉ MAC
- CSMA/CD / Phát hiện xung đột
- Frame format / Định dạng frame
- Speed standards / Tiêu chuẩn tốc độ

ARP - Address Resolution Protocol
- IP to MAC mapping / Ánh xạ IP sang MAC
- ARP cache / Bộ nhớ đệm ARP
- ARP spoofing / Giả mạo ARP
- ARP security / Bảo mật ARP
```

## Network Devices / Thiết Bị Mạng

### Hubs / Hub
- Physical layer device / Thiết bị tầng vật lý
- Broadcasts to all ports / Phát tới tất cả cổng
- No intelligence / Không thông minh
- Half-duplex / Bán song công

### Switches / Switch
- Data link layer device / Thiết bị tầng liên kết dữ liệu
- MAC address learning / Học địa chỉ MAC
- Full-duplex / Song công
- VLAN support / Hỗ trợ VLAN

### Routers / Router
- Network layer device / Thiết bị tầng mạng
- IP packet forwarding / Chuyển tiếp gói IP
- Routing protocols / Giao thức định tuyến
- NAT support / Hỗ trợ NAT

### Firewalls / Tường Lửa
- Security device / Thiết bị bảo mật
- Packet filtering / Lọc gói
- Stateful inspection / Kiểm tra trạng thái
- Application layer filtering / Lọc tầng ứng dụng

## Network Tools / Công Cụ Mạng

### Command Line Tools / Công Cụ Dòng Lệnh
```bash
# Network configuration / Cấu hình mạng
ifconfig
ip addr
ip route

# Network testing / Kiểm tra mạng
ping
traceroute
mtr

# Network scanning / Quét mạng
nmap
netcat
telnet

# Network monitoring / Giám sát mạng
netstat
ss
iftop
```

### GUI Tools / Công Cụ Giao Diện
```
Wireshark - Packet analysis / Phân tích gói
Nmap - Network scanning / Quét mạng
Zenmap - Nmap GUI / Giao diện Nmap
Ettercap - Network analysis / Phân tích mạng
```

## Network Security / Bảo Mật Mạng

### Common Threats / Mối Đe Dọa Thường Gặp
```
- Man-in-the-middle / Tấn công trung gian
- ARP spoofing / Giả mạo ARP
- DNS poisoning / Đầu độc DNS
- Port scanning / Quét cổng
- Denial of Service / Từ chối dịch vụ
```

### Security Measures / Biện Pháp Bảo Mật
```
- Firewalls / Tường lửa
- IDS/IPS / Hệ thống phát hiện/xâm nhập
- VPN / Mạng riêng ảo
- Encryption / Mã hóa
- Access control / Kiểm soát truy cập
```

## Network Troubleshooting / Xử Lý Sự Cố Mạng

### Methodology / Phương Pháp
1. Identify problem / Xác định vấn đề
2. Gather information / Thu thập thông tin
3. Analyze data / Phân tích dữ liệu
4. Implement solution / Triển khai giải pháp
5. Verify fix / Xác minh sửa chữa

### Common Issues / Vấn Đề Thường Gặp
```
- Connectivity problems / Vấn đề kết nối
- DNS resolution / Phân giải DNS
- Routing issues / Vấn đề định tuyến
- Firewall blocks / Chặn tường lửa
- Bandwidth issues / Vấn đề băng thông
```

## Network Monitoring / Giám Sát Mạng

### Performance Metrics / Chỉ Số Hiệu Suất
```
- Bandwidth usage / Sử dụng băng thông
- Latency / Độ trễ
- Packet loss / Mất gói
- Error rates / Tỷ lệ lỗi
- Connection status / Trạng thái kết nối
```

### Monitoring Tools / Công Cụ Giám Sát
```
- SNMP / Giao thức quản lý mạng đơn giản
- NetFlow / Phân tích lưu lượng
- Syslog / Nhật ký hệ thống
- Monitoring software / Phần mềm giám sát
```

## Resources / Tài Nguyên
- RFC Documentation
- Network Protocol Guides
- Online Courses
- Community Forums 
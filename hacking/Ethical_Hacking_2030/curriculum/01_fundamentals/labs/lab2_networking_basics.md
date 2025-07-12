# Lab 2: Networking Fundamentals / Lab 2: Kiến Thức Cơ Bản Mạng

## Overview / Tổng Quan
This lab introduces fundamental networking concepts and tools. Students will learn about network protocols, IP addressing, and basic network troubleshooting.

Lab này giới thiệu các khái niệm và công cụ cơ bản về mạng. Học viên sẽ học về các giao thức mạng, địa chỉ IP và xử lý sự cố mạng cơ bản.

## Objectives / Mục Tiêu
- Understand TCP/IP protocol suite
- Learn IP addressing and subnetting
- Master basic networking tools
- Practice network troubleshooting

- Hiểu bộ giao thức TCP/IP
- Học về địa chỉ IP và chia mạng con
- Thành thạo các công cụ mạng cơ bản
- Thực hành xử lý sự cố mạng

## Prerequisites / Yêu Cầu Đầu Vào
- Linux virtual machine
- Network connectivity
- Basic understanding of networking
- Wireshark installed

- Máy ảo Linux
- Kết nối mạng
- Hiểu biết cơ bản về mạng
- Đã cài đặt Wireshark

## Lab Setup / Thiết Lập Lab
1. Start your Linux virtual machine
2. Open terminal
3. Create a working directory:
```bash
mkdir ~/networking_lab
cd ~/networking_lab
```

1. Khởi động máy ảo Linux
2. Mở terminal
3. Tạo thư mục làm việc:
```bash
mkdir ~/networking_lab
cd ~/networking_lab
```

## Exercises / Bài Tập

### Exercise 1: Network Configuration / Bài Tập 1: Cấu Hình Mạng
1. Check network interfaces:
```bash
ifconfig
ip addr
```

2. Configure network interface:
```bash
sudo ifconfig eth0 192.168.1.100 netmask 255.255.255.0
sudo ip addr add 192.168.1.100/24 dev eth0
```

3. Test connectivity:
```bash
ping 8.8.8.8
ping google.com
```

1. Kiểm tra giao diện mạng:
```bash
ifconfig
ip addr
```

2. Cấu hình giao diện mạng:
```bash
sudo ifconfig eth0 192.168.1.100 netmask 255.255.255.0
sudo ip addr add 192.168.1.100/24 dev eth0
```

3. Kiểm tra kết nối:
```bash
ping 8.8.8.8
ping google.com
```

### Exercise 2: Network Tools / Bài Tập 2: Công Cụ Mạng
1. Network scanning:
```bash
nmap localhost
nmap 192.168.1.0/24
```

2. Route tracing:
```bash
traceroute google.com
mtr google.com
```

3. DNS queries:
```bash
dig google.com
nslookup google.com
```

1. Quét mạng:
```bash
nmap localhost
nmap 192.168.1.0/24
```

2. Theo dõi tuyến đường:
```bash
traceroute google.com
mtr google.com
```

3. Truy vấn DNS:
```bash
dig google.com
nslookup google.com
```

### Exercise 3: Packet Analysis / Bài Tập 3: Phân Tích Gói Tin
1. Start Wireshark capture:
```bash
sudo wireshark
```

2. Filter packets:
```
tcp
http
dns
```

3. Analyze packets:
- TCP handshake
- HTTP requests
- DNS queries

1. Bắt đầu bắt gói tin Wireshark:
```bash
sudo wireshark
```

2. Lọc gói tin:
```
tcp
http
dns
```

3. Phân tích gói tin:
- Bắt tay TCP
- Yêu cầu HTTP
- Truy vấn DNS

### Exercise 4: Network Services / Bài Tập 4: Dịch Vụ Mạng
1. Check running services:
```bash
netstat -tuln
ss -tuln
```

2. Test web server:
```bash
curl http://localhost
wget http://localhost
```

3. Test FTP server:
```bash
ftp localhost
```

1. Kiểm tra dịch vụ đang chạy:
```bash
netstat -tuln
ss -tuln
```

2. Kiểm tra máy chủ web:
```bash
curl http://localhost
wget http://localhost
```

3. Kiểm tra máy chủ FTP:
```bash
ftp localhost
```

## Challenge / Thử Thách
Create a network monitoring script that:
1. Monitors network interfaces
2. Tracks active connections
3. Logs network events
4. Generates reports

Tạo một script giám sát mạng:
1. Giám sát giao diện mạng
2. Theo dõi kết nối đang hoạt động
3. Ghi log sự kiện mạng
4. Tạo báo cáo

## Submission / Nộp Bài
Submit the following:
1. Screenshots of completed exercises
2. Wireshark capture file
3. Network monitoring script
4. Lab report with findings

Nộp các nội dung sau:
1. Ảnh chụp màn hình các bài tập đã hoàn thành
2. File bắt gói tin Wireshark
3. Script giám sát mạng
4. Báo cáo lab với các phát hiện

## Resources / Tài Nguyên
- TCP/IP Protocol Suite
- Wireshark Documentation
- Network Administration Guide
- Linux Networking Cookbook

## Grading Criteria / Tiêu Chí Đánh Giá
- Exercise completion: 60%
- Challenge solution: 30%
- Documentation: 10%

- Hoàn thành bài tập: 60%
- Giải pháp thử thách: 30%
- Tài liệu: 10% 
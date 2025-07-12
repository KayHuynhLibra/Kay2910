# Linux Fundamentals - Phần 1: Linux Basics

## 1. Giới thiệu về Linux
- Lịch sử phát triển
- Kiến trúc hệ thống
- Các bản phân phối phổ biến
- So sánh với Windows

## 2. Hệ thống file
- Cấu trúc thư mục
- Quyền truy cập
- Liên kết (links)
- Mount points

## 3. Quản lý file và thư mục
```bash
# Tạo thư mục
mkdir my_directory

# Tạo file
touch my_file.txt

# Di chuyển file
mv source.txt destination.txt

# Sao chép file
cp source.txt destination.txt

# Xóa file
rm my_file.txt

# Xem nội dung file
cat my_file.txt
less my_file.txt
head -n 10 my_file.txt
tail -n 10 my_file.txt
```

## 4. Quản lý người dùng và nhóm
```bash
# Tạo người dùng mới
useradd newuser

# Đặt mật khẩu
passwd newuser

# Tạo nhóm mới
groupadd newgroup

# Thêm người dùng vào nhóm
usermod -aG newgroup newuser

# Xem thông tin người dùng
id newuser
```

## 5. Quản lý quyền truy cập
```bash
# Thay đổi quyền truy cập
chmod 755 my_file.txt
chmod u+x my_file.txt

# Thay đổi chủ sở hữu
chown newuser:newgroup my_file.txt

# Thay đổi quyền đệ quy
chmod -R 755 my_directory
```

## 6. Quản lý tiến trình
```bash
# Xem danh sách tiến trình
ps aux
top

# Dừng tiến trình
kill PID
killall process_name

# Chạy tiến trình trong nền
nohup command &

# Quản lý dịch vụ
systemctl start service_name
systemctl stop service_name
systemctl status service_name
```

## 7. Quản lý gói phần mềm
```bash
# Cập nhật danh sách gói
apt update

# Cài đặt gói mới
apt install package_name

# Gỡ cài đặt gói
apt remove package_name

# Tìm kiếm gói
apt search keyword
```

## 8. Mạng và bảo mật
```bash
# Kiểm tra kết nối mạng
ping google.com
netstat -tuln

# Cấu hình tường lửa
ufw enable
ufw allow 22/tcp

# Kiểm tra port
nmap localhost
```

## Bài tập thực hành
1. Tạo cấu trúc thư mục cho một dự án
2. Cấu hình quyền truy cập cho các file và thư mục
3. Tạo và quản lý người dùng
4. Cài đặt và cấu hình dịch vụ cơ bản

## Tài liệu tham khảo
- Linux Documentation Project
- Ubuntu Documentation
- Red Hat Enterprise Linux Documentation 
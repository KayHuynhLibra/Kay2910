# Bài tập 1: Các lệnh cơ bản

## Mục tiêu
- Làm quen với các lệnh cơ bản trong Linux
- Thực hành quản lý file và thư mục
- Thực hành quản lý người dùng và quyền truy cập

## Yêu cầu
1. Tạo cấu trúc thư mục sau:
```
~/devops-practice/
├── bin/
├── etc/
├── var/
│   ├── log/
│   └── www/
└── tmp/
```

2. Tạo các file sau:
- `~/devops-practice/etc/config.txt` với nội dung:
```
# Configuration file
APP_NAME=MyApp
DEBUG=true
PORT=8080
```

- `~/devops-practice/var/log/app.log` với nội dung:
```
[2024-03-15 10:00:00] INFO: Application started
[2024-03-15 10:01:00] INFO: User logged in
[2024-03-15 10:02:00] ERROR: Database connection failed
```

3. Tạo người dùng mới:
- Tên người dùng: `devops-user`
- Nhóm: `devops-group`
- Shell: `/bin/bash`
- Home directory: `/home/devops-user`

4. Cấu hình quyền truy cập:
- Thư mục `~/devops-practice`: rwxr-xr-x
- File `config.txt`: rw-r--r--
- File `app.log`: rw-r-----
- Thư mục `bin`: rwxr-x---
- Thư mục `tmp`: rwxrwxrwt

## Hướng dẫn
1. Sử dụng lệnh `mkdir` để tạo cấu trúc thư mục
2. Sử dụng lệnh `touch` và `echo` để tạo file
3. Sử dụng lệnh `useradd` và `groupadd` để tạo người dùng và nhóm
4. Sử dụng lệnh `chmod` và `chown` để cấu hình quyền truy cập

## Kiểm tra
1. Kiểm tra cấu trúc thư mục:
```bash
tree ~/devops-practice
```

2. Kiểm tra nội dung file:
```bash
cat ~/devops-practice/etc/config.txt
cat ~/devops-practice/var/log/app.log
```

3. Kiểm tra người dùng:
```bash
id devops-user
```

4. Kiểm tra quyền truy cập:
```bash
ls -l ~/devops-practice
ls -l ~/devops-practice/etc/config.txt
ls -l ~/devops-practice/var/log/app.log
```

## Gợi ý
- Sử dụng `man` để xem hướng dẫn sử dụng các lệnh
- Sử dụng `sudo` khi cần quyền root
- Sử dụng `|` để kết hợp các lệnh
- Sử dụng `>` và `>>` để ghi file

## Tài liệu tham khảo
- Linux Command Line and Shell Scripting Bible
- Linux System Administration Handbook
- Ubuntu Server Guide 
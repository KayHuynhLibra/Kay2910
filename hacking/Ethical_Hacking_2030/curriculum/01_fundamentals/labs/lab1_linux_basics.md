# Linux Basics Lab / Phòng Thí Nghiệm Linux Cơ Bản

## Overview / Tổng Quan
This lab introduces fundamental Linux concepts and commands through hands-on exercises. Students will learn file system navigation, file operations, permissions, and process management.

Phòng thí nghiệm này giới thiệu các khái niệm và lệnh Linux cơ bản thông qua các bài tập thực hành. Học viên sẽ học cách điều hướng hệ thống file, thao tác file, phân quyền và quản lý tiến trình.

## Objectives / Mục Tiêu
- Navigate the Linux file system / Điều hướng hệ thống file Linux
- Perform basic file operations / Thực hiện thao tác file cơ bản
- Manage file permissions / Quản lý phân quyền file
- Monitor and manage processes / Giám sát và quản lý tiến trình

## Prerequisites / Yêu Cầu Đầu Vào
- Linux virtual machine or system / Máy ảo hoặc hệ thống Linux
- Basic understanding of command line / Hiểu biết cơ bản về dòng lệnh
- Text editor (nano, vim) / Trình soạn thảo văn bản

## Lab Setup / Thiết Lập Phòng Thí Nghiệm

### Environment Setup / Thiết Lập Môi Trường
```bash
# Create lab directory / Tạo thư mục phòng thí nghiệm
mkdir -p ~/linux_lab
cd ~/linux_lab

# Create sample files / Tạo file mẫu
touch file1.txt file2.txt file3.txt
mkdir dir1 dir2 dir3
```

## Exercises / Bài Tập

### Exercise 1: File System Navigation / Bài Tập 1: Điều Hướng Hệ Thống File
```bash
# Current directory / Thư mục hiện tại
pwd

# List directory contents / Liệt kê nội dung thư mục
ls
ls -l
ls -a
ls -h

# Change directory / Thay đổi thư mục
cd dir1
cd ..
cd ~/linux_lab

# Create directory structure / Tạo cấu trúc thư mục
mkdir -p dir1/subdir1/subdir2
```

### Exercise 2: File Operations / Bài Tập 2: Thao Tác File
```bash
# Create files / Tạo file
touch newfile.txt
echo "Hello, World!" > hello.txt

# Copy files / Sao chép file
cp file1.txt file1_copy.txt
cp -r dir1 dir1_backup

# Move files / Di chuyển file
mv file2.txt dir1/
mv dir2 new_dir2

# Remove files / Xóa file
rm file3.txt
rm -r dir3
```

### Exercise 3: File Permissions / Bài Tập 3: Phân Quyền File
```bash
# Check permissions / Kiểm tra phân quyền
ls -l file1.txt

# Change permissions / Thay đổi phân quyền
chmod 644 file1.txt
chmod u+x file1.txt
chmod -R 755 dir1

# Change ownership / Thay đổi quyền sở hữu
sudo chown user:group file1.txt
sudo chown -R user:group dir1
```

### Exercise 4: Process Management / Bài Tập 4: Quản Lý Tiến Trình
```bash
# View processes / Xem tiến trình
ps
ps aux
top

# Background processes / Tiến trình nền
command &
jobs
fg %1
bg %1

# Kill processes / Kết thúc tiến trình
kill PID
kill -9 PID
```

## Challenge / Thử Thách
Create a script that:
1. Sets up a directory structure
2. Generates sample files with content
3. Sets appropriate permissions
4. Monitors system resources

Tạo một script:
1. Thiết lập cấu trúc thư mục
2. Tạo các file mẫu với nội dung
3. Đặt phân quyền phù hợp
4. Giám sát tài nguyên hệ thống

```bash
#!/bin/bash

# Create directory structure / Tạo cấu trúc thư mục
mkdir -p project/{src,doc,test}

# Generate sample files / Tạo file mẫu
echo "Source code" > project/src/main.py
echo "Documentation" > project/doc/README.md
echo "Test cases" > project/test/test.py

# Set permissions / Đặt phân quyền
chmod 755 project
chmod 644 project/src/main.py
chmod 644 project/doc/README.md
chmod 644 project/test/test.py

# Monitor resources / Giám sát tài nguyên
echo "System Resources:"
df -h
free -h
top -b -n 1
```

## Submission Requirements / Yêu Cầu Nộp Bài

### Required Files / File Yêu Cầu
1. Screenshots of completed exercises / Ảnh chụp màn hình các bài tập đã hoàn thành
2. Challenge script / Script thử thách
3. Lab report / Báo cáo phòng thí nghiệm

### Lab Report / Báo Cáo Phòng Thí Nghiệm
- Exercise results / Kết quả bài tập
- Challenges encountered / Thử thách gặp phải
- Solutions implemented / Giải pháp đã thực hiện
- Learning outcomes / Kết quả học tập

## Resources / Tài Nguyên
- Linux Documentation
- Command Line Reference
- File System Hierarchy
- Process Management Guide

## Grading Criteria / Tiêu Chí Chấm Điểm
- Exercise completion / Hoàn thành bài tập (40%)
- Challenge implementation / Thực hiện thử thách (30%)
- Lab report quality / Chất lượng báo cáo (20%)
- Understanding demonstrated / Thể hiện sự hiểu biết (10%) 
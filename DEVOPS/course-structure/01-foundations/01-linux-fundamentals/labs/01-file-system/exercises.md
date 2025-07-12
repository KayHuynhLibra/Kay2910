# Lab 1: File System Management

## Mục tiêu
- Hiểu và thực hành các lệnh quản lý file system
- Làm việc với permissions và ownership
- Tạo và quản lý symbolic links
- Thực hành với file operations

## Yêu cầu
- Hệ điều hành Linux (Ubuntu 20.04+)
- Terminal với quyền sudo
- Ổ cứng trống tối thiểu 1GB

## Bài tập

### 1. File System Navigation
```bash
# Tạo cấu trúc thư mục
mkdir -p ~/devops-lab/{bin,etc,var/{log,www},tmp}

# Di chuyển vào thư mục
cd ~/devops-lab

# Kiểm tra cấu trúc
tree
```

### 2. File Operations
```bash
# Tạo file
touch var/log/app.log
echo "Test log entry" > var/log/app.log

# Sao chép file
cp var/log/app.log var/log/app.log.backup

# Di chuyển file
mv var/log/app.log.backup var/log/backup/

# Xóa file
rm var/log/app.log
```

### 3. Permissions & Ownership
```bash
# Tạo user và group
sudo useradd -m devops_user
sudo groupadd devops_group
sudo usermod -aG devops_group devops_user

# Thay đổi ownership
sudo chown -R devops_user:devops_group ~/devops-lab

# Thay đổi permissions
chmod 755 ~/devops-lab
chmod 644 ~/devops-lab/var/log/app.log
chmod 750 ~/devops-lab/bin

# Kiểm tra permissions
ls -la ~/devops-lab
```

### 4. Symbolic Links
```bash
# Tạo symbolic link
ln -s ~/devops-lab/var/log/app.log ~/devops-lab/tmp/app.log.link

# Kiểm tra link
ls -l ~/devops-lab/tmp/app.log.link

# Xóa link
rm ~/devops-lab/tmp/app.log.link
```

### 5. File System Information
```bash
# Kiểm tra disk usage
df -h

# Kiểm tra inode usage
df -i

# Kiểm tra file system type
mount | grep "^/dev"

# Kiểm tra file system status
sudo fsck /dev/sda1
```

### 6. Advanced Operations
```bash
# Tìm file theo kích thước
find ~/devops-lab -type f -size +1M

# Tìm file theo thời gian
find ~/devops-lab -type f -mtime -7

# Tìm file theo permissions
find ~/devops-lab -type f -perm 644

# Tìm và xóa file cũ
find ~/devops-lab/tmp -type f -mtime +30 -delete
```

## Bài tập nâng cao

### 1. File System Monitoring Script
Tạo script để giám sát:
- Disk usage
- File system errors
- Large files
- Old files

```bash
#!/bin/bash
# monitor.sh

LOG_FILE="~/devops-lab/var/log/fs-monitor.log"
THRESHOLD=80

# Disk usage check
check_disk_usage() {
    local usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
    if [ $usage -gt $THRESHOLD ]; then
        echo "WARNING: Disk usage is $usage%" >> $LOG_FILE
    fi
}

# File system check
check_fs_errors() {
    sudo fsck -n /dev/sda1 >> $LOG_FILE 2>&1
}

# Large files check
find_large_files() {
    find / -type f -size +100M -exec ls -lh {} \; >> $LOG_FILE
}

# Old files check
find_old_files() {
    find / -type f -mtime +30 -exec ls -lh {} \; >> $LOG_FILE
}

# Main
check_disk_usage
check_fs_errors
find_large_files
find_old_files
```

### 2. Backup Script
Tạo script để backup:
- Quan trọng files
- Log files
- Configuration files

```bash
#!/bin/bash
# backup.sh

BACKUP_DIR="~/devops-lab/var/backup"
DATE=$(date +%Y%m%d)

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup important files
tar -czf $BACKUP_DIR/important-files-$DATE.tar.gz \
    ~/devops-lab/etc \
    ~/devops-lab/var/log

# Backup configuration
tar -czf $BACKUP_DIR/config-$DATE.tar.gz \
    ~/devops-lab/etc/*.conf

# Clean old backups
find $BACKUP_DIR -type f -mtime +7 -delete
```

## Kiểm tra

### Câu hỏi
1. Giải thích sự khác biệt giữa hard link và symbolic link
2. Mô tả các loại permissions trong Linux
3. Giải thích cách thay đổi ownership của file
4. Mô tả cách tìm và xóa file cũ

### Thực hành
1. Tạo cấu trúc thư mục cho một ứng dụng web
2. Cấu hình permissions phù hợp
3. Tạo backup script
4. Giám sát file system

## Tài liệu tham khảo
- Linux Documentation Project
- Ubuntu Documentation
- Arch Linux Wiki 
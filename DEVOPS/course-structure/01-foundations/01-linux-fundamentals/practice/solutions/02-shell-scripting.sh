#!/bin/bash

# Bài tập 2: Shell Scripting
# Tác giả: DevOps Team
# Ngày: 2024-03-15

# Tạo thư mục cho scripts
mkdir -p ~/devops-practice/bin

# 1. System Monitor Script
echo "1. Tạo System Monitor Script..."
cat > ~/devops-practice/bin/system-monitor.sh << 'EOF'
#!/bin/bash

# Configuration
LOG_FILE="/var/log/system-monitor.log"
ALERT_THRESHOLD=80

# Functions
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
}

check_cpu() {
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')
    if [ $(echo "$CPU_USAGE > $ALERT_THRESHOLD" | bc) -eq 1 ]; then
        log_message "WARNING: High CPU usage: $CPU_USAGE%"
    else
        log_message "INFO: CPU usage: $CPU_USAGE%"
    fi
}

check_memory() {
    MEM_USAGE=$(free | awk '/Mem:/ {print int($3/$2 * 100)}')
    if [ $MEM_USAGE -gt $ALERT_THRESHOLD ]; then
        log_message "WARNING: High memory usage: $MEM_USAGE%"
    else
        log_message "INFO: Memory usage: $MEM_USAGE%"
    fi
}

check_disk() {
    DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
    if [ $DISK_USAGE -gt $ALERT_THRESHOLD ]; then
        log_message "WARNING: High disk usage: $DISK_USAGE%"
    else
        log_message "INFO: Disk usage: $DISK_USAGE%"
    fi
}

check_network() {
    if ping -c 1 8.8.8.8 >/dev/null 2>&1; then
        log_message "INFO: Network connectivity OK"
    else
        log_message "ERROR: Network connectivity failed"
    fi
}

# Main
while true; do
    check_cpu
    check_memory
    check_disk
    check_network
    sleep 300
done
EOF

# 2. Backup Script
echo "2. Tạo Backup Script..."
cat > ~/devops-practice/bin/backup.sh << 'EOF'
#!/bin/bash

# Configuration
BACKUP_DIR="/var/backups"
LOG_FILE="/var/log/backup.log"
RETENTION_DAYS=7

# Functions
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
}

backup_directory() {
    local source_dir=$1
    local backup_name=$(basename $source_dir)
    local timestamp=$(date +%Y%m%d_%H%M%S)
    local backup_file="$BACKUP_DIR/${backup_name}_${timestamp}.tar.gz"

    if [ ! -d "$source_dir" ]; then
        log_message "ERROR: Source directory $source_dir does not exist"
        return 1
    fi

    tar -czf "$backup_file" "$source_dir"
    if [ $? -eq 0 ]; then
        log_message "INFO: Backup created: $backup_file"
    else
        log_message "ERROR: Backup failed for $source_dir"
        return 1
    fi
}

cleanup_old_backups() {
    find "$BACKUP_DIR" -type f -mtime +$RETENTION_DAYS -delete
    log_message "INFO: Cleaned up backups older than $RETENTION_DAYS days"
}

# Main
if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory_to_backup>"
    exit 1
fi

backup_directory "$1"
cleanup_old_backups
EOF

# 3. User Manager Script
echo "3. Tạo User Manager Script..."
cat > ~/devops-practice/bin/user-manager.sh << 'EOF'
#!/bin/bash

# Configuration
LOG_FILE="/var/log/user-manager.log"

# Functions
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> $LOG_FILE
}

create_user() {
    local username=$1
    local group=$2

    if id "$username" &>/dev/null; then
        log_message "ERROR: User $username already exists"
        return 1
    fi

    useradd -m -s /bin/bash "$username"
    if [ $? -eq 0 ]; then
        if [ ! -z "$group" ]; then
            usermod -aG "$group" "$username"
        fi
        log_message "INFO: Created user $username"
    else
        log_message "ERROR: Failed to create user $username"
        return 1
    fi
}

delete_user() {
    local username=$1

    if ! id "$username" &>/dev/null; then
        log_message "ERROR: User $username does not exist"
        return 1
    fi

    userdel -r "$username"
    if [ $? -eq 0 ]; then
        log_message "INFO: Deleted user $username"
    else
        log_message "ERROR: Failed to delete user $username"
        return 1
    fi
}

list_users() {
    echo "System Users:"
    cat /etc/passwd | cut -d: -f1,3,4,7
}

# Main
case "$1" in
    "create")
        if [ $# -lt 2 ]; then
            echo "Usage: $0 create <username> [group]"
            exit 1
        fi
        create_user "$2" "$3"
        ;;
    "delete")
        if [ $# -lt 2 ]; then
            echo "Usage: $0 delete <username>"
            exit 1
        fi
        delete_user "$2"
        ;;
    "list")
        list_users
        ;;
    *)
        echo "Usage: $0 {create|delete|list}"
        exit 1
        ;;
esac
EOF

# Cấp quyền thực thi
echo "4. Cấp quyền thực thi..."
chmod +x ~/devops-practice/bin/*.sh

# Tạo thư mục log
echo "5. Tạo thư mục log..."
sudo mkdir -p /var/log
sudo touch /var/log/system-monitor.log
sudo touch /var/log/backup.log
sudo touch /var/log/user-manager.log
sudo chown -R $USER:$USER /var/log/system-monitor.log
sudo chown -R $USER:$USER /var/log/backup.log
sudo chown -R $USER:$USER /var/log/user-manager.log

# Tạo thư mục backup
echo "6. Tạo thư mục backup..."
sudo mkdir -p /var/backups
sudo chown -R $USER:$USER /var/backups

# Kiểm tra scripts
echo "7. Kiểm tra scripts..."
echo "System Monitor Script:"
head -n 5 ~/devops-practice/bin/system-monitor.sh

echo "Backup Script:"
head -n 5 ~/devops-practice/bin/backup.sh

echo "User Manager Script:"
head -n 5 ~/devops-practice/bin/user-manager.sh

echo "Hoàn thành!" 
# Linux Commands Cheatsheet

## File System Commands
```bash
# Navigation
cd          # Change directory
pwd         # Print working directory
ls          # List files
ls -la      # List all files with details
ls -lh      # List files with human-readable sizes

# File Operations
cp          # Copy files
mv          # Move files
rm          # Remove files
mkdir       # Create directory
rmdir       # Remove directory
touch       # Create empty file

# File Permissions
chmod       # Change file permissions
chown       # Change file owner
chgrp       # Change file group
```

## Text Processing
```bash
# Viewing Files
cat         # Display file content
less        # View file page by page
head        # Display first lines
tail        # Display last lines
grep        # Search text in files

# Text Editors
nano        # Simple text editor
vim         # Advanced text editor
```

## System Information
```bash
# System Info
uname -a    # System information
df -h       # Disk space usage
free -h     # Memory usage
top         # Process information
ps          # Process status
```

## User Management
```bash
# User Commands
useradd     # Add user
userdel     # Delete user
passwd      # Change password
usermod     # Modify user
groups      # List groups
```

## Network Commands
```bash
# Network
ifconfig    # Network interface configuration
ping        # Test network connectivity
netstat     # Network statistics
ssh         # Secure shell
scp         # Secure copy
```

## Package Management
```bash
# Debian/Ubuntu
apt update          # Update package list
apt upgrade         # Upgrade packages
apt install         # Install package
apt remove          # Remove package
apt search          # Search packages

# Red Hat/CentOS
yum update          # Update packages
yum install         # Install package
yum remove          # Remove package
yum search          # Search packages
```

## Process Management
```bash
# Process Control
ps          # List processes
kill        # Kill process
killall     # Kill processes by name
bg          # Run process in background
fg          # Bring process to foreground
```

## System Control
```bash
# System Control
shutdown    # Shutdown system
reboot      # Reboot system
halt        # Halt system
poweroff    # Power off system
```

## File Permissions
```bash
# Permission Types
r           # Read (4)
w           # Write (2)
x           # Execute (1)

# Examples
chmod 755   # rwxr-xr-x
chmod 644   # rw-r--r--
chmod 777   # rwxrwxrwx
```

## Common Options
```bash
-h          # Human-readable
-a          # All
-l          # Long format
-r          # Recursive
-f          # Force
-v          # Verbose
```

## Tips & Tricks
1. Use `man` command to view manual pages
2. Use `--help` for command help
3. Use `history` to view command history
4. Use `!!` to repeat last command
5. Use `Ctrl+R` to search command history 
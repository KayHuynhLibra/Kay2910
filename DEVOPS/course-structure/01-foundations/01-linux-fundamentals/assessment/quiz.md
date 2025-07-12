# Linux Fundamentals Quiz

## Multiple Choice Questions

1. Which command is used to change file permissions in Linux?
   a) chown
   b) chmod
   c) chgrp
   d) chattr

2. What does the permission 755 mean for a file?
   a) Owner: rwx, Group: rwx, Others: rwx
   b) Owner: rwx, Group: r-x, Others: r-x
   c) Owner: rwx, Group: rwx, Others: r-x
   d) Owner: rwx, Group: r-x, Others: rwx

3. Which signal is used to forcefully terminate a process?
   a) SIGTERM (15)
   b) SIGKILL (9)
   c) SIGSTOP
   d) SIGCONT

4. What command is used to view real-time process information?
   a) ps
   b) top
   c) ls
   d) cat

5. Which directory contains system configuration files?
   a) /bin
   b) /etc
   c) /var
   d) /tmp

6. What command is used to check disk space usage?
   a) du
   b) df
   c) ls
   d) cat

7. Which command is used to check network connectivity?
   a) netstat
   b) ping
   c) ifconfig
   d) route

8. What is the purpose of the `cron` daemon?
   a) Process management
   b) Network configuration
   c) Scheduled task execution
   d) File system management

## Practical Questions

1. Write a command to find all files larger than 100MB in the /var directory.

2. Create a shell script that:
   - Monitors CPU usage
   - Sends an email alert if usage exceeds 80%
   - Logs the alert to a file

3. Write a command to check the last 10 lines of the system log file.

4. Create a systemd service file for a custom application that:
   - Starts after network
   - Restarts on failure
   - Runs as a specific user

## Scenario-based Questions

1. A server is experiencing high CPU usage. Describe the steps you would take to:
   - Identify the cause
   - Resolve the issue
   - Prevent future occurrences

2. A critical application is not starting. The error log shows permission issues. What steps would you take to:
   - Diagnose the problem
   - Fix the permissions
   - Verify the solution

3. A server's disk space is filling up rapidly. Describe your approach to:
   - Identify large files
   - Clean up unnecessary files
   - Implement monitoring to prevent future issues

## Answers

### Multiple Choice
1. b) chmod
2. b) Owner: rwx, Group: r-x, Others: r-x
3. b) SIGKILL (9)
4. b) top
5. b) /etc
6. b) df
7. b) ping
8. c) Scheduled task execution

### Practical Questions
1. ```bash
   find /var -type f -size +100M
   ```

2. ```bash
   #!/bin/bash
   CPU_THRESHOLD=80
   LOG_FILE="/var/log/cpu_alert.log"
   EMAIL="admin@example.com"

   while true; do
       CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')
       if [ $(echo "$CPU_USAGE > $CPU_THRESHOLD" | bc) -eq 1 ]; then
           echo "$(date): CPU usage is $CPU_USAGE%" >> $LOG_FILE
           echo "High CPU usage alert: $CPU_USAGE%" | mail -s "CPU Alert" $EMAIL
       fi
       sleep 300
   done
   ```

3. ```bash
   tail -n 10 /var/log/syslog
   ```

4. ```ini
   [Unit]
   Description=Custom Application
   After=network.target

   [Service]
   Type=simple
   User=appuser
   ExecStart=/usr/local/bin/app
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

### Scenario-based Questions
1. High CPU Usage:
   - Use `top` or `htop` to identify processes
   - Check process details with `ps aux | grep <PID>`
   - Analyze system load with `uptime`
   - Implement monitoring and alerts
   - Set up resource limits
   - Optimize application code if necessary

2. Permission Issues:
   - Check application logs
   - Verify file permissions with `ls -l`
   - Check user permissions with `id`
   - Fix permissions with `chmod` and `chown`
   - Test application startup
   - Document permission requirements

3. Disk Space Issues:
   - Use `df -h` to check disk usage
   - Find large files with `find / -type f -size +100M`
   - Clean package cache
   - Implement log rotation
   - Set up disk space monitoring
   - Create cleanup scripts
   - Document cleanup procedures 
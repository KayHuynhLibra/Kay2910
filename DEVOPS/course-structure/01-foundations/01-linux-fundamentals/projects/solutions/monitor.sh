#!/bin/bash

# System Monitor Script
# A comprehensive system monitoring tool

# Configuration
CONFIG_DIR="/opt/system-monitor/etc"
LOG_DIR="/opt/system-monitor/var/log"
REPORT_DIR="/opt/system-monitor/var/reports/daily"
TMP_DIR="/opt/system-monitor/tmp"

# Load configuration
source "$CONFIG_DIR/thresholds.conf"

# Logging functions
log_message() {
    local level=$1
    local message=$2
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$level] $message" >> "$LOG_DIR/system.log"
}

log_alert() {
    local level=$1
    local message=$2
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$level] $message" >> "$LOG_DIR/alerts.log"
    # Trigger alert script
    "$CONFIG_DIR/alert.sh" "$level" "$message"
}

# Resource monitoring functions
check_cpu() {
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')
    if [ $(echo "$cpu_usage > $CPU_THRESHOLD" | bc) -eq 1 ]; then
        log_alert "WARNING" "High CPU usage: $cpu_usage%"
    else
        log_message "INFO" "CPU usage: $cpu_usage%"
    fi
}

check_memory() {
    local mem_usage=$(free | awk '/Mem:/ {print int($3/$2 * 100)}')
    if [ $mem_usage -gt $MEMORY_THRESHOLD ]; then
        log_alert "WARNING" "High memory usage: $mem_usage%"
    else
        log_message "INFO" "Memory usage: $mem_usage%"
    fi
}

check_disk() {
    local disk_usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
    if [ $disk_usage -gt $DISK_THRESHOLD ]; then
        log_alert "WARNING" "High disk usage: $disk_usage%"
    else
        log_message "INFO" "Disk usage: $disk_usage%"
    fi
}

check_network() {
    if ping -c 1 8.8.8.8 >/dev/null 2>&1; then
        log_message "INFO" "Network connectivity: OK"
    else
        log_alert "ERROR" "Network connectivity: Failed"
    fi
}

check_processes() {
    local high_cpu_processes=$(ps aux | sort -nrk 3,3 | head -n 5)
    log_message "INFO" "Top 5 CPU consuming processes:\n$high_cpu_processes"
}

# Report generation
generate_report() {
    local report_file="$REPORT_DIR/system-report-$(date +%Y%m%d).html"
    
    echo "<html><body>" > $report_file
    echo "<h1>System Report - $(date)</h1>" >> $report_file
    
    # System Information
    echo "<h2>System Information</h2>" >> $report_file
    echo "<pre>" >> $report_file
    uname -a >> $report_file
    echo "</pre>" >> $report_file
    
    # Resource Usage
    echo "<h2>Resource Usage</h2>" >> $report_file
    echo "<h3>CPU Usage</h3>" >> $report_file
    top -bn1 | grep "Cpu(s)" >> $report_file
    
    echo "<h3>Memory Usage</h3>" >> $report_file
    free -h >> $report_file
    
    echo "<h3>Disk Usage</h3>" >> $report_file
    df -h >> $report_file
    
    # Recent Log Entries
    echo "<h2>Recent Log Entries</h2>" >> $report_file
    echo "<pre>" >> $report_file
    tail -n 20 "$LOG_DIR/system.log" >> $report_file
    echo "</pre>" >> $report_file
    
    # Recent Alerts
    echo "<h2>Recent Alerts</h2>" >> $report_file
    echo "<pre>" >> $report_file
    tail -n 20 "$LOG_DIR/alerts.log" >> $report_file
    echo "</pre>" >> $report_file
    
    echo "</body></html>" >> $report_file
}

# Main monitoring loop
main() {
    # Create necessary directories
    mkdir -p "$LOG_DIR" "$REPORT_DIR" "$TMP_DIR"
    
    # Initial log message
    log_message "INFO" "System monitor started"
    
    # Main loop
    while true; do
        check_cpu
        check_memory
        check_disk
        check_network
        check_processes
        
        # Generate daily report at midnight
        if [ "$(date +%H:%M)" = "00:00" ]; then
            generate_report
        fi
        
        sleep $MONITOR_INTERVAL
    done
}

# Error handling
handle_error() {
    local error_msg=$1
    log_alert "ERROR" "Critical error: $error_msg"
    exit 1
}

# Set up error handling
trap 'handle_error "Unexpected error occurred"' ERR

# Start monitoring
main 
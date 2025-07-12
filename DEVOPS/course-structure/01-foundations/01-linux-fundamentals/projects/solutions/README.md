# System Monitoring Tool

A comprehensive system monitoring tool that combines file system operations, process management, networking, and automation skills.

## Features

- Real-time system resource monitoring (CPU, Memory, Disk)
- Network connectivity tracking
- Process monitoring and management
- Automated alert system with escalation
- Daily HTML reports
- Multiple notification channels (Email, Slack, SMS)
- Configurable thresholds and intervals
- Systemd service integration

## Requirements

- Linux operating system
- Systemd
- Basic system utilities (top, free, df, etc.)
- Mail utilities (for email notifications)
- curl (for Slack notifications)
- bc (for calculations)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/system-monitor.git
   cd system-monitor
   ```

2. Run the installation script:
   ```bash
   sudo ./install.sh
   ```

The installation script will:
- Create necessary directories
- Copy files to appropriate locations
- Install dependencies
- Configure and start the systemd service

## Configuration

The main configuration file is located at `/opt/system-monitor/etc/thresholds.conf`. You can modify:

- Resource usage thresholds
- Monitoring intervals
- Alert settings
- Notification preferences
- Log and report settings

Example configuration:
```bash
# Resource Usage Thresholds
CPU_THRESHOLD=80
MEMORY_THRESHOLD=85
DISK_THRESHOLD=90

# Monitoring Intervals
MONITOR_INTERVAL=300  # 5 minutes
```

## Usage

### Starting the Service

```bash
sudo systemctl start system-monitor
```

### Stopping the Service

```bash
sudo systemctl stop system-monitor
```

### Checking Status

```bash
sudo systemctl status system-monitor
```

### Viewing Logs

```bash
# System logs
tail -f /opt/system-monitor/var/log/system.log

# Alert logs
tail -f /opt/system-monitor/var/log/alerts.log
```

### Viewing Reports

Daily reports are generated in HTML format and stored in `/opt/system-monitor/var/reports/daily/`.

## Alert System

The alert system supports multiple notification channels:

### Email Alerts

Configure in `thresholds.conf`:
```bash
ALERT_EMAIL="admin@example.com"
ALERT_SMTP_SERVER="smtp.example.com"
ALERT_SMTP_PORT=587
```

### Slack Alerts

Configure in `thresholds.conf`:
```bash
ENABLE_SLACK_NOTIFICATIONS=true
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/your/webhook/url"
```

### SMS Alerts

Configure in `thresholds.conf`:
```bash
ENABLE_SMS_NOTIFICATIONS=true
```

## Alert Levels

- WARNING: Non-critical issues that require attention
- ERROR: Issues that need immediate attention
- CRITICAL: Severe issues that require immediate action

## Escalation Rules

- WARNING → ERROR: After 3 occurrences
- ERROR → CRITICAL: After 5 occurrences

## Maintenance

### Log Rotation

Logs are automatically rotated based on size and age. Configure in `thresholds.conf`:
```bash
LOG_RETENTION_DAYS=30
LOG_MAX_SIZE_MB=100
```

### Report Retention

Reports are retained for a configurable period. Configure in `thresholds.conf`:
```bash
REPORT_RETENTION_DAYS=90
```

## Troubleshooting

### Common Issues

1. Service not starting
   - Check systemd logs: `journalctl -u system-monitor`
   - Verify permissions: `ls -l /opt/system-monitor/bin/`

2. Alerts not being sent
   - Check SMTP configuration
   - Verify network connectivity
   - Check alert logs

3. High resource usage
   - Adjust monitoring intervals
   - Review process list
   - Check for resource leaks

### Log Files

- System logs: `/opt/system-monitor/var/log/system.log`
- Alert logs: `/opt/system-monitor/var/log/alerts.log`
- Systemd logs: `journalctl -u system-monitor`

## Security Considerations

- The service runs as root (required for system monitoring)
- Security measures implemented:
  - NoNewPrivileges
  - ProtectSystem
  - ProtectHome
  - PrivateTmp
  - Resource limits

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Linux Documentation Project
- Systemd Documentation
- Bash Guide 
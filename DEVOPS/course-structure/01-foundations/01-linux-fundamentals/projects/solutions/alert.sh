#!/bin/bash

# Alert Script for System Monitor
# Handles notifications for system alerts

# Load configuration
source "$(dirname "$0")/../etc/thresholds.conf"

# Log file
ALERT_LOG="/opt/system-monitor/var/log/alerts.log"

# Log alert
log_alert() {
    local level=$1
    local message=$2
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$level] $message" >> "$ALERT_LOG"
}

# Send email alert
send_email_alert() {
    local level=$1
    local message=$2
    local subject="System Alert: $level - $(hostname)"
    
    if [ "$ENABLE_EMAIL_NOTIFICATIONS" = true ]; then
        echo "$message" | mail -s "$subject" \
            -S "smtp=$ALERT_SMTP_SERVER:$ALERT_SMTP_PORT" \
            -S "smtp-use-starttls" \
            -S "smtp-auth=login" \
            -S "smtp-auth-user=$ALERT_SMTP_USER" \
            -S "smtp-auth-password=$ALERT_SMTP_PASSWORD" \
            "$ALERT_EMAIL"
    fi
}

# Send Slack alert
send_slack_alert() {
    local level=$1
    local message=$2
    
    if [ "$ENABLE_SLACK_NOTIFICATIONS" = true ]; then
        curl -X POST -H 'Content-type: application/json' \
            --data "{
                \"text\": \"*System Alert: $level*\nHost: $(hostname)\nMessage: $message\"
            }" \
            "$SLACK_WEBHOOK_URL"
    fi
}

# Send SMS alert
send_sms_alert() {
    local level=$1
    local message=$2
    
    if [ "$ENABLE_SMS_NOTIFICATIONS" = true ]; then
        # Implement SMS sending logic here
        # This is a placeholder for SMS integration
        echo "SMS Alert: $level - $message"
    fi
}

# Handle alert escalation
handle_escalation() {
    local level=$1
    local message=$2
    local count=$3
    
    # Escalation rules
    case $level in
        "WARNING")
            if [ $count -ge 3 ]; then
                level="ERROR"
            fi
            ;;
        "ERROR")
            if [ $count -ge 5 ]; then
                level="CRITICAL"
            fi
            ;;
        "CRITICAL")
            # Implement critical alert handling
            # e.g., wake up on-call engineer
            ;;
    esac
    
    echo "$level"
}

# Main alert handling
main() {
    local level=$1
    local message=$2
    
    # Log the alert
    log_alert "$level" "$message"
    
    # Get alert count for this type
    local alert_count=$(grep -c "$message" "$ALERT_LOG")
    
    # Handle escalation
    level=$(handle_escalation "$level" "$message" "$alert_count")
    
    # Send notifications
    send_email_alert "$level" "$message"
    send_slack_alert "$level" "$message"
    send_sms_alert "$level" "$message"
    
    # Additional actions based on alert level
    case $level in
        "CRITICAL")
            # Implement critical alert actions
            # e.g., create incident ticket, page on-call
            ;;
        "ERROR")
            # Implement error alert actions
            # e.g., create support ticket
            ;;
        "WARNING")
            # Implement warning alert actions
            # e.g., log for review
            ;;
    esac
}

# Error handling
handle_error() {
    local error_msg=$1
    echo "Error in alert script: $error_msg" >> "$ALERT_LOG"
    exit 1
}

# Set up error handling
trap 'handle_error "Unexpected error occurred"' ERR

# Check if arguments are provided
if [ $# -lt 2 ]; then
    echo "Usage: $0 <level> <message>"
    exit 1
fi

# Start alert handling
main "$1" "$2" 
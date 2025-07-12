#!/bin/bash

# System Monitor Installation Script

# Configuration
INSTALL_DIR="/opt/system-monitor"
BIN_DIR="$INSTALL_DIR/bin"
ETC_DIR="$INSTALL_DIR/etc"
VAR_DIR="$INSTALL_DIR/var"
LOG_DIR="$VAR_DIR/log"
REPORT_DIR="$VAR_DIR/reports/daily"
TMP_DIR="$INSTALL_DIR/tmp"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Print status message
print_status() {
    local message=$1
    echo -e "${GREEN}[+]${NC} $message"
}

# Print error message
print_error() {
    local message=$1
    echo -e "${RED}[-]${NC} $message"
}

# Print warning message
print_warning() {
    local message=$1
    echo -e "${YELLOW}[!]${NC} $message"
}

# Check if running as root
check_root() {
    if [ "$EUID" -ne 0 ]; then
        print_error "Please run as root"
        exit 1
    fi
}

# Create directory structure
create_directories() {
    print_status "Creating directory structure..."
    
    mkdir -p "$BIN_DIR" "$ETC_DIR" "$LOG_DIR" "$REPORT_DIR" "$TMP_DIR"
    
    if [ $? -eq 0 ]; then
        print_status "Directory structure created successfully"
    else
        print_error "Failed to create directory structure"
        exit 1
    fi
}

# Copy files
copy_files() {
    print_status "Copying files..."
    
    # Copy scripts
    cp monitor.sh "$BIN_DIR/"
    cp alert.sh "$BIN_DIR/"
    cp thresholds.conf "$ETC_DIR/"
    cp system-monitor.service /etc/systemd/system/
    
    # Set permissions
    chmod +x "$BIN_DIR/monitor.sh"
    chmod +x "$BIN_DIR/alert.sh"
    chmod 644 "$ETC_DIR/thresholds.conf"
    chmod 644 /etc/systemd/system/system-monitor.service
    
    if [ $? -eq 0 ]; then
        print_status "Files copied successfully"
    else
        print_error "Failed to copy files"
        exit 1
    fi
}

# Install dependencies
install_dependencies() {
    print_status "Installing dependencies..."
    
    # Check package manager
    if command -v apt-get &> /dev/null; then
        apt-get update
        apt-get install -y mailutils curl bc
    elif command -v yum &> /dev/null; then
        yum install -y mailx curl bc
    else
        print_error "Unsupported package manager"
        exit 1
    fi
    
    if [ $? -eq 0 ]; then
        print_status "Dependencies installed successfully"
    else
        print_error "Failed to install dependencies"
        exit 1
    fi
}

# Configure systemd service
configure_service() {
    print_status "Configuring systemd service..."
    
    systemctl daemon-reload
    systemctl enable system-monitor
    systemctl start system-monitor
    
    if [ $? -eq 0 ]; then
        print_status "Service configured successfully"
    else
        print_error "Failed to configure service"
        exit 1
    fi
}

# Verify installation
verify_installation() {
    print_status "Verifying installation..."
    
    # Check if service is running
    if systemctl is-active --quiet system-monitor; then
        print_status "Service is running"
    else
        print_error "Service is not running"
        exit 1
    fi
    
    # Check if log file is being created
    sleep 5
    if [ -f "$LOG_DIR/system.log" ]; then
        print_status "Log file is being created"
    else
        print_error "Log file is not being created"
        exit 1
    fi
}

# Main installation process
main() {
    print_status "Starting installation..."
    
    # Check root privileges
    check_root
    
    # Create directories
    create_directories
    
    # Copy files
    copy_files
    
    # Install dependencies
    install_dependencies
    
    # Configure service
    configure_service
    
    # Verify installation
    verify_installation
    
    print_status "Installation completed successfully"
    print_status "System monitor is now running"
    print_status "Logs can be found in $LOG_DIR"
    print_status "Reports can be found in $REPORT_DIR"
}

# Error handling
handle_error() {
    local error_msg=$1
    print_error "Installation failed: $error_msg"
    exit 1
}

# Set up error handling
trap 'handle_error "Unexpected error occurred"' ERR

# Start installation
main 
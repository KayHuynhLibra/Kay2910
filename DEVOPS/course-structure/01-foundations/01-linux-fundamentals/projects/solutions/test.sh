#!/bin/bash

# System Monitor Test Script

# Configuration
TEST_DIR="/tmp/system-monitor-test"
LOG_FILE="$TEST_DIR/test.log"
ALERT_LOG="$TEST_DIR/alerts.log"

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

# Create test environment
setup_test_env() {
    print_status "Setting up test environment..."
    
    # Create test directory
    mkdir -p "$TEST_DIR"
    
    # Create test configuration
    cat > "$TEST_DIR/thresholds.conf" << EOF
CPU_THRESHOLD=80
MEMORY_THRESHOLD=85
DISK_THRESHOLD=90
MONITOR_INTERVAL=1
ENABLE_EMAIL_NOTIFICATIONS=false
ENABLE_SLACK_NOTIFICATIONS=false
ENABLE_SMS_NOTIFICATIONS=false
EOF
    
    # Create test log files
    touch "$LOG_FILE"
    touch "$ALERT_LOG"
}

# Test CPU monitoring
test_cpu_monitoring() {
    print_status "Testing CPU monitoring..."
    
    # Simulate high CPU usage
    dd if=/dev/zero of=/dev/null &
    local dd_pid=$!
    
    # Run monitor script
    ./monitor.sh &
    local monitor_pid=$!
    
    # Wait for monitoring
    sleep 5
    
    # Check logs
    if grep -q "High CPU usage" "$LOG_FILE"; then
        print_status "CPU monitoring test passed"
    else
        print_error "CPU monitoring test failed"
    fi
    
    # Cleanup
    kill $dd_pid
    kill $monitor_pid
}

# Test memory monitoring
test_memory_monitoring() {
    print_status "Testing memory monitoring..."
    
    # Simulate high memory usage
    stress-ng --vm 1 --vm-bytes 1G &
    local stress_pid=$!
    
    # Run monitor script
    ./monitor.sh &
    local monitor_pid=$!
    
    # Wait for monitoring
    sleep 5
    
    # Check logs
    if grep -q "High memory usage" "$LOG_FILE"; then
        print_status "Memory monitoring test passed"
    else
        print_error "Memory monitoring test failed"
    fi
    
    # Cleanup
    kill $stress_pid
    kill $monitor_pid
}

# Test disk monitoring
test_disk_monitoring() {
    print_status "Testing disk monitoring..."
    
    # Create large file
    dd if=/dev/zero of="$TEST_DIR/large_file" bs=1M count=1000
    
    # Run monitor script
    ./monitor.sh &
    local monitor_pid=$!
    
    # Wait for monitoring
    sleep 5
    
    # Check logs
    if grep -q "High disk usage" "$LOG_FILE"; then
        print_status "Disk monitoring test passed"
    else
        print_error "Disk monitoring test failed"
    fi
    
    # Cleanup
    rm "$TEST_DIR/large_file"
    kill $monitor_pid
}

# Test network monitoring
test_network_monitoring() {
    print_status "Testing network monitoring..."
    
    # Run monitor script
    ./monitor.sh &
    local monitor_pid=$!
    
    # Wait for monitoring
    sleep 5
    
    # Check logs
    if grep -q "Network connectivity" "$LOG_FILE"; then
        print_status "Network monitoring test passed"
    else
        print_error "Network monitoring test failed"
    fi
    
    # Cleanup
    kill $monitor_pid
}

# Test alert system
test_alert_system() {
    print_status "Testing alert system..."
    
    # Trigger an alert
    ./alert.sh "WARNING" "Test alert message"
    
    # Check alert log
    if grep -q "Test alert message" "$ALERT_LOG"; then
        print_status "Alert system test passed"
    else
        print_error "Alert system test failed"
    fi
}

# Test report generation
test_report_generation() {
    print_status "Testing report generation..."
    
    # Generate report
    ./monitor.sh --generate-report
    
    # Check if report exists
    if [ -f "$TEST_DIR/reports/daily/system-report-$(date +%Y%m%d).html" ]; then
        print_status "Report generation test passed"
    else
        print_error "Report generation test failed"
    fi
}

# Cleanup test environment
cleanup() {
    print_status "Cleaning up test environment..."
    
    # Kill any remaining processes
    pkill -f "monitor.sh"
    
    # Remove test directory
    rm -rf "$TEST_DIR"
}

# Main test process
main() {
    print_status "Starting tests..."
    
    # Setup test environment
    setup_test_env
    
    # Run tests
    test_cpu_monitoring
    test_memory_monitoring
    test_disk_monitoring
    test_network_monitoring
    test_alert_system
    test_report_generation
    
    # Cleanup
    cleanup
    
    print_status "All tests completed"
}

# Error handling
handle_error() {
    local error_msg=$1
    print_error "Test failed: $error_msg"
    cleanup
    exit 1
}

# Set up error handling
trap 'handle_error "Unexpected error occurred"' ERR

# Start tests
main 
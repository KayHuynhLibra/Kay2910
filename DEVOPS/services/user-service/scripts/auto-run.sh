#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Configuration
LOG_FILE="auto-run.log"
ALERT_THRESHOLD=80
CHECK_INTERVAL=300  # 5 minutes

# Logging function
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a $LOG_FILE
}

# Check system resources
check_resources() {
    # Check disk usage
    local disk_usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
    if [ $disk_usage -gt $ALERT_THRESHOLD ]; then
        log_message "${YELLOW}WARNING: Disk usage is $disk_usage%${NC}"
    fi

    # Check memory usage
    local memory_usage=$(free | awk '/Mem:/ {print int($3/$2 * 100)}')
    if [ $memory_usage -gt $ALERT_THRESHOLD ]; then
        log_message "${YELLOW}WARNING: Memory usage is $memory_usage%${NC}"
    fi
}

# Check service health
check_service_health() {
    # Check if containers are running
    if ! docker-compose ps | grep -q "Up"; then
        log_message "${RED}ERROR: Some containers are not running${NC}"
        docker-compose ps
        return 1
    fi

    # Check API health endpoint
    if ! curl -s http://localhost:3000/health | grep -q "ok"; then
        log_message "${RED}ERROR: Health check failed${NC}"
        return 1
    fi

    # Check database connection
    if ! docker-compose exec postgres pg_isready -U postgres > /dev/null 2>&1; then
        log_message "${RED}ERROR: Database connection failed${NC}"
        return 1
    fi

    # Check Redis connection
    if ! docker-compose exec redis redis-cli ping > /dev/null 2>&1; then
        log_message "${RED}ERROR: Redis connection failed${NC}"
        return 1
    fi

    log_message "${GREEN}Service health check passed${NC}"
    return 0
}

# Start services
start_services() {
    log_message "Starting services..."
    docker-compose up -d

    # Wait for services to be ready
    log_message "Waiting for services to be ready..."
    sleep 10

    # Run database migrations
    log_message "Running database migrations..."
    docker-compose exec app npm run migrate

    # Run database seeds
    log_message "Running database seeds..."
    docker-compose exec app npm run seed
}

# Stop services
stop_services() {
    log_message "Stopping services..."
    docker-compose down
}

# Main monitoring loop
monitor_services() {
    while true; do
        check_resources
        check_service_health
        sleep $CHECK_INTERVAL
    done
}

# Handle script termination
cleanup() {
    log_message "Received termination signal. Cleaning up..."
    stop_services
    exit 0
}

# Set up signal handling
trap cleanup SIGINT SIGTERM

# Main execution
log_message "Starting automated service monitoring..."

# Start services
start_services

# Run initial health check
if ! check_service_health; then
    log_message "${RED}Initial health check failed. Stopping services.${NC}"
    stop_services
    exit 1
fi

log_message "${GREEN}Services started successfully. Beginning monitoring...${NC}"

# Start monitoring
monitor_services 
#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "Starting test environment..."

# Build and start containers
docker-compose up -d

# Wait for services to be ready
echo "Waiting for services to be ready..."
sleep 10

# Test database connection
echo "Testing database connection..."
docker-compose exec postgres pg_isready -U postgres
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Database connection successful${NC}"
else
    echo -e "${RED}Database connection failed${NC}"
    exit 1
fi

# Test Redis connection
echo "Testing Redis connection..."
docker-compose exec redis redis-cli ping
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Redis connection successful${NC}"
else
    echo -e "${RED}Redis connection failed${NC}"
    exit 1
fi

# Test API endpoints
echo "Testing API endpoints..."

# Test health check
echo "Testing health check endpoint..."
curl -s http://localhost:3000/health | grep -q "ok"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Health check successful${NC}"
else
    echo -e "${RED}Health check failed${NC}"
    exit 1
fi

# Test getting users
echo "Testing get users endpoint..."
curl -s http://localhost:3000/api/users | grep -q "id"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Get users successful${NC}"
else
    echo -e "${RED}Get users failed${NC}"
    exit 1
fi

# Test creating a user
echo "Testing create user endpoint..."
curl -s -X POST -H "Content-Type: application/json" \
    -d '{"name":"Test User","email":"test@example.com"}' \
    http://localhost:3000/api/users | grep -q "id"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Create user successful${NC}"
else
    echo -e "${RED}Create user failed${NC}"
    exit 1
fi

echo -e "${GREEN}All tests completed successfully!${NC}"

# Keep containers running for manual testing
echo "Containers are running. Press Ctrl+C to stop."
docker-compose logs -f 
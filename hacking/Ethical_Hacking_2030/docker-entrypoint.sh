#!/bin/bash
set -e

# Check if running as root
if [ "$(id -u)" = '0' ]; then
    # Create a non-root user
    useradd -m -s /bin/bash -u 1000 -g 0 ethical_hacker
    # Change ownership of app directory
    chown -R ethical_hacker:root /app
    # Switch to non-root user
    exec gosu ethical_hacker "$@"
fi

# Execute command
exec "$@" 
# Use Python 3.11 as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    nmap \
    netcat \
    net-tools \
    iputils-ping \
    traceroute \
    dnsutils \
    whois \
    hydra \
    sqlmap \
    nikto \
    dirb \
    gobuster \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install additional security tools
RUN pip install --no-cache-dir \
    metasploit-framework \
    burp-suite \
    wireshark \
    aircrack-ng \
    john \
    hashcat \
    && rm -rf /root/.cache/pip

# Set environment variables
ENV PYTHONPATH=/app
ENV PATH="/app/tools:${PATH}"

# Create necessary directories
RUN mkdir -p /app/{modules,exercises,tools,docs,labs,challenges,resources,projects}

# Copy project files
COPY . .

# Set up entrypoint
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Set default command
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["bash"] 
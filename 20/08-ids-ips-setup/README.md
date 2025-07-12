# 🛡️ Project 8: IDS/IPS Setup with Snort/Suricata

## 📋 Project Overview

Deploy and configure Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) using Snort and Suricata to monitor network traffic and detect/prevent security threats.

**Difficulty**: Intermediate  
**Time Required**: 8-10 hours  
**Skills Gained**: IDS/IPS Configuration, Rule Management, Threat Detection, Network Monitoring

## 🎯 Learning Objectives

- Configure Snort and Suricata IDS/IPS
- Create and manage detection rules
- Implement real-time threat detection
- Set up automated response mechanisms
- Analyze and respond to security alerts
- Integrate with SIEM systems

## 🛠️ Required Tools

### Software
- **Ubuntu Server 22.04 LTS**
- **Snort 3.x** (Latest version)
- **Suricata 6.x** (Latest version)
- **Barnyard2** (Log processor)
- **PulledPork** (Rule management)
- **Wireshark** (Traffic analysis)

### Hardware Requirements
- **CPU**: 4+ cores (8+ recommended)
- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: 100GB+ SSD
- **Network**: Multiple network interfaces

## 🚀 Step-by-Step Implementation

### Phase 1: Snort Installation and Configuration

#### 1.1 Install Snort
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y build-essential libpcap-dev libpcre3-dev libdumbnet-dev bison flex zlib1g-dev liblzma-dev openssl libssl-dev libnghttp2-dev libdnet-dev libnss3-dev libnspr4-dev liblua5.1-dev libluajit-5.1-dev libluabind-dev libcurl4-openssl-dev

# Download and install Snort
cd /tmp
wget https://github.com/snort3/snort3/archive/refs/tags/3.1.58.0.tar.gz
tar -xzf 3.1.58.0.tar.gz
cd snort3-3.1.58.0

# Configure and build
./configure_cmake.sh --prefix=/usr/local/snort
cd build
make -j$(nproc)
sudo make install

# Create Snort user
sudo useradd -r -s /sbin/nologin snort
sudo mkdir -p /var/log/snort
sudo chown snort:snort /var/log/snort
```

#### 1.2 Configure Snort
```bash
# Create Snort configuration directory
sudo mkdir -p /etc/snort
sudo cp /usr/local/snort/etc/snort.lua /etc/snort/

# Edit Snort configuration
sudo nano /etc/snort/snort.lua
```

```lua
-- /etc/snort/snort.lua
HOME_NET = '192.168.1.0/24'
EXTERNAL_NET = '!$HOME_NET'

detection = {
    hyperscan_literals = true,
    pcre_to_regex = true
}

include = '/etc/snort/snort_defaults.lua'

-- Configure outputs
output = {
    alert_fast = {
        file = true,
        packet = false
    },
    alert_syslog = {
        facility = 'local0',
        level = 'warning'
    },
    log_tcpdump = {
        file = '/var/log/snort/snort.log'
    }
}

-- Configure rules
include = '/etc/snort/rules/local.rules'
```

#### 1.3 Download and Configure Rules
```bash
# Create rules directory
sudo mkdir -p /etc/snort/rules

# Download Snort rules (requires registration)
# Visit: https://www.snort.org/downloads
# Download snortrules-snapshot-*.tar.gz

# Extract rules
sudo tar -xzf snortrules-snapshot-*.tar.gz -C /etc/snort/

# Create local rules file
sudo nano /etc/snort/rules/local.rules
```

```bash
# /etc/snort/rules/local.rules
# Local custom rules

# Block known malicious IPs
drop ip [1.2.3.4,5.6.7.8] any -> $HOME_NET any (msg:"Known malicious IP"; sid:1000001; rev:1;)

# Detect port scanning
alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"Port scan detected"; flow:stateless; threshold:type threshold, track by_src, count 10, seconds 60; sid:1000002; rev:1;)

# Detect brute force attempts
alert tcp $EXTERNAL_NET any -> $HOME_NET 22 (msg:"SSH brute force attempt"; flow:established; threshold:type threshold, track by_src, count 5, seconds 60; sid:1000003; rev:1;)

# Detect web attacks
alert tcp $EXTERNAL_NET any -> $HOME_NET 80 (msg:"SQL injection attempt"; content:"' OR 1=1"; http_uri; sid:1000004; rev:1;)
```

### Phase 2: Suricata Installation and Configuration

#### 2.1 Install Suricata
```bash
# Install Suricata
sudo apt install -y suricata

# Create Suricata directories
sudo mkdir -p /var/log/suricata
sudo mkdir -p /etc/suricata/rules
sudo chown -R suricata:suricata /var/log/suricata
```

#### 2.2 Configure Suricata
```bash
# Edit Suricata configuration
sudo nano /etc/suricata/suricata.yaml
```

```yaml
# /etc/suricata/suricata.yaml (key sections)
vars:
  address-groups:
    HOME_NET: "[192.168.1.0/24]"
    EXTERNAL_NET: "!$HOME_NET"

# Configure outputs
outputs:
  - eve-log:
      enabled: yes
      filetype: regular
      filename: eve.json
      types:
        - alert
        - http
        - dns
        - tls
        - flow
        - netflow

  - fast:
      enabled: yes
      filename: fast.log

  - unified2-alert:
      enabled: yes
      filename: unified2.alert

# Configure rules
rule-files:
  - /etc/suricata/rules/*.rules
  - /etc/suricata/rules/local.rules

# Configure performance
threading:
  set-cpu-affinity: yes
  cpu-affinity:
    - management-cpu-set:
        cpu: [ 0 ]
    - receive-cpu-set:
        cpu: [ 0 ]
    - worker-cpu-set:
        cpu: [ 1,2,3 ]
        mode: "balanced"
```

#### 2.3 Download Suricata Rules
```bash
# Download Emerging Threats rules
sudo wget https://rules.emergingthreats.net/open/suricata-6.0/emerging.rules.tar.gz
sudo tar -xzf emerging.rules.tar.gz -C /etc/suricata/rules/

# Download Snort rules for Suricata
sudo wget https://www.snort.org/downloads/community/community-rules.tar.gz
sudo tar -xzf community-rules.tar.gz -C /etc/suricata/rules/

# Create local rules
sudo nano /etc/suricata/rules/local.rules
```

```bash
# /etc/suricata/rules/local.rules
# Local custom rules for Suricata

# Block malicious IPs
drop ip [1.2.3.4,5.6.7.8] any -> $HOME_NET any (msg:"Known malicious IP"; sid:1000001; rev:1;)

# Detect port scanning
alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"Port scan detected"; flow:stateless; threshold:type threshold, track by_src, count 10, seconds 60; sid:1000002; rev:1;)

# Detect web attacks
alert tcp $EXTERNAL_NET any -> $HOME_NET 80 (msg:"SQL injection attempt"; content:"' OR 1=1"; http_uri; sid:1000003; rev:1;)

# Detect malware downloads
alert http $EXTERNAL_NET any -> $HOME_NET any (msg:"Potential malware download"; content:"application/octet-stream"; http_response_body; sid:1000004; rev:1;)
```

### Phase 3: Rule Management and Updates

#### 3.1 Automated Rule Updates
```bash
# Install PulledPork for Snort rule management
sudo apt install -y libcrypt-ssleay-perl liblwp-protocol-https-perl

cd /tmp
wget https://github.com/shirkdog/pulledpork3/archive/refs/tags/3.0.0.tar.gz
tar -xzf 3.0.0.tar.gz
sudo cp -r pulledpork3-3.0.0 /opt/pulledpork

# Configure PulledPork
sudo nano /opt/pulledpork/etc/pulledpork.conf
```

```ini
# /opt/pulledpork/etc/pulledpork.conf
rule_url=https://www.snort.org/reg-rules/|snortrules-snapshot-2983.tar.gz|oinkcode
rule_url=https://rules.emergingthreats.net/open/snort-2.9.0/emerging.rules.tar.gz|emerging.rules.tar.gz|
rule_url=https://rules.emergingthreats.net/open/snort-2.9.0/compromised-ips.txt|compromised-ips.txt|

# Snort configuration
config_path=/etc/snort/snort.lua
rule_path=/etc/snort/rules/
local_rules=/etc/snort/rules/local.rules
sid_msg=/etc/snort/sid-msg.map
sid_msg_version=2

# Output configuration
output_path=/etc/snort/rules/snort.rules
version=2.9.0
```

#### 3.2 Rule Update Script
```bash
#!/bin/bash
# update_rules.sh

# Update Snort rules
echo "Updating Snort rules..."
cd /opt/pulledpork
sudo perl pulledpork.pl -c /opt/pulledpork/etc/pulledpork.conf

# Update Suricata rules
echo "Updating Suricata rules..."
cd /tmp
sudo wget -O emerging.rules.tar.gz https://rules.emergingthreats.net/open/suricata-6.0/emerging.rules.tar.gz
sudo tar -xzf emerging.rules.tar.gz -C /etc/suricata/rules/

# Reload services
echo "Reloading services..."
sudo systemctl reload snort
sudo systemctl reload suricata

echo "Rule update completed!"
```

### Phase 4: Monitoring and Alerting

#### 4.1 Snort Monitoring Script
```python
#!/usr/bin/env python3
# snort_monitor.py

import subprocess
import json
import time
import logging
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

class SnortMonitor:
    def __init__(self, alert_file="/var/log/snort/alert"):
        self.alert_file = alert_file
        self.last_position = 0
        self.setup_logging()
    
    def setup_logging(self):
        logging.basicConfig(
            filename='snort_monitor.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def parse_alert(self, alert_line):
        """Parse Snort alert line"""
        try:
            # Parse alert format
            parts = alert_line.strip().split()
            if len(parts) < 8:
                return None
            
            alert = {
                'timestamp': f"{parts[0]} {parts[1]}",
                'priority': parts[2],
                'protocol': parts[3],
                'src_ip': parts[4],
                'src_port': parts[5],
                'dst_ip': parts[6],
                'dst_port': parts[7],
                'message': ' '.join(parts[8:])
            }
            
            return alert
        except Exception as e:
            logging.error(f"Error parsing alert: {e}")
            return None
    
    def monitor_alerts(self):
        """Monitor Snort alert file"""
        while True:
            try:
                with open(self.alert_file, 'r') as f:
                    f.seek(self.last_position)
                    new_alerts = f.readlines()
                    self.last_position = f.tell()
                
                for alert_line in new_alerts:
                    if alert_line.strip():
                        alert = self.parse_alert(alert_line)
                        if alert:
                            self.handle_alert(alert)
                
                time.sleep(10)  # Check every 10 seconds
                
            except FileNotFoundError:
                logging.error(f"Alert file not found: {self.alert_file}")
                time.sleep(60)
            except Exception as e:
                logging.error(f"Monitoring error: {e}")
                time.sleep(60)
    
    def handle_alert(self, alert):
        """Handle individual alert"""
        logging.warning(f"Alert: {json.dumps(alert)}")
        
        # Check for high priority alerts
        if alert['priority'] in ['1', '2', '3']:
            self.send_alert_notification(alert)
        
        # Check for specific attack types
        if 'brute force' in alert['message'].lower():
            self.handle_bruteforce_alert(alert)
        elif 'port scan' in alert['message'].lower():
            self.handle_portscan_alert(alert)
    
    def send_alert_notification(self, alert):
        """Send email notification"""
        subject = f"High Priority Snort Alert - {alert['src_ip']}"
        body = f"""
High Priority Snort Alert Detected

Timestamp: {alert['timestamp']}
Priority: {alert['priority']}
Protocol: {alert['protocol']}
Source: {alert['src_ip']}:{alert['src_port']}
Destination: {alert['dst_ip']}:{alert['dst_port']}
Message: {alert['message']}

Action Required: Investigate immediately.
"""
        
        # Send email (configure SMTP settings)
        # self.send_email(subject, body)
        
        logging.info(f"Alert notification sent for {alert['src_ip']}")
    
    def handle_bruteforce_alert(self, alert):
        """Handle brute force alerts"""
        logging.warning(f"Brute force attack detected from {alert['src_ip']}")
        
        # Implement blocking logic
        self.block_ip(alert['src_ip'])
    
    def handle_portscan_alert(self, alert):
        """Handle port scan alerts"""
        logging.warning(f"Port scan detected from {alert['src_ip']}")
        
        # Implement monitoring logic
        self.monitor_ip(alert['src_ip'])
    
    def block_ip(self, ip):
        """Block IP address"""
        try:
            # Add to iptables
            subprocess.run(['iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'], check=True)
            logging.info(f"Blocked IP: {ip}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error blocking IP {ip}: {e}")
    
    def monitor_ip(self, ip):
        """Monitor IP address"""
        logging.info(f"Monitoring IP: {ip}")
        # Implement additional monitoring logic

if __name__ == "__main__":
    monitor = SnortMonitor()
    monitor.monitor_alerts()
```

#### 4.2 Suricata Monitoring Script
```python
#!/usr/bin/env python3
# suricata_monitor.py

import json
import time
import logging
from datetime import datetime
import subprocess

class SuricataMonitor:
    def __init__(self, eve_file="/var/log/suricata/eve.json"):
        self.eve_file = eve_file
        self.last_position = 0
        self.setup_logging()
    
    def setup_logging(self):
        logging.basicConfig(
            filename='suricata_monitor.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def monitor_events(self):
        """Monitor Suricata EVE events"""
        while True:
            try:
                with open(self.eve_file, 'r') as f:
                    f.seek(self.last_position)
                    new_events = f.readlines()
                    self.last_position = f.tell()
                
                for event_line in new_events:
                    if event_line.strip():
                        try:
                            event = json.loads(event_line)
                            self.handle_event(event)
                        except json.JSONDecodeError:
                            continue
                
                time.sleep(5)  # Check every 5 seconds
                
            except FileNotFoundError:
                logging.error(f"EVE file not found: {self.eve_file}")
                time.sleep(60)
            except Exception as e:
                logging.error(f"Monitoring error: {e}")
                time.sleep(60)
    
    def handle_event(self, event):
        """Handle individual event"""
        event_type = event.get('event_type')
        
        if event_type == 'alert':
            self.handle_alert(event)
        elif event_type == 'http':
            self.handle_http_event(event)
        elif event_type == 'dns':
            self.handle_dns_event(event)
        elif event_type == 'tls':
            self.handle_tls_event(event)
    
    def handle_alert(self, alert):
        """Handle alert events"""
        logging.warning(f"Alert: {json.dumps(alert)}")
        
        # Check alert severity
        if alert.get('alert', {}).get('severity', 0) >= 2:
            self.send_alert_notification(alert)
        
        # Check for specific signatures
        signature = alert.get('alert', {}).get('signature', '')
        if 'brute force' in signature.lower():
            self.handle_bruteforce_alert(alert)
        elif 'port scan' in signature.lower():
            self.handle_portscan_alert(alert)
    
    def handle_http_event(self, http_event):
        """Handle HTTP events"""
        # Monitor for suspicious HTTP activity
        if http_event.get('http', {}).get('status', 0) >= 400:
            logging.info(f"HTTP error: {json.dumps(http_event)}")
    
    def handle_dns_event(self, dns_event):
        """Handle DNS events"""
        # Monitor for suspicious DNS queries
        query = dns_event.get('dns', {}).get('rrname', '')
        if 'malware' in query.lower() or 'suspicious' in query.lower():
            logging.warning(f"Suspicious DNS query: {query}")
    
    def handle_tls_event(self, tls_event):
        """Handle TLS events"""
        # Monitor for suspicious TLS connections
        subject = tls_event.get('tls', {}).get('subject', '')
        if 'suspicious' in subject.lower():
            logging.warning(f"Suspicious TLS connection: {subject}")
    
    def send_alert_notification(self, alert):
        """Send alert notification"""
        alert_data = alert.get('alert', {})
        subject = f"Suricata Alert - {alert_data.get('signature', 'Unknown')}"
        
        logging.info(f"Alert notification: {subject}")
    
    def handle_bruteforce_alert(self, alert):
        """Handle brute force alerts"""
        src_ip = alert.get('src_ip', '')
        logging.warning(f"Brute force attack from {src_ip}")
        self.block_ip(src_ip)
    
    def handle_portscan_alert(self, alert):
        """Handle port scan alerts"""
        src_ip = alert.get('src_ip', '')
        logging.warning(f"Port scan from {src_ip}")
        self.monitor_ip(src_ip)
    
    def block_ip(self, ip):
        """Block IP address"""
        try:
            subprocess.run(['iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'], check=True)
            logging.info(f"Blocked IP: {ip}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error blocking IP {ip}: {e}")
    
    def monitor_ip(self, ip):
        """Monitor IP address"""
        logging.info(f"Monitoring IP: {ip}")

if __name__ == "__main__":
    monitor = SuricataMonitor()
    monitor.monitor_events()
```

### Phase 5: Performance Optimization

#### 5.1 Snort Performance Tuning
```bash
# Configure Snort for high performance
sudo nano /etc/snort/snort.lua
```

```lua
-- Performance optimizations
detection = {
    hyperscan_literals = true,
    pcre_to_regex = true,
    pcre_match_limit = 1500,
    pcre_match_limit_recursion = 1500
}

-- Configure packet processing
max_pdu = 16384
max_mss = 1460
stream_tcp = {
    max_window = 1048576,
    overlap_limit = 10
}

-- Configure memory usage
max_attribute_hosts = 10000
max_attribute_services_per_host = 10
```

#### 5.2 Suricata Performance Tuning
```yaml
# Performance optimizations in suricata.yaml
threading:
  set-cpu-affinity: yes
  cpu-affinity:
    - management-cpu-set:
        cpu: [ 0 ]
    - receive-cpu-set:
        cpu: [ 0 ]
    - worker-cpu-set:
        cpu: [ 1,2,3,4,5,6,7 ]
        mode: "balanced"

# Configure memory usage
vars:
  max-pending-packets: 1024
  default-packet-size: 1514

# Configure flow settings
flow:
  memcap: 134217728
  hash-size: 1048576
  prealloc: yes
  emergency-recovery: 30
```

## 🧪 Testing and Validation

### Testing Scenarios
```bash
# Test Snort detection
# Generate test traffic
nmap -sS 192.168.1.10
nmap -sV 192.168.1.10

# Test Suricata detection
# Generate HTTP attacks
curl "http://192.168.1.10/?id=1' OR 1=1--"

# Test rule updates
sudo ./update_rules.sh

# Test performance
# Monitor CPU and memory usage
htop
iotop

# Test alerting
# Verify alerts are generated
# Check email notifications
# Test automated responses
```

## 📊 Success Metrics

### Detection Metrics
- **Detection Rate**: > 95%
- **False Positive Rate**: < 5%
- **Detection Time**: < 1 second
- **Coverage**: 100% of network traffic

### Performance Metrics
- **Throughput**: > 1 Gbps
- **Latency**: < 1ms
- **CPU Usage**: < 80%
- **Memory Usage**: < 8GB

## 🎯 Career Impact

### Skills Demonstrated
- **IDS/IPS Configuration**
- **Rule Management**
- **Threat Detection**
- **Performance Tuning**
- **Security Monitoring**

### Job Roles This Prepares You For
- **Security Analyst**
- **SOC Analyst**
- **Network Security Engineer**
- **Threat Hunter**
- **Security Engineer**

---

**Next Project**: [Project 9: OpenVPN + MFA Implementation](../09-openvpn-mfa/README.md)

**Previous Project**: [Project 7: Active Directory + LDAP Bruteforce Monitoring](../07-ad-monitoring/README.md) 
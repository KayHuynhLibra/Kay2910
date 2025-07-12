# 🍯 Project 5: Honeypot Deployment

## 📋 Project Overview

Deploy and monitor honeypot systems to collect threat intelligence, analyze attack patterns, and understand real-world cyber threats in a controlled environment.

**Difficulty**: Intermediate  
**Time Required**: 6-8 hours  
**Skills Gained**: Threat Intelligence, Attack Analysis, Security Monitoring, Data Collection

## 🎯 Learning Objectives

- Deploy multiple honeypot types (T-Pot, Cowrie, Dionaea)
- Monitor and analyze attack patterns
- Collect and process threat intelligence
- Understand attacker behavior and techniques
- Generate threat intelligence reports
- Implement honeypot security best practices

## 🛠️ Required Tools

### Software
- **T-Pot** (Multi-honeypot platform)
- **Cowrie** (SSH/Telnet honeypot)
- **Dionaea** (Malware honeypot)
- **Ubuntu Server 22.04 LTS**
- **Docker & Docker Compose**
- **ELK Stack** (Elasticsearch, Logstash, Kibana)

### Hardware Requirements
- **CPU**: 4+ cores (8+ recommended)
- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: 100GB+ SSD
- **Network**: Public IP address (optional but recommended)

## 🚀 Step-by-Step Implementation

### Phase 1: T-Pot Honeypot Platform Setup

#### 1.1 System Preparation
```bash
# Download and install Ubuntu Server 22.04 LTS
# Ensure system is up to date
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y git curl wget docker.io docker-compose

# Add user to docker group
sudo usermod -aG docker $USER

# Reboot to apply group changes
sudo reboot
```

#### 1.2 T-Pot Installation
```bash
# Clone T-Pot repository
git clone https://github.com/telekom-security/tpotce.git
cd tpotce

# Run T-Pot installer
sudo ./install.sh --type=auto

# During installation, choose:
# - Installation type: Standard (recommended)
# - Web interface: Yes
# - SSH key: Generate new or use existing
# - Admin password: Set strong password
```

#### 1.3 T-Pot Configuration
```bash
# Access T-Pot web interface
# URL: https://your-server-ip:64297
# Username: tsec
# Password: [your-admin-password]

# Configure honeypot settings
# Navigate to: Configuration > Honeypots

# Enable/disable honeypots:
# - Cowrie (SSH/Telnet): Enabled
# - Dionaea (Malware): Enabled
# - Honeytrap (Network): Enabled
# - Adbhoney (Android): Disabled (unless needed)
# - Ciscotelnet (Cisco): Disabled (unless needed)
# - Conpot (ICS): Disabled (unless needed)
# - Elasticpot (Elasticsearch): Enabled
# - Glastopf (Web): Enabled
# - Honeypy (Low-interaction): Enabled
# - Mailoney (SMTP): Enabled
# - Rdphoney (RDP): Enabled
# - Wordpot (WordPress): Enabled
```

### Phase 2: Individual Honeypot Deployment

#### 2.1 Cowrie SSH Honeypot
```bash
# Manual Cowrie installation (alternative to T-Pot)
git clone https://github.com/cowrie/cowrie.git
cd cowrie

# Create virtual environment
python3 -m venv cowrie-env
source cowrie-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure Cowrie
cp cowrie.cfg.dist cowrie.cfg

# Edit configuration
nano cowrie.cfg

# Key configuration options:
[ssh]
enabled = true
port = 2222
version = SSH-2.0-OpenSSH_7.9

[output_jsonlog]
enabled = true
logfile = log/cowrie.json

[output_mysql]
enabled = true
host = localhost
database = cowrie
username = cowrie
password = your_password
```

#### 2.2 Dionaea Malware Honeypot
```bash
# Manual Dionaea installation
git clone https://github.com/DinoTools/dionaea.git
cd dionaea

# Install dependencies
sudo apt install -y build-essential cmake libglib2.0-dev libssl-dev libcurl4-openssl-dev libreadline-dev libsqlite3-dev libtool automake autoconf libxml2-dev libpcap-dev

# Build and install
mkdir build
cd build
cmake ..
make
sudo make install

# Configure Dionaea
sudo cp /opt/dionaea/etc/dionaea.conf.dist /opt/dionaea/etc/dionaea.conf

# Edit configuration
sudo nano /opt/dionaea/etc/dionaea.conf

# Key settings:
[output_json]
enabled = true
logfile = /opt/dionaea/var/log/dionaea.json

[output_sqlite]
enabled = true
logfile = /opt/dionaea/var/log/dionaea.sqlite
```

#### 2.3 Custom Honeypot Development
```python
# Simple Python honeypot example
import socket
import threading
import json
import datetime
import logging

class SimpleHoneypot:
    def __init__(self, host='0.0.0.0', port=22):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Setup logging
        logging.basicConfig(
            filename='honeypot.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
    def start(self):
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(5)
            print(f"Honeypot listening on {self.host}:{self.port}")
            
            while True:
                client, address = self.socket.accept()
                client_handler = threading.Thread(
                    target=self.handle_client,
                    args=(client, address)
                )
                client_handler.start()
                
        except Exception as e:
            print(f"Error: {e}")
            self.socket.close()
    
    def handle_client(self, client, address):
        try:
            # Log connection
            self.log_connection(address)
            
            # Send fake SSH banner
            banner = "SSH-2.0-OpenSSH_7.9 Ubuntu-10ubuntu2.1\r\n"
            client.send(banner.encode())
            
            # Collect data
            data = client.recv(1024)
            if data:
                self.log_data(address, data)
            
            # Keep connection open for a while
            import time
            time.sleep(30)
            
        except Exception as e:
            logging.error(f"Error handling client {address}: {e}")
        finally:
            client.close()
    
    def log_connection(self, address):
        log_entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'event': 'connection',
            'ip': address[0],
            'port': address[1]
        }
        logging.info(json.dumps(log_entry))
    
    def log_data(self, address, data):
        log_entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'event': 'data_received',
            'ip': address[0],
            'port': address[1],
            'data': data.decode('utf-8', errors='ignore')
        }
        logging.info(json.dumps(log_entry))

if __name__ == "__main__":
    honeypot = SimpleHoneypot()
    honeypot.start()
```

### Phase 3: Monitoring and Data Collection

#### 3.1 ELK Stack Integration
```yaml
# docker-compose.yml for ELK Stack
version: '3.7'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.0
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - "9200:9200"
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data

  kibana:
    image: docker.elastic.co/kibana/kibana:7.17.0
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch

  logstash:
    image: docker.elastic.co/logstash/logstash:7.17.0
    ports:
      - "5044:5044"
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    depends_on:
      - elasticsearch
```

#### 3.2 Logstash Configuration
```ruby
# logstash.conf
input {
  file {
    path => "/opt/dionaea/var/log/dionaea.json"
    type => "dionaea"
    codec => json
  }
  file {
    path => "/opt/cowrie/log/cowrie.json"
    type => "cowrie"
    codec => json
  }
}

filter {
  if [type] == "dionaea" {
    mutate {
      add_field => { "honeypot_type" => "dionaea" }
    }
  }
  if [type] == "cowrie" {
    mutate {
      add_field => { "honeypot_type" => "cowrie" }
    }
  }
  
  geoip {
    source => "src_ip"
    target => "geoip"
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "honeypot-%{+YYYY.MM.dd}"
  }
}
```

#### 3.3 Real-time Monitoring Script
```python
# honeypot_monitor.py
import json
import time
import requests
from datetime import datetime
import logging

class HoneypotMonitor:
    def __init__(self, elasticsearch_url="http://localhost:9200"):
        self.es_url = elasticsearch_url
        self.setup_logging()
    
    def setup_logging(self):
        logging.basicConfig(
            filename='honeypot_monitor.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def get_recent_attacks(self, minutes=60):
        """Get attacks from the last N minutes"""
        query = {
            "query": {
                "range": {
                    "@timestamp": {
                        "gte": f"now-{minutes}m",
                        "lte": "now"
                    }
                }
            },
            "sort": [{"@timestamp": {"order": "desc"}}],
            "size": 100
        }
        
        try:
            response = requests.post(
                f"{self.es_url}/honeypot-*/_search",
                json=query
            )
            return response.json()
        except Exception as e:
            logging.error(f"Error querying Elasticsearch: {e}")
            return None
    
    def analyze_attack_patterns(self, attacks):
        """Analyze attack patterns and statistics"""
        if not attacks or 'hits' not in attacks:
            return {}
        
        stats = {
            'total_attacks': len(attacks['hits']['hits']),
            'unique_ips': set(),
            'countries': {},
            'honeypot_types': {},
            'attack_times': []
        }
        
        for hit in attacks['hits']['hits']:
            source = hit['_source']
            
            # Count unique IPs
            if 'src_ip' in source:
                stats['unique_ips'].add(source['src_ip'])
            
            # Count countries
            if 'geoip' in source and 'country_name' in source['geoip']:
                country = source['geoip']['country_name']
                stats['countries'][country] = stats['countries'].get(country, 0) + 1
            
            # Count honeypot types
            if 'honeypot_type' in source:
                hp_type = source['honeypot_type']
                stats['honeypot_types'][hp_type] = stats['honeypot_types'].get(hp_type, 0) + 1
            
            # Track attack times
            if '@timestamp' in source:
                stats['attack_times'].append(source['@timestamp'])
        
        stats['unique_ips'] = len(stats['unique_ips'])
        return stats
    
    def generate_alert(self, stats):
        """Generate alerts based on attack patterns"""
        alerts = []
        
        # Alert for high attack volume
        if stats['total_attacks'] > 100:
            alerts.append({
                'type': 'high_volume',
                'message': f"High attack volume detected: {stats['total_attacks']} attacks",
                'severity': 'high'
            })
        
        # Alert for attacks from specific countries
        suspicious_countries = ['Russia', 'China', 'North Korea', 'Iran']
        for country in suspicious_countries:
            if country in stats['countries'] and stats['countries'][country] > 10:
                alerts.append({
                    'type': 'suspicious_country',
                    'message': f"Multiple attacks from {country}: {stats['countries'][country]}",
                    'severity': 'medium'
                })
        
        return alerts
    
    def run_monitoring(self, interval=300):  # 5 minutes
        """Run continuous monitoring"""
        print("Starting honeypot monitoring...")
        
        while True:
            try:
                # Get recent attacks
                attacks = self.get_recent_attacks()
                
                if attacks:
                    # Analyze patterns
                    stats = self.analyze_attack_patterns(attacks)
                    
                    # Generate alerts
                    alerts = self.generate_alert(stats)
                    
                    # Log statistics
                    logging.info(f"Attack Statistics: {json.dumps(stats)}")
                    
                    # Process alerts
                    for alert in alerts:
                        logging.warning(f"Alert: {alert['message']}")
                        print(f"[{alert['severity'].upper()}] {alert['message']}")
                
                time.sleep(interval)
                
            except KeyboardInterrupt:
                print("Monitoring stopped by user")
                break
            except Exception as e:
                logging.error(f"Monitoring error: {e}")
                time.sleep(interval)

if __name__ == "__main__":
    monitor = HoneypotMonitor()
    monitor.run_monitoring()
```

### Phase 4: Threat Intelligence Analysis

#### 4.1 Attack Pattern Analysis
```python
# threat_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import requests
import json

class ThreatAnalyzer:
    def __init__(self, elasticsearch_url="http://localhost:9200"):
        self.es_url = elasticsearch_url
    
    def get_attack_data(self, days=7):
        """Get attack data for analysis"""
        query = {
            "query": {
                "range": {
                    "@timestamp": {
                        "gte": f"now-{days}d",
                        "lte": "now"
                    }
                }
            },
            "size": 10000
        }
        
        response = requests.post(
            f"{self.es_url}/honeypot-*/_search",
            json=query
        )
        
        if response.status_code == 200:
            return response.json()
        return None
    
    def analyze_attack_trends(self, data):
        """Analyze attack trends over time"""
        if not data or 'hits' not in data:
            return None
        
        attacks = []
        for hit in data['hits']['hits']:
            source = hit['_source']
            attacks.append({
                'timestamp': source.get('@timestamp'),
                'ip': source.get('src_ip'),
                'honeypot_type': source.get('honeypot_type'),
                'country': source.get('geoip', {}).get('country_name'),
                'city': source.get('geoip', {}).get('city_name')
            })
        
        df = pd.DataFrame(attacks)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.hour
        df['day'] = df['timestamp'].dt.day
        
        return df
    
    def generate_visualizations(self, df):
        """Generate threat intelligence visualizations"""
        if df is None or df.empty:
            return
        
        # Set up the plotting style
        plt.style.use('seaborn')
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        
        # 1. Attacks by hour of day
        hourly_attacks = df['hour'].value_counts().sort_index()
        axes[0, 0].bar(hourly_attacks.index, hourly_attacks.values)
        axes[0, 0].set_title('Attacks by Hour of Day')
        axes[0, 0].set_xlabel('Hour')
        axes[0, 0].set_ylabel('Number of Attacks')
        
        # 2. Attacks by honeypot type
        honeypot_attacks = df['honeypot_type'].value_counts()
        axes[0, 1].pie(honeypot_attacks.values, labels=honeypot_attacks.index, autopct='%1.1f%%')
        axes[0, 1].set_title('Attacks by Honeypot Type')
        
        # 3. Top attacking countries
        country_attacks = df['country'].value_counts().head(10)
        axes[1, 0].barh(range(len(country_attacks)), country_attacks.values)
        axes[1, 0].set_yticks(range(len(country_attacks)))
        axes[1, 0].set_yticklabels(country_attacks.index)
        axes[1, 0].set_title('Top 10 Attacking Countries')
        axes[1, 0].set_xlabel('Number of Attacks')
        
        # 4. Attacks over time
        daily_attacks = df.groupby(df['timestamp'].dt.date).size()
        axes[1, 1].plot(daily_attacks.index, daily_attacks.values, marker='o')
        axes[1, 1].set_title('Daily Attack Volume')
        axes[1, 1].set_xlabel('Date')
        axes[1, 1].set_ylabel('Number of Attacks')
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('threat_intelligence_report.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def generate_threat_report(self, df):
        """Generate comprehensive threat intelligence report"""
        if df is None or df.empty:
            return "No attack data available"
        
        report = {
            'summary': {
                'total_attacks': len(df),
                'unique_attackers': df['ip'].nunique(),
                'countries_involved': df['country'].nunique(),
                'honeypot_types_targeted': df['honeypot_type'].nunique()
            },
            'top_attackers': df['ip'].value_counts().head(10).to_dict(),
            'top_countries': df['country'].value_counts().head(10).to_dict(),
            'honeypot_targeting': df['honeypot_type'].value_counts().to_dict(),
            'peak_hours': df['hour'].value_counts().head(5).to_dict()
        }
        
        return report

# Usage
analyzer = ThreatAnalyzer()
data = analyzer.get_attack_data(days=7)
df = analyzer.analyze_attack_trends(data)
analyzer.generate_visualizations(df)
report = analyzer.generate_threat_report(df)
print(json.dumps(report, indent=2))
```

#### 4.2 Malware Analysis
```python
# malware_analysis.py
import hashlib
import os
import json
import requests
from datetime import datetime

class MalwareAnalyzer:
    def __init__(self, samples_dir="/opt/dionaea/var/lib/dionaea/binaries"):
        self.samples_dir = samples_dir
        self.virustotal_api_key = "your_virustotal_api_key"  # Optional
    
    def analyze_samples(self):
        """Analyze collected malware samples"""
        samples = []
        
        for filename in os.listdir(self.samples_dir):
            filepath = os.path.join(self.samples_dir, filename)
            
            if os.path.isfile(filepath):
                sample_info = self.analyze_sample(filepath)
                samples.append(sample_info)
        
        return samples
    
    def analyze_sample(self, filepath):
        """Analyze individual malware sample"""
        with open(filepath, 'rb') as f:
            content = f.read()
        
        sample_info = {
            'filename': os.path.basename(filepath),
            'filepath': filepath,
            'size': len(content),
            'md5': hashlib.md5(content).hexdigest(),
            'sha1': hashlib.sha1(content).hexdigest(),
            'sha256': hashlib.sha256(content).hexdigest(),
            'analysis_date': datetime.now().isoformat()
        }
        
        # Optional: Submit to VirusTotal
        if self.virustotal_api_key:
            vt_result = self.submit_to_virustotal(sample_info['sha256'])
            sample_info['virustotal'] = vt_result
        
        return sample_info
    
    def submit_to_virustotal(self, file_hash):
        """Submit file hash to VirusTotal for analysis"""
        url = f"https://www.virustotal.com/vtapi/v2/file/report"
        params = {
            'apikey': self.virustotal_api_key,
            'resource': file_hash
        }
        
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Error submitting to VirusTotal: {e}")
        
        return None
    
    def generate_malware_report(self, samples):
        """Generate malware analysis report"""
        report = {
            'summary': {
                'total_samples': len(samples),
                'unique_hashes': len(set(s['md5'] for s in samples)),
                'analysis_date': datetime.now().isoformat()
            },
            'samples': samples,
            'statistics': {
                'size_distribution': self.analyze_size_distribution(samples),
                'detection_rates': self.analyze_detection_rates(samples)
            }
        }
        
        return report
    
    def analyze_size_distribution(self, samples):
        """Analyze malware sample size distribution"""
        sizes = [s['size'] for s in samples]
        return {
            'min_size': min(sizes),
            'max_size': max(sizes),
            'avg_size': sum(sizes) / len(sizes),
            'size_ranges': {
                'small (< 1KB)': len([s for s in sizes if s < 1024]),
                'medium (1KB-100KB)': len([s for s in sizes if 1024 <= s < 102400]),
                'large (> 100KB)': len([s for s in sizes if s >= 102400])
            }
        }
    
    def analyze_detection_rates(self, samples):
        """Analyze VirusTotal detection rates"""
        if not samples or 'virustotal' not in samples[0]:
            return {}
        
        detections = []
        for sample in samples:
            if 'virustotal' in sample and sample['virustotal']:
                vt = sample['virustotal']
                if 'positives' in vt and 'total' in vt:
                    detections.append({
                        'positives': vt['positives'],
                        'total': vt['total'],
                        'ratio': vt['positives'] / vt['total'] if vt['total'] > 0 else 0
                    })
        
        if detections:
            return {
                'avg_detection_rate': sum(d['ratio'] for d in detections) / len(detections),
                'high_detection_samples': len([d for d in detections if d['ratio'] > 0.5]),
                'low_detection_samples': len([d for d in detections if d['ratio'] < 0.1])
            }
        
        return {}

# Usage
analyzer = MalwareAnalyzer()
samples = analyzer.analyze_samples()
report = analyzer.generate_malware_report(samples)
print(json.dumps(report, indent=2))
```

### Phase 5: Security and Best Practices

#### 5.1 Honeypot Security Configuration
```bash
# Security hardening for honeypot systems

# 1. Network isolation
# Configure honeypot on isolated network segment
# Use VLANs to separate honeypot traffic
# Implement strict firewall rules

# 2. System hardening
sudo apt install -y fail2ban ufw
sudo ufw enable
sudo ufw default deny incoming
sudo ufw allow ssh

# Configure fail2ban
sudo nano /etc/fail2ban/jail.local
```

```ini
# /etc/fail2ban/jail.local
[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 3

[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
```

```bash
# 3. Monitoring and alerting
# Set up system monitoring
sudo apt install -y htop iotop nethogs

# Configure log monitoring
sudo nano /etc/logwatch/conf/logwatch.conf
```

#### 5.2 Legal and Ethical Considerations
```markdown
# Legal and Ethical Guidelines

## Legal Considerations
- **Jurisdiction**: Understand local laws regarding honeypots
- **Data Collection**: Ensure compliance with privacy laws
- **Data Retention**: Implement appropriate data retention policies
- **Disclosure**: Be transparent about honeypot deployment

## Ethical Guidelines
- **Purpose**: Use honeypots for research and defense only
- **Data Handling**: Protect collected data appropriately
- **Sharing**: Share threat intelligence responsibly
- **Transparency**: Be honest about honeypot capabilities

## Best Practices
- **Isolation**: Keep honeypots isolated from production systems
- **Monitoring**: Monitor honeypot systems continuously
- **Documentation**: Document all activities and findings
- **Incident Response**: Have procedures for handling incidents
```

## 🧪 Testing and Validation

### Honeypot Testing Scenarios
```bash
# Test honeypot functionality

# 1. Test SSH honeypot
ssh -p 2222 user@honeypot-ip

# 2. Test web honeypot
curl http://honeypot-ip:80

# 3. Test malware honeypot
# Use tools like Metasploit to generate test payloads

# 4. Test monitoring
# Verify logs are being generated
# Check ELK Stack dashboards
# Validate alerting systems
```

### Performance Testing
```bash
# Load testing honeypots

# Test with multiple concurrent connections
for i in {1..100}; do
    ssh -p 2222 user@honeypot-ip &
done

# Monitor system resources
htop
iotop
nethogs

# Check log generation rate
tail -f /var/log/honeypot.log | wc -l
```

## 📊 Success Metrics

### Technical Metrics
```markdown
# Honeypot Performance Metrics

## Data Collection
- **Attack Volume**: Number of attacks per day/week
- **Unique Attackers**: Number of unique IP addresses
- **Geographic Distribution**: Countries of origin
- **Attack Types**: Types of attacks observed

## System Performance
- **Uptime**: Honeypot system availability
- **Response Time**: Time to respond to attacks
- **Log Generation**: Volume of logs generated
- **Resource Usage**: CPU, memory, disk usage

## Threat Intelligence
- **New Threats**: Previously unknown attack patterns
- **Malware Samples**: Number of unique malware samples
- **IOC Generation**: Indicators of compromise identified
- **TTP Analysis**: Tactics, techniques, and procedures observed
```

### Business Metrics
```markdown
# Business Value Metrics

## Security Improvement
- **Threat Detection**: Improved threat detection capabilities
- **Incident Response**: Faster incident response times
- **Risk Reduction**: Reduced security risks
- **Compliance**: Enhanced compliance capabilities

## Cost Benefits
- **Research Value**: Value of threat intelligence gathered
- **Training Value**: Value for security team training
- **Tool Development**: Insights for security tool development
- **Risk Assessment**: Improved risk assessment capabilities
```

## 🔍 Troubleshooting

### Common Issues
```bash
# Troubleshooting Guide

## Honeypot Not Receiving Attacks
- Check network connectivity
- Verify firewall configuration
- Ensure honeypot is publicly accessible
- Check honeypot service status

## High Resource Usage
- Monitor system resources
- Optimize honeypot configuration
- Implement resource limits
- Consider scaling infrastructure

## Log Management Issues
- Check disk space
- Implement log rotation
- Verify log permissions
- Test log forwarding

## False Positives
- Tune detection rules
- Implement whitelisting
- Review alert thresholds
- Validate threat intelligence
```

## 📈 Advanced Features

### Machine Learning Integration
```python
# ML-based threat detection
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class MLThreatDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)
        self.scaler = StandardScaler()
        self.features = []
    
    def extract_features(self, attack_data):
        """Extract features from attack data"""
        features = []
        for attack in attack_data:
            feature_vector = [
                attack.get('hour', 0),
                attack.get('day_of_week', 0),
                attack.get('country_code', 0),
                attack.get('payload_size', 0),
                attack.get('connection_duration', 0)
            ]
            features.append(feature_vector)
        
        return np.array(features)
    
    def train_model(self, attack_data):
        """Train anomaly detection model"""
        features = self.extract_features(attack_data)
        features_scaled = self.scaler.fit_transform(features)
        self.model.fit(features_scaled)
    
    def detect_anomalies(self, new_attacks):
        """Detect anomalous attacks"""
        features = self.extract_features(new_attacks)
        features_scaled = self.scaler.transform(features)
        predictions = self.model.predict(features_scaled)
        
        anomalies = []
        for i, pred in enumerate(predictions):
            if pred == -1:  # Anomaly detected
                anomalies.append(new_attacks[i])
        
        return anomalies
```

### Threat Intelligence Sharing
```python
# Threat intelligence sharing
import requests
import json

class ThreatIntelligenceSharing:
    def __init__(self):
        self.sharing_endpoints = {
            'abuseipdb': 'https://api.abuseipdb.com/api/v2/blacklist',
            'virustotal': 'https://www.virustotal.com/vtapi/v2/ip-address/report',
            'alienvault': 'https://otx.alienvault.com/api/v1/indicators/IPv4/'
        }
    
    def share_ioc(self, ioc_type, ioc_value, confidence=50):
        """Share indicator of compromise"""
        ioc_data = {
            'type': ioc_type,
            'value': ioc_value,
            'confidence': confidence,
            'source': 'honeypot',
            'timestamp': datetime.now().isoformat()
        }
        
        # Share with threat intelligence platforms
        for platform, endpoint in self.sharing_endpoints.items():
            try:
                response = requests.post(endpoint, json=ioc_data)
                if response.status_code == 200:
                    print(f"Successfully shared IOC with {platform}")
            except Exception as e:
                print(f"Error sharing with {platform}: {e}")
    
    def get_reputation(self, ip_address):
        """Get IP reputation from multiple sources"""
        reputation_data = {}
        
        for platform, endpoint in self.sharing_endpoints.items():
            try:
                response = requests.get(f"{endpoint}/{ip_address}")
                if response.status_code == 200:
                    reputation_data[platform] = response.json()
            except Exception as e:
                print(f"Error getting reputation from {platform}: {e}")
        
        return reputation_data
```

## 📚 Documentation and Reporting

### Threat Intelligence Report Template
```markdown
# Threat Intelligence Report

## Executive Summary
- **Report Period**: [Date Range]
- **Total Attacks**: [Number]
- **Unique Attackers**: [Number]
- **Key Findings**: [Summary of major findings]

## Attack Analysis
### Attack Volume
- Daily attack trends
- Peak attack times
- Geographic distribution

### Attack Types
- Most targeted services
- Common attack patterns
- Emerging threats

### Attacker Behavior
- Attack techniques observed
- Tools and malware used
- Attack sophistication levels

## Threat Intelligence
### Indicators of Compromise
- IP addresses
- Domain names
- File hashes
- URLs

### Malware Analysis
- Malware families identified
- Sample analysis results
- Detection rates

### Recommendations
- Security improvements
- Monitoring enhancements
- Response procedures

## Appendices
- Raw data
- Technical details
- Methodology
```

## 🎯 Career Impact

### Skills Demonstrated
- **Threat Intelligence Collection**
- **Attack Pattern Analysis**
- **Security Monitoring**
- **Data Analysis**
- **Malware Analysis**

### Job Roles This Prepares You For
- **Threat Intelligence Analyst**
- **Security Analyst**
- **SOC Analyst**
- **Malware Analyst**
- **Security Researcher**

### Certifications This Helps With
- **GIAC GCTI** (Cyber Threat Intelligence)
- **GIAC GCFA** (Forensics)
- **SANS SEC503** (Intrusion Detection)
- **CompTIA Security+**
- **CISSP**

## 🔗 Additional Resources

- [T-Pot Documentation](https://github.com/telekom-security/tpotce)
- [Cowrie Documentation](https://github.com/cowrie/cowrie)
- [Dionaea Documentation](https://github.com/DinoTools/dionaea)
- [Threat Intelligence Platforms](https://otx.alienvault.com/)
- [Malware Analysis Tools](https://cuckoosandbox.org/)

---

**Next Project**: [Project 6: Cisco Router & Switch Security Config](../06-cisco-security/README.md)

**Previous Project**: [Project 4: Custom Nmap Automation Tool](../04-nmap-automation/README.md) 
# 🛠️ Network Security Lab Setup Guide

This guide will help you set up a complete lab environment for all 20 network security projects.

## 🖥️ System Requirements

### Minimum Requirements
- **CPU**: Intel i5/AMD Ryzen 5 or better (4+ cores)
- **RAM**: 16GB minimum, 32GB recommended
- **Storage**: 500GB SSD (1TB recommended)
- **Network**: Gigabit Ethernet or WiFi 6
- **OS**: Windows 10/11, macOS, or Linux

### Recommended Setup
- **CPU**: Intel i7/AMD Ryzen 7 (8+ cores)
- **RAM**: 64GB
- **Storage**: 2TB NVMe SSD
- **Network**: 2.5Gbps Ethernet
- **GPU**: NVIDIA GTX 1660 or better (for password cracking)

## 🏗️ Lab Architecture Overview

```
Internet
    │
    ├── pfSense Firewall (WAN/LAN)
    │
    ├── DMZ Network
    │   ├── Web Server (Apache/Nginx)
    │   ├── Mail Server (Postfix)
    │   └── Honeypot (T-Pot)
    │
    ├── Internal Network
    │   ├── Active Directory Domain Controller
    │   ├── File Server
    │   ├── Database Server
    │   └── Workstations (Windows/Linux)
    │
    ├── Security Tools Network
    │   ├── SIEM (Wazuh + ELK)
    │   ├── IDS/IPS (Snort/Suricata)
    │   ├── Vulnerability Scanner
    │   └── Monitoring Tools
    │
    └── Red Team Network (Isolated)
        ├── Kali Linux
        ├── ParrotOS
        └── Custom Attack Tools
```

## 📦 Required Software

### Virtualization Platform
- **VMware Workstation Pro** (Recommended)
- **VirtualBox** (Free alternative)
- **Hyper-V** (Windows only)

### Operating Systems
- **Windows Server 2019/2022** (Evaluation)
- **Ubuntu Server 22.04 LTS**
- **CentOS 8/Rocky Linux 8**
- **Kali Linux 2024.1**
- **pfSense CE**

### Security Tools
- **Wireshark**
- **Nmap**
- **Metasploit Framework**
- **Burp Suite Community**
- **OWASP ZAP**
- **Hashcat**
- **John the Ripper**

## 🚀 Step-by-Step Setup

### 1. Install Virtualization Software

#### VMware Workstation Pro
```bash
# Download from VMware website
# Install with default settings
# Activate with license key or use trial
```

#### VirtualBox (Free Alternative)
```bash
# Download from virtualbox.org
# Install with default settings
# Install VirtualBox Extension Pack
```

### 2. Create Base VM Templates

#### Windows Server Template
```powershell
# Download Windows Server 2019/2022 ISO
# Create VM with 4GB RAM, 50GB storage
# Install with minimal features
# Run Windows Updates
# Install VMware Tools/VirtualBox Guest Additions
# Create snapshot as "Base Windows Server"
```

#### Ubuntu Server Template
```bash
# Download Ubuntu Server 22.04 LTS ISO
# Create VM with 2GB RAM, 20GB storage
# Install with OpenSSH Server
# Update system: sudo apt update && sudo apt upgrade
# Install VMware Tools/VirtualBox Guest Additions
# Create snapshot as "Base Ubuntu Server"
```

### 3. Network Configuration

#### Create Virtual Networks
```
VMnet1 (Host-only): 192.168.1.0/24 - Management
VMnet2 (Host-only): 192.168.2.0/24 - Internal
VMnet3 (Host-only): 192.168.3.0/24 - DMZ
VMnet4 (Host-only): 192.168.4.0/24 - Security Tools
VMnet5 (Host-only): 192.168.5.0/24 - Red Team (Isolated)
```

### 4. Install pfSense Firewall

```bash
# Download pfSense CE ISO
# Create VM with 2GB RAM, 20GB storage
# Configure network interfaces:
#   - WAN: VMnet0 (NAT)
#   - LAN: VMnet2 (Internal)
#   - DMZ: VMnet3
#   - Security: VMnet4
# Configure basic firewall rules
# Enable DHCP for each network
```

### 5. Set Up Active Directory

```powershell
# Clone Windows Server template
# Promote to Domain Controller
# Create domain: lab.local
# Create organizational units:
#   - Users
#   - Computers
#   - Servers
#   - Security Groups
# Create test users and groups
```

### 6. Install Security Tools

#### SIEM Stack (Wazuh + ELK)
```bash
# Ubuntu Server VM
sudo apt update
sudo apt install docker.io docker-compose
git clone https://github.com/wazuh/wazuh-docker.git
cd wazuh-docker
docker-compose up -d
```

#### IDS/IPS (Snort)
```bash
# Ubuntu Server VM
sudo apt install snort
sudo cp /etc/snort/snort.conf /etc/snort/snort.conf.backup
# Configure snort.conf for your network
sudo systemctl enable snort
sudo systemctl start snort
```

### 7. Create Attack Lab Environment

#### Kali Linux Setup
```bash
# Download Kali Linux ISO
# Create VM with 4GB RAM, 50GB storage
# Install with default tools
# Update system: sudo apt update && sudo apt upgrade
# Install additional tools:
sudo apt install gobuster dirb nikto sqlmap
```

#### Windows 10 Target
```powershell
# Clone Windows 10 template
# Join to lab.local domain
# Install vulnerable applications
# Disable Windows Defender (for testing)
# Create snapshot as "Vulnerable Windows 10"
```

## 🔧 Network Configuration Details

### pfSense Firewall Rules

#### WAN to DMZ
```
Action: Pass
Protocol: TCP
Source: Any
Destination: DMZ Web Server
Port: 80, 443
```

#### Internal to Internet
```
Action: Pass
Protocol: Any
Source: Internal Network
Destination: Any
Port: Any
```

#### Red Team to Internal (Blocked)
```
Action: Block
Protocol: Any
Source: Red Team Network
Destination: Internal Network
Port: Any
```

### VLAN Configuration

#### Switch Configuration (Cisco Packet Tracer)
```
vlan 10
 name Internal
vlan 20
 name DMZ
vlan 30
 name Security
vlan 40
 name RedTeam

interface vlan 10
 ip address 192.168.2.1 255.255.255.0
interface vlan 20
 ip address 192.168.3.1 255.255.255.0
interface vlan 30
 ip address 192.168.4.1 255.255.255.0
interface vlan 40
 ip address 192.168.5.1 255.255.255.0
```

## 📊 Monitoring Setup

### Wazuh Configuration
```yaml
# /etc/ossec/ossec.conf
<ossec_config>
  <cluster>
    <name>lab-cluster</name>
    <node_name>wazuh-manager</node_name>
    <node_type>master</node_type>
    <key>your-cluster-key</key>
    <port>1516</port>
    <bind_addr>0.0.0.0</bind_addr>
    <nodes>
      <node>192.168.4.10</node>
    </nodes>
  </cluster>
</ossec_config>
```

### ELK Stack Configuration
```yaml
# docker-compose.yml
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
    depends_on:
      - elasticsearch
```

## 🔒 Security Considerations

### Lab Isolation
- **Never connect lab to production networks**
- **Use separate physical network if possible**
- **Disable internet access for Red Team VMs**
- **Regular snapshots before testing**

### Data Protection
- **Use dummy data for testing**
- **Never use real credentials**
- **Encrypt sensitive lab data**
- **Regular backups of configurations**

### Legal Compliance
- **Only test on your own systems**
- **Follow responsible disclosure**
- **Document all testing activities**
- **Respect privacy and data protection laws**

## 🧪 Testing Your Setup

### Basic Connectivity Test
```bash
# From Kali Linux
ping 192.168.2.10  # Internal network
ping 192.168.3.10  # DMZ network
ping 8.8.8.8       # Internet (should work)
```

### Security Tool Verification
```bash
# Test Wazuh
curl -u admin:admin http://192.168.4.10:55000

# Test Snort
sudo snort -T -c /etc/snort/snort.conf

# Test pfSense
https://192.168.2.1 (admin/pfsense)
```

## 📚 Next Steps

1. **Complete the setup verification**
2. **Create documentation for your lab**
3. **Start with Project 1: Enterprise Firewall Lab**
4. **Join cybersecurity communities for support**
5. **Consider pursuing relevant certifications**

## 🆘 Troubleshooting

### Common Issues
- **VM networking problems**: Check virtual network settings
- **Performance issues**: Allocate more RAM/CPU to VMs
- **Tool installation failures**: Check dependencies and permissions
- **Firewall blocking**: Verify pfSense rules and NAT settings

### Getting Help
- **Documentation**: Check official tool documentation
- **Forums**: Reddit r/netsec, Stack Overflow
- **Communities**: Discord cybersecurity servers
- **Vendor Support**: For commercial tools

---

**Your lab is now ready for the 20 network security projects! 🚀** 
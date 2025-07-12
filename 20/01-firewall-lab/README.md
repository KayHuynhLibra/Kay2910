# 🔥 Project 1: Enterprise Firewall Lab Setup

## 📋 Project Overview

Set up and configure enterprise-grade firewalls (pfSense and FortiGate) to understand network security fundamentals, traffic filtering, and advanced security features.

**Difficulty**: Beginner  
**Time Required**: 4-6 hours  
**Skills Gained**: Network Security, Firewall Administration, Traffic Analysis

## 🎯 Learning Objectives

- Configure enterprise firewall solutions
- Implement network segmentation
- Set up VPN connections
- Configure intrusion prevention
- Monitor and analyze network traffic
- Implement security policies

## 🛠️ Required Tools

### Software
- **pfSense CE** (Free)
- **FortiGate VM** (Free trial)
- **VMware Workstation/VirtualBox**
- **Wireshark** (for traffic analysis)

### Hardware Requirements
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 20GB per firewall VM
- **Network**: Multiple virtual network adapters

## 🚀 Step-by-Step Implementation

### Phase 1: pfSense Setup

#### 1.1 Download and Install pfSense
```bash
# Download pfSense CE ISO from pfsense.org
# Create VM with specifications:
# - 2GB RAM
# - 20GB storage
# - 2 network adapters (WAN/LAN)
# - 1 network adapter (DMZ - optional)

# Boot from ISO and install
# Choose "Install pfSense"
# Accept defaults for disk partitioning
# Set root password
# Configure network interfaces
```

#### 1.2 Initial Configuration
```bash
# Access pfSense web interface
# URL: https://192.168.1.1
# Default credentials: admin/pfsense

# Run setup wizard:
# 1. Set hostname: pfsense-lab
# 2. Set domain: lab.local
# 3. Configure DNS servers: 8.8.8.8, 8.8.4.4
# 4. Set timezone
# 5. Configure WAN interface (DHCP)
# 6. Configure LAN interface: 192.168.2.1/24
```

#### 1.3 Basic Firewall Rules
```bash
# Navigate to Firewall > Rules > LAN
# Create rules for internal network:

# Rule 1: Allow LAN to Internet
Action: Pass
Protocol: Any
Source: LAN net
Destination: Any
Port: Any
Description: "Allow LAN to Internet"

# Rule 2: Allow LAN to DMZ
Action: Pass
Protocol: Any
Source: LAN net
Destination: DMZ net
Port: Any
Description: "Allow LAN to DMZ"

# Rule 3: Block DMZ to LAN
Action: Block
Protocol: Any
Source: DMZ net
Destination: LAN net
Port: Any
Description: "Block DMZ to LAN"
```

#### 1.4 Network Address Translation (NAT)
```bash
# Navigate to Firewall > NAT > Outbound
# Enable "Manual outbound NAT"
# Create NAT rule:
Interface: WAN
Protocol: Any
Source: LAN net
Destination: Any
Translation: Interface address
Description: "LAN to Internet NAT"
```

### Phase 2: Advanced pfSense Features

#### 2.1 Intrusion Prevention System (IPS)
```bash
# Install Snort package:
System > Package Manager > Available Packages
Search for "snort" and install

# Configure Snort:
Services > Snort > Global Settings
Enable Snort on WAN interface
Download and enable rule sets:
- Emerging Threats (ET) Open
- Snort VRT rules (free registration required)

# Configure IPS mode:
Services > Snort > WAN
Enable "IPS Mode"
Select rule categories to enable
```

#### 2.2 VPN Setup (OpenVPN)
```bash
# Install OpenVPN package
System > Package Manager > Available Packages
Search for "openvpn" and install

# Configure OpenVPN server:
VPN > OpenVPN > Servers
Add new server:
- Server mode: Remote Access (SSL/TLS + User Auth)
- Protocol: UDP
- Port: 1194
- Interface: WAN
- Local network: 192.168.2.0/24
- Certificate: Create new CA and certificate

# Create user accounts:
System > User Manager
Add users with certificates
```

#### 2.3 Traffic Shaping and QoS
```bash
# Install traffic shaper:
System > Package Manager > Available Packages
Search for "traffic shaper" and install

# Configure QoS rules:
Firewall > Traffic Shaper > By Interface
Create queues for different traffic types:
- VoIP: High priority
- Web browsing: Normal priority
- File downloads: Low priority
```

### Phase 3: FortiGate Setup

#### 3.1 Download and Install FortiGate VM
```bash
# Download FortiGate VM from Fortinet website
# Create VM with specifications:
# - 2GB RAM
# - 20GB storage
# - 3 network adapters (port1, port2, port3)

# Boot VM and access console
# Default credentials: admin/(empty)
# Set new admin password
```

#### 3.2 Initial FortiGate Configuration
```bash
# Access web interface
# URL: https://192.168.1.99
# Login with admin credentials

# Run setup wizard:
# 1. Set hostname: fortigate-lab
# 2. Configure interfaces:
#    - port1 (WAN): DHCP
#    - port2 (LAN): 192.168.3.1/24
#    - port3 (DMZ): 192.168.4.1/24
# 3. Set DNS servers
# 4. Configure admin access
```

#### 3.3 FortiGate Security Policies
```bash
# Navigate to Policy & Objects > Firewall Policy
# Create security policies:

# Policy 1: LAN to Internet
Name: "LAN_to_Internet"
Incoming Interface: port2 (LAN)
Outgoing Interface: port1 (WAN)
Source: all
Destination: all
Service: ALL
Action: ACCEPT
NAT: Enable
Logging: Enable

# Policy 2: Internet to DMZ
Name: "Internet_to_DMZ"
Incoming Interface: port1 (WAN)
Outgoing Interface: port3 (DMZ)
Source: all
Destination: DMZ_Web_Server
Service: HTTP, HTTPS
Action: ACCEPT
Logging: Enable
```

#### 3.4 FortiGate Advanced Features

##### Application Control
```bash
# Navigate to Security Profiles > Application Control
# Create new profile:
Name: "Standard_App_Control"
- Block: Peer-to-peer, Social media
- Monitor: Web browsing, Email
- Allow: Business applications

# Apply to firewall policies
```

##### Web Filtering
```bash
# Navigate to Security Profiles > Web Filter
# Create new profile:
Name: "Standard_Web_Filter"
- Block: Malicious websites, Adult content
- Allow: Business websites
- Monitor: Social media, Entertainment

# Apply to LAN to Internet policy
```

##### Intrusion Prevention
```bash
# Navigate to Security Profiles > Intrusion Prevention
# Create new profile:
Name: "Standard_IPS"
- Enable all signature categories
- Set action to "Block"
- Enable anomaly detection

# Apply to firewall policies
```

### Phase 4: Monitoring and Analysis

#### 4.1 pfSense Monitoring
```bash
# Dashboard monitoring:
Status > Dashboard
Monitor: CPU, Memory, Network interfaces
View: System logs, Firewall logs

# Traffic analysis:
Status > Traffic Graph
Monitor bandwidth usage by interface
Analyze traffic patterns

# Log analysis:
Status > System Logs
View: General, Firewall, DHCP, DNS logs
Filter by severity and source
```

#### 4.2 FortiGate Monitoring
```bash
# Dashboard monitoring:
Dashboard > System Status
Monitor: System resources, Network usage
View: Security events, Traffic statistics

# Log analysis:
Log & Report > Forward Traffic
View: Allowed/denied traffic
Filter by: Source, Destination, Service

# Security monitoring:
Log & Report > Security Events
Monitor: IPS alerts, Web filter blocks
View: Application control logs
```

#### 4.3 Wireshark Traffic Analysis
```bash
# Capture traffic on different interfaces:
# WAN interface: External traffic
# LAN interface: Internal traffic
# DMZ interface: Public services

# Analyze captured traffic:
# Look for: Suspicious patterns, Protocol anomalies
# Filter by: IP addresses, Ports, Protocols
# Export: PCAP files for further analysis
```

## 🧪 Testing Scenarios

### Test 1: Basic Connectivity
```bash
# From LAN client:
ping 8.8.8.8  # Internet connectivity
ping 192.168.2.1  # Gateway connectivity
nslookup google.com  # DNS resolution
```

### Test 2: Security Policy Testing
```bash
# Test firewall rules:
# From LAN to DMZ: Should work
# From DMZ to LAN: Should be blocked
# From Internet to DMZ: Only HTTP/HTTPS allowed

# Test VPN connectivity:
# Connect OpenVPN client
# Verify access to internal resources
# Test traffic routing
```

### Test 3: Intrusion Prevention
```bash
# Test IPS functionality:
# Generate suspicious traffic patterns
# Verify alerts in firewall logs
# Test signature-based detection

# Test application control:
# Attempt to access blocked applications
# Verify blocking and logging
```

## 📊 Performance Optimization

### pfSense Optimization
```bash
# System tuning:
System > Advanced > System Tunables
- net.inet.tcp.delayed_ack: 0
- net.inet.tcp.syncookies: 1
- kern.ipc.maxsockets: 65536

# Package optimization:
# Disable unused packages
# Regular system updates
# Monitor resource usage
```

### FortiGate Optimization
```bash
# System optimization:
System > Settings > Performance
- Enable hardware acceleration
- Optimize memory usage
- Configure session limits

# Policy optimization:
# Use policy ordering efficiently
# Enable policy optimization
# Regular policy cleanup
```

## 🔍 Troubleshooting

### Common pfSense Issues
```bash
# Network connectivity problems:
# Check interface configuration
# Verify firewall rules
# Test DNS resolution

# Performance issues:
# Monitor system resources
# Check for resource-intensive packages
# Optimize firewall rules
```

### Common FortiGate Issues
```bash
# Policy conflicts:
# Check policy order
# Verify interface assignments
# Test policy matching

# VPN connectivity:
# Check certificate validity
# Verify user permissions
# Test network connectivity
```

## 📈 Advanced Features

### pfSense Advanced Features
- **Captive Portal**: Guest network access control
- **Load Balancing**: Multiple WAN connections
- **High Availability**: Failover configuration
- **Multi-WAN**: Multiple internet connections
- **DNS Filtering**: Block malicious domains

### FortiGate Advanced Features
- **SD-WAN**: Software-defined wide area networking
- **SSL Inspection**: Deep packet inspection
- **Sandboxing**: Advanced threat protection
- **Fabric Integration**: Security fabric deployment
- **Zero Trust**: Identity-based access control

## 📚 Documentation and Reporting

### Create Documentation
```markdown
# Firewall Configuration Documentation

## Network Topology
- WAN: Internet connection
- LAN: Internal network (192.168.2.0/24)
- DMZ: Public services (192.168.3.0/24)

## Security Policies
- LAN to Internet: Allowed with NAT
- Internet to DMZ: HTTP/HTTPS only
- DMZ to LAN: Blocked

## VPN Configuration
- OpenVPN server on port 1194
- Certificate-based authentication
- Split tunneling enabled

## Monitoring Setup
- Log aggregation configured
- Alert thresholds set
- Regular backup schedule
```

### Performance Report
```markdown
# Firewall Performance Report

## Throughput Testing
- LAN to WAN: 100 Mbps
- WAN to DMZ: 50 Mbps
- VPN throughput: 25 Mbps

## Resource Utilization
- CPU: 15% average
- Memory: 45% average
- Disk: 20% used

## Security Events
- Blocked connections: 1,234
- IPS alerts: 56
- VPN connections: 12 active
```

## 🎯 Career Impact

### Skills Demonstrated
- **Network Security Architecture**
- **Firewall Administration**
- **VPN Configuration**
- **Traffic Analysis**
- **Security Policy Implementation**

### Job Roles This Prepares You For
- **Network Security Engineer**
- **Firewall Administrator**
- **Security Analyst**
- **Network Administrator**
- **Infrastructure Security Specialist**

### Certifications This Helps With
- **CompTIA Security+**
- **Cisco CCNA Security**
- **Fortinet NSE4**
- **Juniper JNCIS-SEC**

## 🔗 Additional Resources

- [pfSense Documentation](https://docs.netgate.com/)
- [FortiGate Documentation](https://docs.fortinet.com/)
- [Network Security Best Practices](https://www.sans.org/)
- [Firewall Configuration Guides](https://www.nist.gov/)

---

**Next Project**: [Project 2: Wireshark Deep Packet Analysis Report](../02-wireshark-analysis/README.md)

**Previous Project**: [Setup Guide](../setup-guide.md) 
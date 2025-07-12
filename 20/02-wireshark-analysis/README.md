# 🔍 Project 2: Wireshark Deep Packet Analysis Report

## 📋 Project Overview

Master Wireshark for deep packet analysis, create comprehensive security reports, and develop skills in network forensics and threat detection through hands-on packet capture and analysis.

**Difficulty**: Beginner-Intermediate  
**Time Required**: 6-8 hours  
**Skills Gained**: Network Forensics, Packet Analysis, Security Reporting, Threat Detection

## 🎯 Learning Objectives

- Master Wireshark interface and filtering techniques
- Analyze network protocols and traffic patterns
- Identify security threats and anomalies
- Create professional security analysis reports
- Perform network forensics investigations
- Detect malware and attack signatures

## 🛠️ Required Tools

### Software
- **Wireshark** (Latest version)
- **tcpdump** (Command-line capture)
- **tshark** (Wireshark CLI)
- **NetworkMiner** (File extraction)
- **CapAnalysis** (Traffic analysis)

### Sample PCAP Files
- **Malware traffic samples**
- **Attack scenarios**
- **Normal network traffic**
- **Protocol-specific captures**

## 🚀 Step-by-Step Implementation

### Phase 1: Wireshark Fundamentals

#### 1.1 Installation and Setup
```bash
# Download Wireshark from wireshark.org
# Install with default settings
# Install WinPcap/Npcap for packet capture

# Verify installation:
wireshark --version
tshark --version

# Configure preferences:
Edit > Preferences > Capture
- Set default interface
- Configure capture filters
- Set display filters
```

#### 1.2 Basic Interface Navigation
```bash
# Main Wireshark interface components:
# 1. Menu Bar: File, Edit, View, Capture, Analyze, Statistics
# 2. Toolbar: Quick access to common functions
# 3. Filter Bar: Display and capture filters
# 4. Packet List: Overview of captured packets
# 5. Packet Details: Detailed packet information
# 6. Packet Bytes: Raw packet data in hex/ASCII

# Keyboard shortcuts:
# Ctrl+K: Start capture
# Ctrl+E: Stop capture
# Ctrl+R: Reload capture file
# Ctrl+F: Find packets
```

#### 1.3 Capture Configuration
```bash
# Capture options:
Capture > Options
- Interface selection
- Capture filters
- Buffer size settings
- Ring buffer configuration

# Example capture filters:
# Capture HTTP traffic only:
port 80 or port 443

# Capture traffic to/from specific IP:
host 192.168.1.100

# Capture DNS queries:
port 53

# Capture ARP traffic:
arp
```

### Phase 2: Advanced Filtering Techniques

#### 2.1 Display Filters
```bash
# Basic display filters:
# Filter by IP address:
ip.addr == 192.168.1.100
ip.src == 192.168.1.100
ip.dst == 192.168.1.100

# Filter by protocol:
tcp
udp
http
dns
ftp

# Filter by port:
tcp.port == 80
udp.port == 53
tcp.port == 443 or tcp.port == 80

# Filter by packet size:
frame.len > 1000
frame.len < 100

# Filter by time:
frame.time >= "2024-01-01 10:00:00"
frame.time <= "2024-01-01 11:00:00"
```

#### 2.2 Complex Filtering
```bash
# Compound filters:
# HTTP traffic from specific IP:
http and ip.src == 192.168.1.100

# Failed TCP connections:
tcp.flags.syn == 1 and tcp.flags.ack == 0

# DNS queries for specific domain:
dns.qry.name contains "google.com"

# HTTP POST requests:
http.request.method == "POST"

# SSL/TLS handshakes:
ssl.handshake

# ICMP ping requests:
icmp.type == 8

# ARP requests:
arp.opcode == 1
```

#### 2.3 Custom Filters and Expressions
```bash
# Create custom filter buttons:
# Right-click filter bar > Add Filter Expression
# Name: "Suspicious Traffic"
# Expression: tcp.flags.syn == 1 and tcp.flags.ack == 0 or icmp.type == 8

# Use expressions in filters:
# TCP retransmissions:
tcp.analysis.retransmission

# TCP window scaling:
tcp.window_size > 65535

# HTTP user agents:
http.user_agent contains "bot"

# DNS response codes:
dns.flags.rcode != 0
```

### Phase 3: Protocol Analysis

#### 3.1 TCP/IP Analysis
```bash
# TCP connection analysis:
# Follow TCP stream:
Right-click packet > Follow > TCP Stream

# TCP flags analysis:
tcp.flags.syn == 1    # SYN flag
tcp.flags.ack == 1    # ACK flag
tcp.flags.fin == 1    # FIN flag
tcp.flags.rst == 1    # RST flag
tcp.flags.psh == 1    # PSH flag
tcp.flags.urg == 1    # URG flag

# TCP handshake analysis:
# Three-way handshake:
# 1. SYN packet
# 2. SYN-ACK packet
# 3. ACK packet

# TCP teardown analysis:
# Four-way handshake:
# 1. FIN packet
# 2. ACK packet
# 3. FIN packet
# 4. ACK packet
```

#### 3.2 HTTP/HTTPS Analysis
```bash
# HTTP analysis:
# Filter HTTP requests:
http.request

# Filter HTTP responses:
http.response

# Analyze HTTP methods:
http.request.method == "GET"
http.request.method == "POST"
http.request.method == "PUT"
http.request.method == "DELETE"

# Analyze HTTP status codes:
http.response.code == 200
http.response.code == 404
http.response.code == 500

# Extract HTTP headers:
http.request.header
http.response.header

# Analyze cookies:
http.cookie
```

#### 3.3 DNS Analysis
```bash
# DNS query analysis:
# Filter DNS queries:
dns.qry.type == 1    # A record
dns.qry.type == 28   # AAAA record
dns.qry.type == 5    # CNAME record
dns.qry.type == 15   # MX record
dns.qry.type == 16   # TXT record

# DNS response analysis:
dns.flags.rcode == 0     # No error
dns.flags.rcode == 3     # NXDOMAIN
dns.flags.rcode == 2     # Server failure

# DNS tunneling detection:
# Look for:
# - Unusual DNS query lengths
# - Base64 encoded data
# - Unusual query patterns
# - High frequency DNS requests
```

### Phase 4: Security Analysis

#### 4.1 Malware Traffic Analysis
```bash
# Common malware indicators:
# 1. Beaconing behavior:
#    - Regular outbound connections
#    - Consistent time intervals
#    - Small data transfers

# Filter for beaconing:
tcp and frame.time_delta > 30 and frame.time_delta < 300

# 2. Command and Control (C2):
#    - HTTP POST requests with data
#    - DNS tunneling
#    - Encrypted traffic patterns

# Filter for C2 traffic:
http.request.method == "POST" and http.content_length > 1000

# 3. Data exfiltration:
#    - Large outbound transfers
#    - Unusual protocols
#    - Encrypted data streams

# Filter for data exfiltration:
tcp.len > 1000 and ip.dst != 192.168.0.0/16
```

#### 4.2 Attack Pattern Detection
```bash
# Port scanning detection:
# SYN scans:
tcp.flags.syn == 1 and tcp.flags.ack == 0

# UDP scans:
udp and udp.length > 0

# Service enumeration:
# Multiple connections to different ports
# Short connection durations
# RST responses

# Brute force attacks:
# Multiple failed authentication attempts
# Rapid connection attempts
# Failed login patterns

# DDoS detection:
# High volume of traffic
# SYN floods
# UDP floods
# ICMP floods
```

#### 4.3 Network Anomalies
```bash
# Unusual traffic patterns:
# 1. Protocol violations:
#    - Malformed packets
#    - Invalid checksums
#    - Wrong port usage

# 2. Timing anomalies:
#    - Unusual connection timing
#    - Burst traffic
#    - Irregular patterns

# 3. Volume anomalies:
#    - Traffic spikes
#    - Unusual bandwidth usage
#    - Protocol distribution changes

# Filter for anomalies:
# High packet rates:
frame.time_delta < 0.001

# Large packet sizes:
frame.len > 1500

# Unusual protocols:
not (tcp or udp or icmp or arp)
```

### Phase 5: Advanced Analysis Techniques

#### 5.1 Statistical Analysis
```bash
# Use Wireshark statistics:
Statistics > Protocol Hierarchy
# Shows protocol distribution

Statistics > Conversations
# Shows communication patterns

Statistics > Endpoints
# Shows traffic by endpoint

Statistics > IO Graphs
# Shows traffic over time

Statistics > Flow Graph
# Shows connection flows
```

#### 5.2 Expert Information
```bash
# Analyze expert information:
Analyze > Expert Information
# Shows:
# - Errors
# - Warnings
# - Notes
# - Chats

# Common expert messages:
# - TCP retransmissions
# - Duplicate ACKs
# - Window size changes
# - Connection resets
```

#### 5.3 Custom Columns and Profiles
```bash
# Create custom columns:
Edit > Preferences > Columns
# Add columns for:
# - Source port
# - Destination port
# - Protocol
# - Length
# - Info

# Create custom profiles:
Edit > Configuration Profiles
# Save different configurations for:
# - Security analysis
# - Performance monitoring
# - Protocol analysis
```

### Phase 6: Report Generation

#### 6.1 Export and Documentation
```bash
# Export packet data:
File > Export Packet Dissections
# Options:
# - As Plain Text
# - As CSV
# - As XML
# - As JSON

# Export specific packets:
# Select packets > File > Export Selected Packet Dissections

# Export conversation data:
Statistics > Conversations > Export
```

#### 6.2 Professional Report Template
```markdown
# Network Security Analysis Report

## Executive Summary
- Analysis period: [Date/Time]
- Total packets analyzed: [Number]
- Key findings: [Summary]
- Risk level: [Low/Medium/High/Critical]

## Methodology
- Capture method: [Interface/File]
- Analysis tools: [Wireshark version, plugins]
- Filter criteria: [Filters used]
- Time period: [Start - End]

## Traffic Overview
- Total traffic volume: [MB/GB]
- Protocol distribution: [Chart/Table]
- Top talkers: [IP addresses]
- Peak traffic times: [Timestamps]

## Security Findings

### 1. Suspicious Activity
- **Finding**: [Description]
- **Evidence**: [Packet numbers, timestamps]
- **Risk**: [Assessment]
- **Recommendation**: [Action items]

### 2. Protocol Anomalies
- **Finding**: [Description]
- **Evidence**: [Details]
- **Impact**: [Assessment]
- **Recommendation**: [Action items]

### 3. Performance Issues
- **Finding**: [Description]
- **Evidence**: [Metrics]
- **Impact**: [Assessment]
- **Recommendation**: [Action items]

## Detailed Analysis

### Packet Analysis
```
Packet #1234
Time: 2024-01-01 10:30:15
Source: 192.168.1.100:54321
Destination: 10.0.0.1:80
Protocol: TCP
Length: 1024 bytes
Flags: SYN
Analysis: Initial connection attempt
```

### Conversation Analysis
```
Conversation: 192.168.1.100 ↔ 10.0.0.1
Duration: 45 seconds
Packets: 150
Bytes: 15,000
Protocol: HTTP
Analysis: Normal web browsing session
```

## Recommendations
1. **Immediate Actions**: [Priority items]
2. **Short-term**: [Next 30 days]
3. **Long-term**: [Next 90 days]

## Appendices
- Raw packet data
- Filter expressions used
- Tool configurations
- Reference materials
```

## 🧪 Practical Exercises

### Exercise 1: Basic Traffic Analysis
```bash
# Capture normal web browsing:
# 1. Start Wireshark capture
# 2. Browse to google.com
# 3. Stop capture after 2 minutes
# 4. Analyze:
#    - DNS queries
#    - TCP handshakes
#    - HTTP requests/responses
#    - Connection teardown

# Questions to answer:
# - How many DNS queries were made?
# - What was the TCP handshake sequence?
# - What HTTP status codes were received?
# - How long did connections last?
```

### Exercise 2: Security Incident Analysis
```bash
# Analyze suspicious PCAP file:
# 1. Load provided PCAP file
# 2. Apply security filters
# 3. Identify:
#    - Malicious traffic patterns
#    - Attack signatures
#    - Data exfiltration attempts
#    - Command and control traffic

# Create incident report with:
# - Timeline of events
# - Attack vectors used
# - Impact assessment
# - Remediation steps
```

### Exercise 3: Performance Analysis
```bash
# Analyze network performance:
# 1. Capture during file transfer
# 2. Analyze:
#    - Bandwidth utilization
#    - Packet loss
#    - Retransmissions
#    - Window scaling

# Create performance report with:
# - Throughput measurements
# - Latency analysis
# - Bottleneck identification
# - Optimization recommendations
```

## 📊 Advanced Techniques

### Custom Dissectors
```lua
-- Create custom protocol dissector
local my_protocol = Proto("MyProtocol", "My Custom Protocol")

local fields = {
    version = ProtoField.uint8("my.version", "Version"),
    length = ProtoField.uint16("my.length", "Length"),
    data = ProtoField.bytes("my.data", "Data")
}

my_protocol.fields = fields

function my_protocol.dissector(buffer, pinfo, tree)
    local subtree = tree:add(my_protocol, buffer())
    
    local version = buffer(0, 1):uint()
    local length = buffer(1, 2):uint()
    
    subtree:add(fields.version, buffer(0, 1))
    subtree:add(fields.length, buffer(1, 2))
    subtree:add(fields.data, buffer(3, length))
    
    pinfo.cols.protocol = "MyProtocol"
end

DissectorTable.get("tcp.port"):add(12345, my_protocol)
```

### Automated Analysis Scripts
```python
#!/usr/bin/env python3
import pyshark
import pandas as pd

def analyze_pcap(pcap_file):
    cap = pyshark.FileCapture(pcap_file)
    
    data = []
    for packet in cap:
        try:
            data.append({
                'time': packet.sniff_timestamp,
                'source': packet.ip.src,
                'destination': packet.ip.dst,
                'protocol': packet.transport_layer,
                'length': packet.length
            })
        except:
            continue
    
    df = pd.DataFrame(data)
    
    # Analysis
    print("Top talkers:")
    print(df.groupby('source')['length'].sum().sort_values(ascending=False).head())
    
    print("\nProtocol distribution:")
    print(df['protocol'].value_counts())
    
    cap.close()

# Usage
analyze_pcap('capture.pcap')
```

## 🔍 Troubleshooting

### Common Issues
```bash
# No packets captured:
# 1. Check interface permissions
# 2. Verify interface is active
# 3. Check capture filters
# 4. Ensure WinPcap/Npcap is installed

# Performance issues:
# 1. Use capture filters
# 2. Limit buffer size
# 3. Use ring buffer
# 4. Close unnecessary applications

# Display issues:
# 1. Clear display filters
# 2. Reset column layout
# 3. Reload capture file
# 4. Check Wireshark version
```

### Performance Optimization
```bash
# Capture optimization:
# 1. Use hardware timestamping
# 2. Increase buffer size
# 3. Use multiple capture threads
# 4. Filter at capture time

# Analysis optimization:
# 1. Use display filters
# 2. Limit packet range
# 3. Use statistics instead of packet analysis
# 4. Export data for external analysis
```

## 📈 Career Impact

### Skills Demonstrated
- **Network Protocol Analysis**
- **Security Incident Response**
- **Forensic Investigation**
- **Technical Documentation**
- **Threat Detection**

### Job Roles This Prepares You For
- **Network Security Analyst**
- **Security Incident Responder**
- **Digital Forensics Analyst**
- **Network Administrator**
- **Security Engineer**

### Certifications This Helps With
- **CompTIA Security+**
- **Cisco CCNA Security**
- **GIAC GCFA (Forensics)**
- **EC-Council CEH**
- **SANS SEC503**

## 🔗 Additional Resources

- [Wireshark Documentation](https://www.wireshark.org/docs/)
- [Wireshark University](https://www.wireshark.org/learn/)
- [Network Forensics Resources](https://www.sans.org/)
- [PCAP Analysis Tools](https://github.com/topics/pcap-analysis)

---

**Next Project**: [Project 3: Secure Network Architecture Design](../03-network-architecture/README.md)

**Previous Project**: [Project 1: Enterprise Firewall Lab Setup](../01-firewall-lab/README.md) 
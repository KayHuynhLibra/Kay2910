# 🔒 Project 6: Cisco Router & Switch Security Config

## 📋 Project Overview

Configure and secure Cisco routers and switches using Packet Tracer, implementing enterprise-grade security features including access control, VLANs, port security, and monitoring.

**Difficulty**: Beginner-Intermediate  
**Time Required**: 6-8 hours  
**Skills Gained**: Cisco IOS, Network Security, VLAN Configuration, Access Control

## 🎯 Learning Objectives

- Configure Cisco IOS security features
- Implement VLAN segmentation and security
- Set up access control lists (ACLs)
- Configure port security and storm control
- Implement secure management access
- Monitor and log security events

## 🛠️ Required Tools

### Software
- **Cisco Packet Tracer** (Free)
- **GNS3** (Alternative)
- **Cisco IOS Images** (for GNS3)
- **Wireshark** (for traffic analysis)

### Hardware Requirements
- **CPU**: 4+ cores recommended
- **RAM**: 8GB minimum
- **Storage**: 10GB free space
- **Network**: Internet connection for downloads

## 🚀 Step-by-Step Implementation

### Phase 1: Packet Tracer Setup

#### 1.1 Download and Install
```bash
# Download Cisco Packet Tracer
# Visit: https://www.netacad.com/courses/packet-tracer
# Create free account and download Packet Tracer

# System Requirements:
# - Windows 10/11, macOS 10.14+, or Linux
# - 4GB RAM minimum
# - 1GB free disk space
# - 1024x768 display resolution
```

#### 1.2 Initial Network Topology
```bash
# Create basic network topology:
# - 2x Cisco 2960 Switches
# - 2x Cisco 4321 Routers
# - 4x PCs (2 per VLAN)
# - 1x Server (Management)

# Network addressing:
# - Management Network: 192.168.1.0/24
# - VLAN 10 (Sales): 192.168.10.0/24
# - VLAN 20 (Engineering): 192.168.20.0/24
# - VLAN 30 (Guest): 192.168.30.0/24
```

### Phase 2: Basic Switch Security Configuration

#### 2.1 Switch Initial Configuration
```cisco
! Switch 1 Configuration
enable
configure terminal

! Set hostname
hostname SW1

! Set enable secret
enable secret Cisco123!

! Configure console access
line console 0
password console123
login
exit

! Configure vty access
line vty 0 15
password telnet123
login
exit

! Configure management interface
interface vlan 1
ip address 192.168.1.10 255.255.255.0
no shutdown
exit

! Set default gateway
ip default-gateway 192.168.1.1

! Save configuration
write memory
```

#### 2.2 VLAN Configuration
```cisco
! Create VLANs
vlan 10
name Sales
vlan 20
name Engineering
vlan 30
name Guest
vlan 99
name Management
exit

! Configure trunk ports
interface gigabitEthernet 0/1
switchport mode trunk
switchport trunk allowed vlan 10,20,30,99
exit

! Configure access ports
interface range gigabitEthernet 0/2-5
switchport mode access
switchport access vlan 10
exit

interface range gigabitEthernet 0/6-9
switchport mode access
switchport access vlan 20
exit

interface range gigabitEthernet 0/10-13
switchport mode access
switchport access vlan 30
exit
```

#### 2.3 Port Security Configuration
```cisco
! Enable port security on access ports
interface range gigabitEthernet 0/2-13
switchport port-security
switchport port-security maximum 2
switchport port-security violation restrict
switchport port-security aging time 2
switchport port-security aging type inactivity
exit

! Configure sticky MAC addresses
interface gigabitEthernet 0/2
switchport port-security mac-address sticky
exit

! Verify port security
show port-security
show port-security address
```

### Phase 3: Advanced Switch Security

#### 3.1 Storm Control
```cisco
! Configure storm control for broadcast, multicast, and unicast
interface range gigabitEthernet 0/2-13
storm-control broadcast level 20.00
storm-control multicast level 20.00
storm-control unicast level 20.00
storm-control action shutdown
exit

! Verify storm control
show storm-control
```

#### 3.2 DHCP Snooping
```cisco
! Enable DHCP snooping
ip dhcp snooping
ip dhcp snooping vlan 10,20,30

! Configure trusted ports (connected to DHCP server)
interface gigabitEthernet 0/1
ip dhcp snooping trust
exit

! Verify DHCP snooping
show ip dhcp snooping
show ip dhcp snooping binding
```

#### 3.3 Dynamic ARP Inspection (DAI)
```cisco
! Enable DAI on VLANs
ip arp inspection vlan 10,20,30

! Configure trusted ports
interface gigabitEthernet 0/1
ip arp inspection trust
exit

! Verify DAI
show ip arp inspection
show ip arp inspection statistics
```

#### 3.4 IP Source Guard
```cisco
! Enable IP source guard on access ports
interface range gigabitEthernet 0/2-13
ip verify source
ip verify source port-security
exit

! Verify IP source guard
show ip verify source
```

### Phase 4: Router Security Configuration

#### 4.1 Router Initial Configuration
```cisco
! Router 1 Configuration
enable
configure terminal

! Set hostname
hostname R1

! Set enable secret
enable secret Router123!

! Configure console access
line console 0
password console123
login
exit

! Configure vty access with SSH
username admin privilege 15 secret Admin123!
ip domain-name company.local
crypto key generate rsa modulus 2048

line vty 0 4
transport input ssh
login local
exit

! Configure interfaces
interface gigabitEthernet 0/0/0
description WAN Interface
ip address 203.0.113.1 255.255.255.0
no shutdown
exit

interface gigabitEthernet 0/0/1
description LAN Interface
ip address 192.168.1.1 255.255.255.0
no shutdown
exit
```

#### 4.2 Access Control Lists (ACLs)
```cisco
! Standard ACL for management access
access-list 10 permit 192.168.1.0 0.0.0.255
access-list 10 deny any log

! Extended ACL for traffic filtering
access-list 100 permit tcp 192.168.10.0 0.0.0.255 any eq 80
access-list 100 permit tcp 192.168.10.0 0.0.0.255 any eq 443
access-list 100 permit tcp 192.168.20.0 0.0.0.255 any eq 22
access-list 100 permit tcp 192.168.20.0 0.0.0.255 any eq 3389
access-list 100 deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255
access-list 100 deny ip 192.168.30.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 100 permit ip any any

! Apply ACLs to interfaces
interface gigabitEthernet 0/0/1
ip access-group 100 in
exit

! Apply management ACL to vty lines
line vty 0 4
access-class 10 in
exit
```

#### 4.3 NAT Configuration
```cisco
! Configure NAT for internal networks
ip access-list standard NAT_ACL
permit 192.168.10.0 0.0.0.255
permit 192.168.20.0 0.0.0.255
permit 192.168.30.0 0.0.0.255
exit

! Configure NAT
interface gigabitEthernet 0/0/0
ip nat outside
exit

interface gigabitEthernet 0/0/1
ip nat inside
exit

ip nat inside source list NAT_ACL interface gigabitEthernet 0/0/0 overload

! Verify NAT
show ip nat translations
show ip nat statistics
```

### Phase 5: Advanced Router Security

#### 5.1 Zone-Based Firewall
```cisco
! Define security zones
zone security INSIDE
zone security OUTSIDE
zone security DMZ

! Define zone pairs
zone-pair security INSIDE-TO-OUTSIDE source INSIDE destination OUTSIDE
zone-pair security OUTSIDE-TO-INSIDE source OUTSIDE destination INSIDE

! Configure class maps
class-map type inspect match-all INSIDE-TRAFFIC
match access-group 100
exit

! Configure policy maps
policy-map type inspect INSIDE-TO-OUTSIDE-POLICY
class type inspect INSIDE-TRAFFIC
inspect
exit

! Apply zone-based firewall
zone-pair security INSIDE-TO-OUTSIDE
service-policy type inspect INSIDE-TO-OUTSIDE-POLICY
exit

! Assign interfaces to zones
interface gigabitEthernet 0/0/0
zone-member security OUTSIDE
exit

interface gigabitEthernet 0/0/1
zone-member security INSIDE
exit
```

#### 5.2 VPN Configuration
```cisco
! Configure IPsec VPN
crypto isakmp policy 10
encryption aes
authentication pre-share
group 2
lifetime 3600
exit

crypto isakmp key VPN_KEY address 203.0.113.2

crypto ipsec transform-set ESP-AES-SHA esp-aes esp-sha-hmac
exit

crypto map VPN_MAP 10 ipsec-isakmp
set peer 203.0.113.2
set transform-set ESP-AES-SHA
match address 101
exit

! Define interesting traffic
access-list 101 permit ip 192.168.10.0 0.0.0.255 10.0.0.0 0.255.255.255
access-list 101 permit ip 192.168.20.0 0.0.0.255 10.0.0.0 0.255.255.255

! Apply crypto map
interface gigabitEthernet 0/0/0
crypto map VPN_MAP
exit
```

#### 5.3 Logging and Monitoring
```cisco
! Configure logging
logging host 192.168.1.100
logging trap informational
logging facility local6
logging source-interface gigabitEthernet 0/0/1

! Configure SNMP
snmp-server community public RO
snmp-server location "Data Center"
snmp-server contact "Network Admin"
snmp-server enable traps

! Configure NTP
ntp server 192.168.1.100
ntp update-calendar

! Configure syslog
service timestamps log datetime msec
service sequence-numbers
```

### Phase 6: Network Monitoring and Troubleshooting

#### 6.1 Monitoring Commands
```cisco
! Basic monitoring commands
show interfaces
show ip interface brief
show vlan
show spanning-tree
show port-security
show access-lists
show ip nat translations
show crypto isakmp sa
show crypto ipsec sa

! Security monitoring
show logging
show ip dhcp snooping
show ip arp inspection
show storm-control
show ip verify source

! Performance monitoring
show processes cpu
show memory statistics
show interface counters
show interface statistics
```

#### 6.2 Troubleshooting Commands
```cisco
! Troubleshooting connectivity
ping 192.168.10.1
traceroute 8.8.8.8
show ip route
show arp

! Troubleshooting VLANs
show vlan brief
show interface trunk
show spanning-tree vlan 10

! Troubleshooting security
show port-security interface gigabitEthernet 0/2
show ip dhcp snooping binding
show ip arp inspection statistics
show access-lists
```

#### 6.3 Debug Commands
```cisco
! Enable debugging (use with caution)
debug ip packet
debug ip nat
debug crypto isakmp
debug crypto ipsec

! Disable debugging
no debug all
undebug all
```

### Phase 7: Security Hardening

#### 7.1 Additional Security Features
```cisco
! Disable unnecessary services
no service pad
no service tcp-small-servers
no service udp-small-servers
no service finger
no service http
no service https

! Configure banner
banner motd ^
*** WARNING ***
This is a private system. Unauthorized access is prohibited.
All activities are logged and monitored.
^C

! Configure exec timeout
line console 0
exec-timeout 5 0
exit

line vty 0 4
exec-timeout 5 0
exit

! Configure service password-encryption
service password-encryption

! Configure login block-for
login block-for 120 attempts 3 within 60
```

#### 7.2 Interface Security
```cisco
! Configure interface security
interface range gigabitEthernet 0/2-13
switchport port-security
switchport port-security maximum 2
switchport port-security violation shutdown
switchport port-security aging time 2
switchport port-security aging type inactivity
spanning-tree portfast
spanning-tree bpduguard enable
exit

! Configure unused ports
interface range gigabitEthernet 0/14-24
shutdown
switchport mode access
switchport access vlan 99
exit
```

## 🧪 Testing and Validation

### Security Testing Scenarios
```bash
# Test VLAN isolation
# From VLAN 10, try to ping VLAN 20
ping 192.168.20.1

# Test port security
# Connect unauthorized device to secured port
# Verify port shutdown

# Test ACL filtering
# Try to access blocked services
telnet 192.168.10.1 23

# Test DHCP snooping
# Connect rogue DHCP server
# Verify DHCP snooping blocks it

# Test storm control
# Generate broadcast storm
# Verify storm control activates
```

### Performance Testing
```bash
# Test network performance
# Measure throughput between VLANs
# Test latency and jitter
# Monitor CPU and memory usage

# Test security features
# Measure impact of security features on performance
# Test failover scenarios
# Validate backup and recovery procedures
```

## 📊 Configuration Examples

### Complete Switch Configuration
```cisco
! Complete Switch 1 Configuration
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname SW1
!
enable secret 5 $1$mERr$hx5rVt7rPNoS4wqbXKX7m0
!
username admin privilege 15 secret 5 $1$mERr$hx5rVt7rPNoS4wqbXKX7m0
!
ip dhcp snooping
ip dhcp snooping vlan 10,20,30
!
vlan 10
 name Sales
vlan 20
 name Engineering
vlan 30
 name Guest
vlan 99
 name Management
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,99
 switchport trunk native vlan 99
!
interface range GigabitEthernet0/2-5
 switchport mode access
 switchport access vlan 10
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security aging time 2
 switchport port-security aging type inactivity
 storm-control broadcast level 20.00
 storm-control multicast level 20.00
 storm-control unicast level 20.00
 storm-control action shutdown
 spanning-tree portfast
 spanning-tree bpduguard enable
!
interface range GigabitEthernet0/6-9
 switchport mode access
 switchport access vlan 20
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security aging time 2
 switchport port-security aging type inactivity
 storm-control broadcast level 20.00
 storm-control multicast level 20.00
 storm-control unicast level 20.00
 storm-control action shutdown
 spanning-tree portfast
 spanning-tree bpduguard enable
!
interface range GigabitEthernet0/10-13
 switchport mode access
 switchport access vlan 30
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security aging time 2
 switchport port-security aging type inactivity
 storm-control broadcast level 20.00
 storm-control multicast level 20.00
 storm-control unicast level 20.00
 storm-control action shutdown
 spanning-tree portfast
 spanning-tree bpduguard enable
!
interface Vlan1
 ip address 192.168.1.10 255.255.255.0
!
ip default-gateway 192.168.1.1
!
line con 0
 password console123
 login
 exec-timeout 5 0
!
line vty 0 4
 password telnet123
 login
 exec-timeout 5 0
!
line vty 5 15
 password telnet123
 login
 exec-timeout 5 0
!
end
```

### Complete Router Configuration
```cisco
! Complete Router 1 Configuration
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname R1
!
boot-start-marker
boot-end-marker
!
enable secret 5 $1$mERr$hx5rVt7rPNoS4wqbXKX7m0
!
no aaa new-model
!
ip domain-name company.local
ip name-server 8.8.8.8
!
username admin privilege 15 secret 5 $1$mERr$hx5rVt7rPNoS4wqbXKX7m0
!
crypto pki token default removal timeout 0
!
license udi pid CISCO4321/K9 sn FGL12345678
!
redundancy
!
interface GigabitEthernet0/0/0
 description WAN Interface
 ip address 203.0.113.1 255.255.255.0
 ip nat outside
 ip virtual-reassembly in
 duplex auto
 speed auto
!
interface GigabitEthernet0/0/1
 description LAN Interface
 ip address 192.168.1.1 255.255.255.0
 ip nat inside
 ip virtual-reassembly in
 duplex auto
 speed auto
!
router ospf 1
 network 192.168.1.0 0.0.0.255 area 0
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
ip access-list standard NAT_ACL
 permit 192.168.10.0 0.0.0.255
 permit 192.168.20.0 0.0.0.255
 permit 192.168.30.0 0.0.0.255
!
access-list 10 permit 192.168.1.0 0.0.0.255
access-list 10 deny any log
!
access-list 100 permit tcp 192.168.10.0 0.0.0.255 any eq 80
access-list 100 permit tcp 192.168.10.0 0.0.0.255 any eq 443
access-list 100 permit tcp 192.168.20.0 0.0.0.255 any eq 22
access-list 100 permit tcp 192.168.20.0 0.0.0.255 any eq 3389
access-list 100 deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255
access-list 100 deny ip 192.168.30.0 0.0.0.255 192.168.20.0 0.0.0.255
access-list 100 permit ip any any
!
ip nat inside source list NAT_ACL interface GigabitEthernet0/0/0 overload
!
control-plane
!
line con 0
 password console123
 login
 exec-timeout 5 0
!
line aux 0
!
line vty 0 4
 access-class 10 in
 password telnet123
 login local
 exec-timeout 5 0
 transport input ssh
!
scheduler allocate 20000 1000
!
end
```

## 🔍 Troubleshooting

### Common Issues and Solutions
```bash
# Issue: VLANs not communicating
# Solution: Check trunk configuration
show interface trunk
show vlan brief

# Issue: Port security blocking legitimate traffic
# Solution: Check MAC address bindings
show port-security address
clear port-security sticky interface gigabitEthernet 0/2

# Issue: ACL blocking required traffic
# Solution: Check ACL configuration
show access-lists
show ip interface gigabitEthernet 0/0/1

# Issue: NAT not working
# Solution: Check NAT configuration
show ip nat translations
show ip nat statistics
debug ip nat

# Issue: VPN not connecting
# Solution: Check VPN configuration
show crypto isakmp sa
show crypto ipsec sa
debug crypto isakmp
```

## 📈 Advanced Features

### Quality of Service (QoS)
```cisco
! Configure QoS for voice traffic
class-map match-all VOICE
 match dscp ef
exit

policy-map VOICE-POLICY
 class VOICE
  priority percent 20
 class class-default
  fair-queue
exit

interface gigabitEthernet 0/0/1
 service-policy output VOICE-POLICY
exit
```

### Network Time Protocol (NTP)
```cisco
! Configure NTP for time synchronization
ntp server 192.168.1.100
ntp update-calendar
ntp master 1
```

### Simple Network Management Protocol (SNMP)
```cisco
! Configure SNMP for network management
snmp-server community public RO
snmp-server community private RW
snmp-server location "Data Center"
snmp-server contact "Network Admin"
snmp-server enable traps
```

## 📚 Documentation and Reporting

### Network Documentation Template
```markdown
# Network Security Configuration Report

## Network Topology
- **Switches**: 2x Cisco 2960
- **Routers**: 2x Cisco 4321
- **VLANs**: 4 (Sales, Engineering, Guest, Management)
- **Subnets**: 4 subnets with proper segmentation

## Security Configuration
### Switch Security
- **Port Security**: Enabled on all access ports
- **Storm Control**: Configured for broadcast/multicast/unicast
- **DHCP Snooping**: Enabled on all VLANs
- **DAI**: Enabled for ARP protection
- **IP Source Guard**: Enabled on access ports

### Router Security
- **ACLs**: Standard and extended ACLs configured
- **NAT**: PAT configured for internal networks
- **VPN**: IPsec VPN configured
- **Zone-Based Firewall**: Implemented
- **Logging**: Syslog configured

## Monitoring and Management
- **SNMP**: Configured for network management
- **NTP**: Time synchronization configured
- **Logging**: Comprehensive logging enabled
- **Backup**: Configuration backups scheduled

## Compliance and Best Practices
- **Password Policy**: Strong passwords enforced
- **Access Control**: Role-based access implemented
- **Network Segmentation**: Proper VLAN isolation
- **Security Monitoring**: Continuous monitoring enabled
```

## 🎯 Career Impact

### Skills Demonstrated
- **Cisco IOS Configuration**
- **Network Security Implementation**
- **VLAN and Trunking**
- **Access Control Lists**
- **Network Troubleshooting**

### Job Roles This Prepares You For
- **Network Administrator**
- **Network Security Engineer**
- **Cisco Network Engineer**
- **Infrastructure Security Specialist**
- **Network Operations Engineer**

### Certifications This Helps With
- **Cisco CCNA**
- **Cisco CCNA Security**
- **Cisco CCNP**
- **CompTIA Network+**
- **CompTIA Security+**

## 🔗 Additional Resources

- [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer)
- [Cisco IOS Configuration Guides](https://www.cisco.com/c/en/us/support/docs/)
- [Cisco Security Configuration Guides](https://www.cisco.com/c/en/us/support/docs/security/)
- [GNS3 Network Simulator](https://www.gns3.com/)
- [Cisco Learning Network](https://learningnetwork.cisco.com/)

---

**Next Project**: [Project 7: Active Directory + LDAP Bruteforce Monitoring](../07-ad-monitoring/README.md)

**Previous Project**: [Project 5: Honeypot Deployment](../05-honeypot-deployment/README.md) 
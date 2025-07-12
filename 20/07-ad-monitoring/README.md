# 🔐 Project 7: Active Directory + LDAP Bruteforce Monitoring

## 📋 Project Overview

Implement comprehensive monitoring and detection systems for Active Directory and LDAP bruteforce attacks, including real-time alerting and automated response mechanisms.

**Difficulty**: Intermediate  
**Time Required**: 6-8 hours  
**Skills Gained**: AD Security, LDAP Monitoring, SIEM Integration, Incident Response

## 🎯 Learning Objectives

- Configure Active Directory security monitoring
- Implement LDAP attack detection
- Set up real-time alerting systems
- Create automated response mechanisms
- Analyze attack patterns and trends
- Develop incident response procedures

## 🛠️ Required Tools

### Software
- **Windows Server 2019/2022** (Domain Controller)
- **Windows 10/11** (Client machines)
- **Wazuh SIEM** (Free)
- **ELK Stack** (Elasticsearch, Logstash, Kibana)
- **PowerShell** (Scripting)
- **Python** (Custom tools)

### Hardware Requirements
- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: 100GB+ SSD
- **Network**: Internal network access

## 🚀 Step-by-Step Implementation

### Phase 1: Active Directory Setup

#### 1.1 Domain Controller Configuration
```powershell
# Install Active Directory Domain Services
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# Promote to Domain Controller
Install-ADDSForest -DomainName "lab.local" -DomainNetbiosName "LAB" -ForestMode "WinThreshold" -DomainMode "WinThreshold" -InstallDNS

# Configure audit policies
auditpol /set /category:* /success:enable /failure:enable

# Enable advanced audit policies
auditpol /set /subcategory:"Credential Validation" /success:enable /failure:enable
auditpol /set /subcategory:"Kerberos Authentication Service" /success:enable /failure:enable
auditpol /set /subcategory:"Kerberos Service Ticket Operations" /success:enable /failure:enable
auditpol /set /subcategory:"Logoff" /success:enable /failure:enable
auditpol /set /subcategory:"Logon" /success:enable /failure:enable
auditpol /set /subcategory:"Other Logon/Logoff Events" /success:enable /failure:enable
auditpol /set /subcategory:"Special Logon" /success:enable /failure:enable
```

#### 1.2 Security Policy Configuration
```powershell
# Configure account lockout policy
net accounts /lockoutthreshold:5
net accounts /lockoutduration:30
net accounts /lockoutwindow:30

# Configure password policy
net accounts /minpwlen:12
net accounts /maxpwage:90
net accounts /minpwage:1
net accounts /pwshist:24

# Configure Kerberos policy
Set-ADDefaultDomainPasswordPolicy -Identity lab.local -ComplexityEnabled $true -MinPasswordLength 12 -PasswordHistoryCount 24 -MaxPasswordAge 90.00:00:00 -LockoutDuration 0.00:30:00 -LockoutThreshold 5 -LockoutObservationWindow 0.00:30:00
```

### Phase 2: Monitoring Setup

#### 2.1 Event Log Configuration
```powershell
# Configure Windows Event Logs for security monitoring
wevtutil sl Security /ms:1024000
wevtutil sl System /ms:1024000
wevtutil sl Application /ms:1024000

# Enable detailed logging
# Security Event IDs to monitor:
# 4624 - Successful logon
# 4625 - Failed logon
# 4627 - Group membership information
# 4634 - Account logoff
# 4647 - User initiated logoff
# 4648 - Explicit credential logon
# 4672 - Special privileges assigned
# 4688 - Process creation
# 4702 - Task scheduled
# 4719 - System audit policy changed
# 4767 - User account unlocked
# 4771 - Kerberos authentication ticket request
# 4776 - Credential validation
# 4778 - Session reconnected
# 4779 - Session disconnected
# 4964 - Special groups have been assigned to a new logon
```

#### 2.2 Wazuh Agent Installation
```bash
# Install Wazuh agent on Domain Controller
# Download Wazuh agent for Windows
# Install with default settings
# Configure agent to connect to Wazuh server

# Agent configuration file: C:\Program Files (x86)\ossec-agent\ossec.conf
<ossec_config>
  <client>
    <server-ip>192.168.1.100</server-ip>
  </client>
  
  <syscheck>
    <frequency>43200</frequency>
  </syscheck>
  
  <rootcheck>
    <frequency>43200</frequency>
  </rootcheck>
  
  <localfile>
    <log_format>eventlog</log_format>
    <location>Security</location>
  </localfile>
  
  <localfile>
    <log_format>eventlog</log_format>
    <location>System</location>
  </localfile>
  
  <localfile>
    <log_format>eventlog</log_format>
    <location>Application</location>
  </localfile>
</ossec_config>
```

### Phase 3: Bruteforce Detection

#### 3.1 PowerShell Monitoring Script
```powershell
# bruteforce_monitor.ps1
param(
    [int]$Threshold = 5,
    [int]$TimeWindow = 300,
    [string]$LogFile = "C:\Logs\bruteforce_detection.log"
)

# Create log directory if it doesn't exist
$LogDir = Split-Path $LogFile -Parent
if (!(Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir -Force
}

# Function to write logs
function Write-Log {
    param([string]$Message)
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$Timestamp - $Message" | Out-File -FilePath $LogFile -Append
    Write-Host "$Timestamp - $Message"
}

# Function to get failed logon attempts
function Get-FailedLogons {
    $StartTime = (Get-Date).AddSeconds(-$TimeWindow)
    
    $Events = Get-WinEvent -FilterHashtable @{
        LogName = 'Security'
        ID = 4625
        StartTime = $StartTime
    } -ErrorAction SilentlyContinue
    
    return $Events
}

# Function to analyze bruteforce attempts
function Test-BruteforceAttack {
    $FailedLogons = Get-FailedLogons
    
    if ($FailedLogons.Count -eq 0) {
        return $null
    }
    
    # Group by source IP
    $IPGroups = $FailedLogons | Group-Object -Property {$_.Properties[19].Value}
    
    foreach ($Group in $IPGroups) {
        $IP = $Group.Name
        $Count = $Group.Count
        
        if ($Count -ge $Threshold) {
            $LastAttempt = ($Group.Group | Sort-Object TimeCreated -Descending | Select-Object -First 1).TimeCreated
            $FirstAttempt = ($Group.Group | Sort-Object TimeCreated | Select-Object -First 1).TimeCreated
            
            $AttackInfo = @{
                IP = $IP
                Count = $Count
                FirstAttempt = $FirstAttempt
                LastAttempt = $LastAttempt
                Duration = $LastAttempt - $FirstAttempt
            }
            
            Write-Log "BRUTEFORCE DETECTED: IP $IP - $Count attempts from $FirstAttempt to $LastAttempt"
            
            # Send alert
            Send-BruteforceAlert -AttackInfo $AttackInfo
            
            return $AttackInfo
        }
    }
    
    return $null
}

# Function to send alerts
function Send-BruteforceAlert {
    param([hashtable]$AttackInfo)
    
    $Subject = "BRUTEFORCE ATTACK DETECTED - $($AttackInfo.IP)"
    $Body = @"
BRUTEFORCE ATTACK DETECTED

Source IP: $($AttackInfo.IP)
Failed Attempts: $($AttackInfo.Count)
Time Window: $($AttackInfo.FirstAttempt) to $($AttackInfo.LastAttempt)
Duration: $($AttackInfo.Duration)

Action Required: Investigate and block if necessary.
"@
    
    # Send email alert (configure SMTP settings)
    # Send-MailMessage -SmtpServer "smtp.company.com" -From "security@company.com" -To "admin@company.com" -Subject $Subject -Body $Body
    
    # Log to Windows Event Log
    Write-EventLog -LogName Application -Source "BruteforceMonitor" -EventId 1001 -EntryType Warning -Message "Bruteforce attack detected from $($AttackInfo.IP)"
    
    # Block IP using Windows Firewall
    New-NetFirewallRule -DisplayName "Block Bruteforce IP $($AttackInfo.IP)" -Direction Inbound -RemoteAddress $AttackInfo.IP -Action Block -Profile Any
}

# Main monitoring loop
Write-Log "Starting bruteforce monitoring..."
Write-Log "Threshold: $Threshold attempts in $TimeWindow seconds"

while ($true) {
    try {
        $Attack = Test-BruteforceAttack
        if ($Attack) {
            Write-Log "Attack detected and blocked: $($Attack.IP)"
        }
        
        Start-Sleep -Seconds 60
    }
    catch {
        Write-Log "Error in monitoring loop: $($_.Exception.Message)"
        Start-Sleep -Seconds 60
    }
}
```

#### 3.2 Python LDAP Monitoring Tool
```python
#!/usr/bin/env python3
# ldap_monitor.py

import ldap3
import time
import json
import logging
from datetime import datetime, timedelta
from collections import defaultdict
import smtplib
from email.mime.text import MIMEText

class LDAPMonitor:
    def __init__(self, server, port=389, use_ssl=False):
        self.server = server
        self.port = port
        self.use_ssl = use_ssl
        self.failed_attempts = defaultdict(list)
        self.threshold = 5
        self.time_window = 300  # 5 minutes
        
        # Setup logging
        logging.basicConfig(
            filename='ldap_monitor.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def test_ldap_connection(self, username, password):
        """Test LDAP connection with credentials"""
        try:
            server = ldap3.Server(self.server, port=self.port, use_ssl=self.use_ssl)
            conn = ldap3.Connection(server, user=username, password=password, auto_bind=True)
            
            if conn.bound:
                logging.info(f"Successful LDAP login: {username}")
                return True
            else:
                logging.warning(f"Failed LDAP login: {username}")
                return False
                
        except Exception as e:
            logging.error(f"LDAP connection error for {username}: {e}")
            return False
    
    def monitor_bruteforce(self):
        """Monitor for bruteforce attempts"""
        while True:
            try:
                # Get current time
                now = datetime.now()
                
                # Clean old attempts
                cutoff_time = now - timedelta(seconds=self.time_window)
                for ip in list(self.failed_attempts.keys()):
                    self.failed_attempts[ip] = [
                        attempt for attempt in self.failed_attempts[ip]
                        if attempt['timestamp'] > cutoff_time
                    ]
                
                # Check for bruteforce patterns
                for ip, attempts in self.failed_attempts.items():
                    if len(attempts) >= self.threshold:
                        self.handle_bruteforce_attack(ip, attempts)
                
                time.sleep(60)  # Check every minute
                
            except KeyboardInterrupt:
                logging.info("Monitoring stopped by user")
                break
            except Exception as e:
                logging.error(f"Monitoring error: {e}")
                time.sleep(60)
    
    def handle_bruteforce_attack(self, ip, attempts):
        """Handle detected bruteforce attack"""
        logging.warning(f"BRUTEFORCE ATTACK DETECTED: {ip} - {len(attempts)} attempts")
        
        # Generate alert
        alert = {
            'timestamp': datetime.now().isoformat(),
            'type': 'bruteforce_attack',
            'source_ip': ip,
            'attempts': len(attempts),
            'time_window': self.time_window,
            'usernames_attempted': list(set(attempt['username'] for attempt in attempts))
        }
        
        # Log alert
        logging.warning(f"Alert: {json.dumps(alert)}")
        
        # Send notification
        self.send_alert(alert)
        
        # Block IP (implement your blocking mechanism)
        self.block_ip(ip)
    
    def send_alert(self, alert):
        """Send alert notification"""
        subject = f"LDAP Bruteforce Attack Detected - {alert['source_ip']}"
        body = f"""
LDAP Bruteforce Attack Detected

Source IP: {alert['source_ip']}
Attempts: {alert['attempts']}
Time Window: {alert['time_window']} seconds
Usernames Attempted: {', '.join(alert['usernames_attempted'])}

Timestamp: {alert['timestamp']}

Action Required: Investigate and block if necessary.
"""
        
        # Send email (configure your SMTP settings)
        # self.send_email(subject, body)
        
        # Log to file
        with open('ldap_alerts.log', 'a') as f:
            f.write(f"{datetime.now().isoformat()} - {json.dumps(alert)}\n")
    
    def block_ip(self, ip):
        """Block IP address"""
        logging.info(f"Blocking IP: {ip}")
        
        # Implement your IP blocking mechanism
        # Examples:
        # - Add to firewall rules
        # - Update network ACLs
        # - Add to blacklist
        
        # For Windows, you could use:
        # os.system(f'netsh advfirewall firewall add rule name="Block LDAP Bruteforce {ip}" dir=in action=block remoteip={ip}')
        
        # For Linux, you could use:
        # os.system(f'iptables -A INPUT -s {ip} -j DROP')
    
    def simulate_attack(self, ip, usernames):
        """Simulate bruteforce attack for testing"""
        for username in usernames:
            # Simulate failed login
            attempt = {
                'timestamp': datetime.now(),
                'username': username,
                'ip': ip
            }
            self.failed_attempts[ip].append(attempt)
            
            time.sleep(1)  # Small delay between attempts

# Usage example
if __name__ == "__main__":
    monitor = LDAPMonitor("192.168.1.10")
    
    # Start monitoring
    monitor.monitor_bruteforce()
```

### Phase 4: SIEM Integration

#### 4.1 Wazuh Rules Configuration
```xml
<!-- /var/ossec/etc/rules/bruteforce_rules.xml -->
<group name="bruteforce,authentication_failures,">
  <rule id="100001" level="10">
    <if_sid>0</if_sid>
    <match>^Security.*4625</match>
    <description>Windows failed logon attempt</description>
  </rule>
  
  <rule id="100002" level="12">
    <if_sid>100001</if_sid>
    <field name="win.eventdata.ipAddress">\.</field>
    <options>threshold:5,timeframe:300</options>
    <description>Multiple failed logon attempts from same IP</description>
  </rule>
  
  <rule id="100003" level="14">
    <if_sid>100002</if_sid>
    <options>threshold:10,timeframe:300</options>
    <description>Bruteforce attack detected</description>
  </rule>
  
  <rule id="100004" level="10">
    <if_sid>0</if_sid>
    <match>^Security.*4771</match>
    <description>Kerberos pre-authentication failed</description>
  </rule>
  
  <rule id="100005" level="12">
    <if_sid>100004</if_sid>
    <field name="win.eventdata.ipAddress">\.</field>
    <options>threshold:3,timeframe:300</options>
    <description>Multiple Kerberos failures from same IP</description>
  </rule>
</group>
```

#### 4.2 ELK Stack Configuration
```yaml
# logstash.conf
input {
  beats {
    port => 5044
  }
}

filter {
  if [event][dataset] == "windows.security" {
    if [win][event_id] == 4625 {
      mutate {
        add_tag => ["failed_logon"]
      }
    }
    
    if [win][event_id] == 4771 {
      mutate {
        add_tag => ["kerberos_failure"]
      }
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "windows-security-%{+YYYY.MM.dd}"
  }
}
```

### Phase 5: Automated Response

#### 5.1 PowerShell Response Script
```powershell
# automated_response.ps1
param(
    [string]$AttackerIP,
    [string]$Action = "Block"
)

# Function to block IP
function Block-IPAddress {
    param([string]$IP)
    
    # Add to Windows Firewall
    New-NetFirewallRule -DisplayName "Block Bruteforce IP $IP" -Direction Inbound -RemoteAddress $IP -Action Block -Profile Any
    
    # Add to hosts file (optional)
    Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "`n$IP 0.0.0.0"
    
    # Log the action
    Write-EventLog -LogName Application -Source "BruteforceResponse" -EventId 1002 -EntryType Information -Message "Blocked IP $IP due to bruteforce attack"
    
    Write-Host "Blocked IP: $IP"
}

# Function to unblock IP
function Unblock-IPAddress {
    param([string]$IP)
    
    # Remove from Windows Firewall
    Remove-NetFirewallRule -DisplayName "Block Bruteforce IP $IP" -ErrorAction SilentlyContinue
    
    # Remove from hosts file (optional)
    $HostsContent = Get-Content "C:\Windows\System32\drivers\etc\hosts"
    $HostsContent = $HostsContent | Where-Object { $_ -notmatch $IP }
    Set-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value $HostsContent
    
    Write-Host "Unblocked IP: $IP"
}

# Main execution
switch ($Action) {
    "Block" {
        Block-IPAddress -IP $AttackerIP
    }
    "Unblock" {
        Unblock-IPAddress -IP $AttackerIP
    }
    default {
        Write-Host "Invalid action. Use 'Block' or 'Unblock'"
    }
}
```

## 🧪 Testing and Validation

### Testing Scenarios
```bash
# Test bruteforce detection
# Use tools like Hydra or Medusa to simulate attacks
hydra -L users.txt -P passwords.txt 192.168.1.10 ldap

# Test monitoring scripts
# Run PowerShell monitoring script
.\bruteforce_monitor.ps1

# Test Python LDAP monitor
python3 ldap_monitor.py

# Verify alerts and responses
# Check log files
# Verify firewall rules
# Test email notifications
```

## 📊 Success Metrics

### Detection Metrics
- **False Positive Rate**: < 5%
- **Detection Time**: < 1 minute
- **Coverage**: 100% of authentication events
- **Alert Accuracy**: > 95%

### Response Metrics
- **Response Time**: < 5 minutes
- **Blocking Success**: > 99%
- **False Blocking**: < 1%
- **Recovery Time**: < 10 minutes

## 🎯 Career Impact

### Skills Demonstrated
- **Active Directory Security**
- **LDAP Monitoring**
- **SIEM Integration**
- **Automated Response**
- **Incident Response**

### Job Roles This Prepares You For
- **Security Analyst**
- **SOC Analyst**
- **Active Directory Administrator**
- **Security Engineer**
- **Incident Responder**

---

**Next Project**: [Project 8: IDS/IPS Setup with Snort/Suricata](../08-ids-ips-setup/README.md)

**Previous Project**: [Project 6: Cisco Router & Switch Security Config](../06-cisco-security/README.md) 
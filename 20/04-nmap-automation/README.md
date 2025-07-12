# 🔧 Project 4: Custom Nmap Automation Tool

## 📋 Project Overview

Build a custom network scanning and automation tool using Python and Nmap to perform comprehensive network reconnaissance, vulnerability assessment, and security auditing with a user-friendly CLI interface.

**Difficulty**: Intermediate  
**Time Required**: 8-10 hours  
**Skills Gained**: Python Development, Network Automation, Security Tooling, CLI Design

## 🎯 Learning Objectives

- Develop custom network scanning tools
- Integrate multiple security tools via Python
- Create user-friendly CLI interfaces
- Implement automated security workflows
- Generate comprehensive security reports
- Build reusable security automation frameworks

## 🛠️ Required Tools

### Software
- **Python 3.8+**
- **Nmap** (Latest version)
- **Git** (Version control)
- **VS Code/PyCharm** (IDE)

### Python Libraries
- **python-nmap** (Nmap integration)
- **argparse** (CLI argument parsing)
- **colorama** (Colored output)
- **rich** (Rich terminal output)
- **pandas** (Data analysis)
- **matplotlib** (Visualization)
- **sqlite3** (Database storage)

## 🚀 Step-by-Step Implementation

### Phase 1: Project Setup and Architecture

#### 1.1 Project Structure
```bash
nmap-automation-tool/
├── src/
│   ├── __init__.py
│   ├── scanner.py          # Core scanning logic
│   ├── cli.py              # CLI interface
│   ├── reporter.py         # Report generation
│   ├── database.py         # Data storage
│   └── utils.py            # Utility functions
├── config/
│   ├── scan_profiles.json  # Scan configurations
│   └── templates/          # Report templates
├── data/
│   ├── scans/              # Scan results
│   └── reports/            # Generated reports
├── tests/
│   ├── test_scanner.py
│   ├── test_cli.py
│   └── test_reporter.py
├── requirements.txt
├── setup.py
└── README.md
```

#### 1.2 Environment Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Verify Nmap installation
nmap --version
```

#### 1.3 Requirements File
```txt
# requirements.txt
python-nmap==0.7.1
colorama==0.4.6
rich==13.7.0
pandas==2.1.4
matplotlib==3.8.2
jinja2==3.1.2
click==8.1.7
tabulate==0.9.0
pyyaml==6.0.1
sqlite3
```

### Phase 2: Core Scanner Implementation

#### 2.1 Basic Scanner Class
```python
# src/scanner.py
import nmap
import json
import time
from datetime import datetime
from typing import Dict, List, Optional
import logging

class NetworkScanner:
    def __init__(self, config_file: str = None):
        """Initialize the network scanner."""
        self.nm = nmap.PortScanner()
        self.config = self._load_config(config_file)
        self.scan_results = {}
        self.logger = self._setup_logging()
    
    def _load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file."""
        default_config = {
            "scan_profiles": {
                "quick": {
                    "ports": "1-1000",
                    "timing": "3",
                    "scripts": []
                },
                "comprehensive": {
                    "ports": "1-65535",
                    "timing": "4",
                    "scripts": ["vuln", "auth", "default"]
                },
                "stealth": {
                    "ports": "22,80,443,3389",
                    "timing": "2",
                    "scripts": ["banner"]
                }
            },
            "output_formats": ["xml", "json", "txt"],
            "default_timeout": 300
        }
        
        if config_file:
            try:
                with open(config_file, 'r') as f:
                    return json.load(f)
            except FileNotFoundError:
                self.logger.warning(f"Config file {config_file} not found, using defaults")
        
        return default_config
    
    def _setup_logging(self) -> logging.Logger:
        """Setup logging configuration."""
        logger = logging.getLogger('NetworkScanner')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def scan_target(self, target: str, profile: str = "quick", 
                   custom_args: str = None) -> Dict:
        """Perform network scan on target."""
        self.logger.info(f"Starting scan of {target} with profile: {profile}")
        
        if profile not in self.config["scan_profiles"]:
            raise ValueError(f"Unknown scan profile: {profile}")
        
        scan_config = self.config["scan_profiles"][profile]
        
        # Build Nmap arguments
        args = f"-sS -sV -O -p {scan_config['ports']} -T{scan_config['timing']}"
        
        if scan_config['scripts']:
            args += f" --script={','.join(scan_config['scripts'])}"
        
        if custom_args:
            args += f" {custom_args}"
        
        self.logger.info(f"Nmap arguments: {args}")
        
        try:
            # Perform scan
            start_time = time.time()
            self.nm.scan(target, arguments=args)
            scan_time = time.time() - start_time
            
            # Process results
            results = {
                'target': target,
                'profile': profile,
                'scan_time': scan_time,
                'timestamp': datetime.now().isoformat(),
                'hosts': self._process_hosts(),
                'summary': self._generate_summary()
            }
            
            self.scan_results[target] = results
            self.logger.info(f"Scan completed in {scan_time:.2f} seconds")
            
            return results
            
        except Exception as e:
            self.logger.error(f"Scan failed: {str(e)}")
            raise
    
    def _process_hosts(self) -> List[Dict]:
        """Process scan results for all hosts."""
        hosts = []
        
        for host in self.nm.all_hosts():
            host_data = {
                'ip': host,
                'state': self.nm[host].state(),
                'hostnames': self.nm[host]['hostnames'],
                'os': self._extract_os_info(host),
                'ports': self._extract_ports(host),
                'scripts': self._extract_script_output(host)
            }
            hosts.append(host_data)
        
        return hosts
    
    def _extract_os_info(self, host: str) -> Dict:
        """Extract operating system information."""
        try:
            os_info = self.nm[host]['osmatch']
            if os_info:
                return {
                    'name': os_info[0]['name'],
                    'accuracy': os_info[0]['accuracy'],
                    'line': os_info[0]['line']
                }
        except KeyError:
            pass
        
        return {}
    
    def _extract_ports(self, host: str) -> List[Dict]:
        """Extract port information."""
        ports = []
        
        try:
            for proto in self.nm[host].all_protocols():
                for port in self.nm[host][proto]:
                    port_info = self.nm[host][proto][port]
                    ports.append({
                        'port': port,
                        'protocol': proto,
                        'state': port_info['state'],
                        'service': port_info['name'],
                        'version': port_info.get('version', ''),
                        'product': port_info.get('product', ''),
                        'extrainfo': port_info.get('extrainfo', '')
                    })
        except KeyError:
            pass
        
        return ports
    
    def _extract_script_output(self, host: str) -> Dict:
        """Extract NSE script output."""
        scripts = {}
        
        try:
            for proto in self.nm[host].all_protocols():
                for port in self.nm[host][proto]:
                    port_info = self.nm[host][proto][port]
                    if 'script' in port_info:
                        scripts[f"{proto}/{port}"] = port_info['script']
        except KeyError:
            pass
        
        return scripts
    
    def _generate_summary(self) -> Dict:
        """Generate scan summary statistics."""
        total_hosts = len(self.nm.all_hosts())
        up_hosts = len([h for h in self.nm.all_hosts() if self.nm[h].state() == 'up'])
        
        total_ports = 0
        open_ports = 0
        services = set()
        
        for host in self.nm.all_hosts():
            for proto in self.nm[host].all_protocols():
                for port in self.nm[host][proto]:
                    total_ports += 1
                    if self.nm[host][proto][port]['state'] == 'open':
                        open_ports += 1
                        services.add(self.nm[host][proto][port]['name'])
        
        return {
            'total_hosts': total_hosts,
            'up_hosts': up_hosts,
            'total_ports': total_ports,
            'open_ports': open_ports,
            'unique_services': len(services),
            'services': list(services)
        }
```

#### 2.2 Advanced Scanning Features
```python
# src/scanner.py (continued)
class NetworkScanner:
    # ... previous methods ...
    
    def scan_network(self, network: str, profile: str = "quick") -> Dict:
        """Scan entire network range."""
        self.logger.info(f"Starting network scan: {network}")
        
        results = {
            'network': network,
            'profile': profile,
            'timestamp': datetime.now().isoformat(),
            'hosts': [],
            'summary': {}
        }
        
        # Discover hosts first
        self.logger.info("Performing host discovery...")
        self.nm.scan(hosts=network, arguments='-sn')
        
        up_hosts = [h for h in self.nm.all_hosts() if self.nm[h].state() == 'up']
        self.logger.info(f"Found {len(up_hosts)} hosts")
        
        # Scan each host
        for i, host in enumerate(up_hosts, 1):
            self.logger.info(f"Scanning host {i}/{len(up_hosts)}: {host}")
            try:
                host_result = self.scan_target(host, profile)
                results['hosts'].append(host_result)
            except Exception as e:
                self.logger.error(f"Failed to scan {host}: {str(e)}")
        
        # Generate network summary
        results['summary'] = self._generate_network_summary(results['hosts'])
        
        return results
    
    def _generate_network_summary(self, hosts: List[Dict]) -> Dict:
        """Generate summary for network scan."""
        total_hosts = len(hosts)
        total_ports = sum(len(h['ports']) for h in hosts)
        open_ports = sum(len([p for p in h['ports'] if p['state'] == 'open']) 
                        for h in hosts)
        
        # Collect all services
        all_services = set()
        for host in hosts:
            for port in host['ports']:
                if port['state'] == 'open':
                    all_services.add(port['service'])
        
        # OS distribution
        os_distribution = {}
        for host in hosts:
            if host['os'] and 'name' in host['os']:
                os_name = host['os']['name']
                os_distribution[os_name] = os_distribution.get(os_name, 0) + 1
        
        return {
            'total_hosts': total_hosts,
            'total_ports': total_ports,
            'open_ports': open_ports,
            'unique_services': len(all_services),
            'services': list(all_services),
            'os_distribution': os_distribution
        }
    
    def vulnerability_scan(self, target: str) -> Dict:
        """Perform vulnerability scan using NSE scripts."""
        self.logger.info(f"Starting vulnerability scan: {target}")
        
        vuln_scripts = [
            'vuln',           # Default vulnerability scripts
            'auth',           # Authentication bypass
            'brute',          # Brute force attacks
            'default',        # Default scripts
            'discovery',      # Service discovery
            'dos',            # Denial of service
            'exploit',        # Exploit scripts
            'external',       # External scripts
            'fuzzer',         # Fuzzing scripts
            'intrusive',      # Intrusive scripts
            'malware',        # Malware detection
            'safe',           # Safe scripts
            'version'         # Version detection
        ]
        
        args = f"-sS -sV -O --script={','.join(vuln_scripts)} -T4"
        
        try:
            self.nm.scan(target, arguments=args)
            
            results = {
                'target': target,
                'scan_type': 'vulnerability',
                'timestamp': datetime.now().isoformat(),
                'vulnerabilities': self._extract_vulnerabilities(target),
                'recommendations': self._generate_recommendations()
            }
            
            return results
            
        except Exception as e:
            self.logger.error(f"Vulnerability scan failed: {str(e)}")
            raise
    
    def _extract_vulnerabilities(self, target: str) -> List[Dict]:
        """Extract vulnerability information from scan results."""
        vulnerabilities = []
        
        try:
            for proto in self.nm[target].all_protocols():
                for port in self.nm[target][proto]:
                    port_info = self.nm[target][proto][port]
                    
                    if 'script' in port_info:
                        for script_name, output in port_info['script'].items():
                            if any(keyword in script_name.lower() 
                                   for keyword in ['vuln', 'auth', 'exploit']):
                                vulnerabilities.append({
                                    'port': port,
                                    'protocol': proto,
                                    'script': script_name,
                                    'output': output,
                                    'severity': self._assess_severity(script_name, output)
                                })
        except KeyError:
            pass
        
        return vulnerabilities
    
    def _assess_severity(self, script_name: str, output: str) -> str:
        """Assess vulnerability severity based on script and output."""
        high_keywords = ['critical', 'high', 'exploit', 'remote', 'root']
        medium_keywords = ['medium', 'warning', 'weak', 'default']
        low_keywords = ['info', 'low', 'note']
        
        output_lower = output.lower()
        
        if any(keyword in output_lower for keyword in high_keywords):
            return 'HIGH'
        elif any(keyword in output_lower for keyword in medium_keywords):
            return 'MEDIUM'
        elif any(keyword in output_lower for keyword in low_keywords):
            return 'LOW'
        else:
            return 'INFO'
    
    def _generate_recommendations(self) -> List[str]:
        """Generate security recommendations based on findings."""
        recommendations = [
            "Keep all systems and services updated",
            "Use strong authentication mechanisms",
            "Implement proper access controls",
            "Monitor network traffic for anomalies",
            "Regular security assessments recommended"
        ]
        
        return recommendations
```

### Phase 3: CLI Interface Development

#### 3.1 Command Line Interface
```python
# src/cli.py
import click
import json
import os
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.text import Text

from .scanner import NetworkScanner
from .reporter import ReportGenerator
from .database import ScanDatabase

console = Console()

@click.group()
@click.version_option(version='1.0.0')
def cli():
    """Network Security Scanner - Advanced Nmap Automation Tool"""
    pass

@cli.command()
@click.argument('target')
@click.option('--profile', '-p', default='quick', 
              type=click.Choice(['quick', 'comprehensive', 'stealth']),
              help='Scan profile to use')
@click.option('--output', '-o', default='scan_results.json',
              help='Output file for results')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
@click.option('--config', '-c', help='Configuration file path')
def scan(target, profile, output, verbose, config):
    """Scan a single target or network range."""
    
    if verbose:
        console.print(f"[bold blue]Starting scan of {target}[/bold blue]")
        console.print(f"[dim]Profile: {profile}[/dim]")
    
    try:
        # Initialize scanner
        scanner = NetworkScanner(config)
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Scanning...", total=None)
            
            # Perform scan
            if '/' in target or target.endswith('.0/24'):
                # Network scan
                results = scanner.scan_network(target, profile)
            else:
                # Single target scan
                results = scanner.scan_target(target, profile)
            
            progress.update(task, description="Scan completed!")
        
        # Save results
        with open(output, 'w') as f:
            json.dump(results, f, indent=2)
        
        # Display summary
        display_scan_summary(results)
        
        console.print(f"[green]Results saved to {output}[/green]")
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise click.Abort()

@cli.command()
@click.argument('target')
@click.option('--output', '-o', default='vuln_scan.json',
              help='Output file for results')
def vulnscan(target, output):
    """Perform vulnerability scan on target."""
    
    console.print(f"[bold red]Starting vulnerability scan of {target}[/bold red]")
    
    try:
        scanner = NetworkScanner()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Vulnerability scanning...", total=None)
            
            results = scanner.vulnerability_scan(target)
            
            progress.update(task, description="Vulnerability scan completed!")
        
        # Save results
        with open(output, 'w') as f:
            json.dump(results, f, indent=2)
        
        # Display vulnerabilities
        display_vulnerabilities(results)
        
        console.print(f"[green]Vulnerability results saved to {output}[/green]")
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise click.Abort()

@cli.command()
@click.argument('scan_file')
@click.option('--format', '-f', default='html',
              type=click.Choice(['html', 'pdf', 'json', 'csv']),
              help='Report format')
@click.option('--output', '-o', help='Output file name')
def report(scan_file, format, output):
    """Generate report from scan results."""
    
    if not os.path.exists(scan_file):
        console.print(f"[red]Scan file not found: {scan_file}[/red]")
        raise click.Abort()
    
    try:
        # Load scan results
        with open(scan_file, 'r') as f:
            scan_data = json.load(f)
        
        # Generate report
        reporter = ReportGenerator()
        
        if not output:
            output = f"report_{Path(scan_file).stem}.{format}"
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Generating report...", total=None)
            
            reporter.generate_report(scan_data, format, output)
            
            progress.update(task, description="Report generated!")
        
        console.print(f"[green]Report saved to {output}[/green]")
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise click.Abort()

@cli.command()
@click.option('--host', default='localhost', help='Database host')
@click.option('--port', default=5432, help='Database port')
@click.option('--database', default='scans', help='Database name')
def initdb(host, port, database):
    """Initialize database for storing scan results."""
    
    console.print("[bold blue]Initializing database...[/bold blue]")
    
    try:
        db = ScanDatabase(host, port, database)
        db.initialize()
        
        console.print("[green]Database initialized successfully![/green]")
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise click.Abort()

def display_scan_summary(results):
    """Display scan results summary."""
    
    # Create summary table
    table = Table(title="Scan Summary")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    
    if 'summary' in results:
        summary = results['summary']
        table.add_row("Total Hosts", str(summary.get('total_hosts', 0)))
        table.add_row("Up Hosts", str(summary.get('up_hosts', 0)))
        table.add_row("Total Ports", str(summary.get('total_ports', 0)))
        table.add_row("Open Ports", str(summary.get('open_ports', 0)))
        table.add_row("Services", str(summary.get('unique_services', 0)))
    
    console.print(table)
    
    # Display hosts table
    if 'hosts' in results and results['hosts']:
        hosts_table = Table(title="Hosts Found")
        hosts_table.add_column("IP Address", style="cyan")
        hosts_table.add_column("State", style="green")
        hosts_table.add_column("Open Ports", style="yellow")
        hosts_table.add_column("OS", style="blue")
        
        for host in results['hosts']:
            open_ports = len([p for p in host.get('ports', []) if p['state'] == 'open'])
            os_name = host.get('os', {}).get('name', 'Unknown')
            
            hosts_table.add_row(
                host.get('ip', 'Unknown'),
                host.get('state', 'Unknown'),
                str(open_ports),
                os_name
            )
        
        console.print(hosts_table)

def display_vulnerabilities(results):
    """Display vulnerability scan results."""
    
    if not results.get('vulnerabilities'):
        console.print("[yellow]No vulnerabilities found![/yellow]")
        return
    
    # Group by severity
    vuln_table = Table(title="Vulnerabilities Found")
    vuln_table.add_column("Severity", style="red")
    vuln_table.add_column("Port", style="cyan")
    vuln_table.add_column("Script", style="yellow")
    vuln_table.add_column("Details", style="white")
    
    for vuln in results['vulnerabilities']:
        severity_color = {
            'HIGH': 'red',
            'MEDIUM': 'yellow',
            'LOW': 'green',
            'INFO': 'blue'
        }.get(vuln['severity'], 'white')
        
        vuln_table.add_row(
            f"[{severity_color}]{vuln['severity']}[/{severity_color}]",
            f"{vuln['protocol']}/{vuln['port']}",
            vuln['script'],
            vuln['output'][:100] + "..." if len(vuln['output']) > 100 else vuln['output']
        )
    
    console.print(vuln_table)
    
    # Display recommendations
    if results.get('recommendations'):
        console.print("\n[bold]Recommendations:[/bold]")
        for rec in results['recommendations']:
            console.print(f"• {rec}")

if __name__ == '__main__':
    cli()
```

### Phase 4: Report Generation

#### 4.1 Report Generator
```python
# src/reporter.py
import json
import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List
import jinja2
import matplotlib.pyplot as plt
import pandas as pd

class ReportGenerator:
    def __init__(self, template_dir: str = "config/templates"):
        """Initialize report generator."""
        self.template_dir = Path(template_dir)
        self.jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(str(self.template_dir))
        )
    
    def generate_report(self, scan_data: Dict, format: str, output_file: str):
        """Generate report in specified format."""
        if format == 'html':
            self._generate_html_report(scan_data, output_file)
        elif format == 'pdf':
            self._generate_pdf_report(scan_data, output_file)
        elif format == 'json':
            self._generate_json_report(scan_data, output_file)
        elif format == 'csv':
            self._generate_csv_report(scan_data, output_file)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _generate_html_report(self, scan_data: Dict, output_file: str):
        """Generate HTML report."""
        template = self.jinja_env.get_template('report_template.html')
        
        # Prepare data for template
        report_data = {
            'scan_data': scan_data,
            'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'summary': self._generate_summary_stats(scan_data),
            'charts': self._generate_charts(scan_data)
        }
        
        html_content = template.render(**report_data)
        
        with open(output_file, 'w') as f:
            f.write(html_content)
    
    def _generate_pdf_report(self, scan_data: Dict, output_file: str):
        """Generate PDF report."""
        # This would require additional libraries like weasyprint or reportlab
        # For now, we'll generate HTML and suggest conversion
        html_file = output_file.replace('.pdf', '.html')
        self._generate_html_report(scan_data, html_file)
        
        print(f"HTML report generated: {html_file}")
        print("Convert to PDF using: wkhtmltopdf {html_file} {output_file}")
    
    def _generate_json_report(self, scan_data: Dict, output_file: str):
        """Generate JSON report."""
        report_data = {
            'report_metadata': {
                'generated_at': datetime.now().isoformat(),
                'scan_data': scan_data,
                'summary': self._generate_summary_stats(scan_data)
            }
        }
        
        with open(output_file, 'w') as f:
            json.dump(report_data, f, indent=2)
    
    def _generate_csv_report(self, scan_data: Dict, output_file: str):
        """Generate CSV report."""
        # Flatten scan data for CSV
        rows = []
        
        for host in scan_data.get('hosts', []):
            for port in host.get('ports', []):
                row = {
                    'ip': host.get('ip', ''),
                    'state': host.get('state', ''),
                    'port': port.get('port', ''),
                    'protocol': port.get('protocol', ''),
                    'service': port.get('service', ''),
                    'version': port.get('version', ''),
                    'product': port.get('product', '')
                }
                rows.append(row)
        
        if rows:
            df = pd.DataFrame(rows)
            df.to_csv(output_file, index=False)
    
    def _generate_summary_stats(self, scan_data: Dict) -> Dict:
        """Generate summary statistics."""
        summary = scan_data.get('summary', {})
        
        stats = {
            'total_hosts': summary.get('total_hosts', 0),
            'up_hosts': summary.get('up_hosts', 0),
            'total_ports': summary.get('total_ports', 0),
            'open_ports': summary.get('open_ports', 0),
            'unique_services': summary.get('unique_services', 0),
            'scan_duration': scan_data.get('scan_time', 0),
            'scan_profile': scan_data.get('profile', 'unknown')
        }
        
        return stats
    
    def _generate_charts(self, scan_data: Dict) -> Dict:
        """Generate charts for the report."""
        charts = {}
        
        # Service distribution chart
        if 'summary' in scan_data and 'services' in scan_data['summary']:
            services = scan_data['summary']['services']
            if services:
                plt.figure(figsize=(10, 6))
                service_counts = pd.Series(services).value_counts()
                service_counts.plot(kind='bar')
                plt.title('Service Distribution')
                plt.xlabel('Service')
                plt.ylabel('Count')
                plt.xticks(rotation=45)
                plt.tight_layout()
                
                chart_file = 'service_distribution.png'
                plt.savefig(chart_file)
                plt.close()
                
                charts['service_distribution'] = chart_file
        
        # OS distribution chart
        if 'summary' in scan_data and 'os_distribution' in scan_data['summary']:
            os_dist = scan_data['summary']['os_distribution']
            if os_dist:
                plt.figure(figsize=(10, 6))
                os_counts = pd.Series(os_dist)
                os_counts.plot(kind='pie', autopct='%1.1f%%')
                plt.title('Operating System Distribution')
                plt.ylabel('')
                plt.tight_layout()
                
                chart_file = 'os_distribution.png'
                plt.savefig(chart_file)
                plt.close()
                
                charts['os_distribution'] = chart_file
        
        return charts
```

### Phase 5: Database Integration

#### 5.1 Database Handler
```python
# src/database.py
import sqlite3
import json
from datetime import datetime
from typing import Dict, List, Optional
import logging

class ScanDatabase:
    def __init__(self, db_path: str = "data/scans.db"):
        """Initialize database connection."""
        self.db_path = db_path
        self.logger = logging.getLogger('ScanDatabase')
        self._ensure_db_directory()
    
    def _ensure_db_directory(self):
        """Ensure database directory exists."""
        db_dir = Path(self.db_path).parent
        db_dir.mkdir(parents=True, exist_ok=True)
    
    def initialize(self):
        """Initialize database tables."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create scans table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS scans (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    target TEXT NOT NULL,
                    profile TEXT NOT NULL,
                    scan_time REAL,
                    timestamp TEXT NOT NULL,
                    summary TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create hosts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS hosts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    scan_id INTEGER,
                    ip TEXT NOT NULL,
                    state TEXT,
                    os_name TEXT,
                    os_accuracy INTEGER,
                    FOREIGN KEY (scan_id) REFERENCES scans (id)
                )
            ''')
            
            # Create ports table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ports (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    host_id INTEGER,
                    port INTEGER NOT NULL,
                    protocol TEXT NOT NULL,
                    state TEXT,
                    service TEXT,
                    version TEXT,
                    product TEXT,
                    FOREIGN KEY (host_id) REFERENCES hosts (id)
                )
            ''')
            
            # Create vulnerabilities table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS vulnerabilities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    scan_id INTEGER,
                    port_id INTEGER,
                    script_name TEXT,
                    output TEXT,
                    severity TEXT,
                    FOREIGN KEY (scan_id) REFERENCES scans (id),
                    FOREIGN KEY (port_id) REFERENCES ports (id)
                )
            ''')
            
            conn.commit()
    
    def save_scan(self, scan_data: Dict) -> int:
        """Save scan results to database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Insert scan record
            cursor.execute('''
                INSERT INTO scans (target, profile, scan_time, timestamp, summary)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                scan_data['target'],
                scan_data['profile'],
                scan_data.get('scan_time', 0),
                scan_data['timestamp'],
                json.dumps(scan_data.get('summary', {}))
            ))
            
            scan_id = cursor.lastrowid
            
            # Insert hosts
            for host in scan_data.get('hosts', []):
                cursor.execute('''
                    INSERT INTO hosts (scan_id, ip, state, os_name, os_accuracy)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    scan_id,
                    host['ip'],
                    host['state'],
                    host.get('os', {}).get('name', ''),
                    host.get('os', {}).get('accuracy', 0)
                ))
                
                host_id = cursor.lastrowid
                
                # Insert ports
                for port in host.get('ports', []):
                    cursor.execute('''
                        INSERT INTO ports (host_id, port, protocol, state, service, version, product)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        host_id,
                        port['port'],
                        port['protocol'],
                        port['state'],
                        port['service'],
                        port.get('version', ''),
                        port.get('product', '')
                    ))
            
            conn.commit()
            return scan_id
    
    def get_scan(self, scan_id: int) -> Optional[Dict]:
        """Retrieve scan by ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Get scan details
            cursor.execute('SELECT * FROM scans WHERE id = ?', (scan_id,))
            scan_row = cursor.fetchone()
            
            if not scan_row:
                return None
            
            scan_data = {
                'id': scan_row[0],
                'target': scan_row[1],
                'profile': scan_row[2],
                'scan_time': scan_row[3],
                'timestamp': scan_row[4],
                'summary': json.loads(scan_row[5]),
                'hosts': []
            }
            
            # Get hosts
            cursor.execute('SELECT * FROM hosts WHERE scan_id = ?', (scan_id,))
            for host_row in cursor.fetchall():
                host_data = {
                    'id': host_row[0],
                    'ip': host_row[2],
                    'state': host_row[3],
                    'os': {
                        'name': host_row[4],
                        'accuracy': host_row[5]
                    },
                    'ports': []
                }
                
                # Get ports for this host
                cursor.execute('SELECT * FROM ports WHERE host_id = ?', (host_row[0],))
                for port_row in cursor.fetchall():
                    port_data = {
                        'port': port_row[2],
                        'protocol': port_row[3],
                        'state': port_row[4],
                        'service': port_row[5],
                        'version': port_row[6],
                        'product': port_row[7]
                    }
                    host_data['ports'].append(port_data)
                
                scan_data['hosts'].append(host_data)
            
            return scan_data
    
    def get_recent_scans(self, limit: int = 10) -> List[Dict]:
        """Get recent scans."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT id, target, profile, scan_time, timestamp, summary
                FROM scans
                ORDER BY created_at DESC
                LIMIT ?
            ''', (limit,))
            
            scans = []
            for row in cursor.fetchall():
                scans.append({
                    'id': row[0],
                    'target': row[1],
                    'profile': row[2],
                    'scan_time': row[3],
                    'timestamp': row[4],
                    'summary': json.loads(row[5])
                })
            
            return scans
    
    def search_scans(self, target: str = None, profile: str = None) -> List[Dict]:
        """Search scans by criteria."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            query = 'SELECT id, target, profile, scan_time, timestamp FROM scans WHERE 1=1'
            params = []
            
            if target:
                query += ' AND target LIKE ?'
                params.append(f'%{target}%')
            
            if profile:
                query += ' AND profile = ?'
                params.append(profile)
            
            query += ' ORDER BY created_at DESC'
            
            cursor.execute(query, params)
            
            scans = []
            for row in cursor.fetchall():
                scans.append({
                    'id': row[0],
                    'target': row[1],
                    'profile': row[2],
                    'scan_time': row[3],
                    'timestamp': row[4]
                })
            
            return scans
```

## 🧪 Testing and Validation

### Unit Tests
```python
# tests/test_scanner.py
import unittest
from unittest.mock import Mock, patch
from src.scanner import NetworkScanner

class TestNetworkScanner(unittest.TestCase):
    def setUp(self):
        self.scanner = NetworkScanner()
    
    def test_load_config(self):
        """Test configuration loading."""
        config = self.scanner._load_config(None)
        self.assertIn('scan_profiles', config)
        self.assertIn('quick', config['scan_profiles'])
    
    def test_scan_target(self):
        """Test target scanning."""
        with patch('nmap.PortScanner') as mock_nmap:
            mock_scanner = Mock()
            mock_scanner.all_hosts.return_value = ['192.168.1.1']
            mock_scanner['192.168.1.1'].state.return_value = 'up'
            mock_scanner['192.168.1.1'].all_protocols.return_value = ['tcp']
            mock_scanner['192.168.1.1']['tcp'] = {
                80: {'state': 'open', 'name': 'http'}
            }
            
            mock_nmap.return_value = mock_scanner
            
            results = self.scanner.scan_target('192.168.1.1')
            
            self.assertIn('target', results)
            self.assertEqual(results['target'], '192.168.1.1')

if __name__ == '__main__':
    unittest.main()
```

### Integration Tests
```python
# tests/test_integration.py
import unittest
import tempfile
import os
from src.scanner import NetworkScanner
from src.reporter import ReportGenerator

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.scanner = NetworkScanner()
        self.reporter = ReportGenerator()
    
    def test_scan_and_report(self):
        """Test complete scan and report workflow."""
        # Mock scan data
        scan_data = {
            'target': '192.168.1.1',
            'profile': 'quick',
            'scan_time': 10.5,
            'timestamp': '2024-01-01T10:00:00',
            'hosts': [
                {
                    'ip': '192.168.1.1',
                    'state': 'up',
                    'ports': [
                        {
                            'port': 80,
                            'protocol': 'tcp',
                            'state': 'open',
                            'service': 'http'
                        }
                    ]
                }
            ],
            'summary': {
                'total_hosts': 1,
                'up_hosts': 1,
                'open_ports': 1
            }
        }
        
        # Generate report
        output_file = os.path.join(self.temp_dir, 'test_report.json')
        self.reporter.generate_report(scan_data, 'json', output_file)
        
        # Verify report was created
        self.assertTrue(os.path.exists(output_file))
    
    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

if __name__ == '__main__':
    unittest.main()
```

## 📊 Usage Examples

### Basic Usage
```bash
# Install the tool
pip install -e .

# Scan a single host
python -m src.cli scan 192.168.1.100

# Scan with comprehensive profile
python -m src.cli scan 192.168.1.0/24 --profile comprehensive

# Vulnerability scan
python -m src.cli vulnscan 192.168.1.100

# Generate HTML report
python -m src.cli report scan_results.json --format html
```

### Advanced Usage
```bash
# Custom scan with specific ports
python -m src.cli scan 192.168.1.100 --profile quick --output custom_scan.json

# Network scan with stealth profile
python -m src.cli scan 10.0.0.0/16 --profile stealth

# Generate multiple report formats
python -m src.cli report scan_results.json --format html --output report.html
python -m src.cli report scan_results.json --format csv --output data.csv
python -m src.cli report scan_results.json --format json --output analysis.json
```

## 🔍 Troubleshooting

### Common Issues
```bash
# Permission denied for Nmap
sudo chmod +s /usr/bin/nmap

# Python dependencies not found
pip install -r requirements.txt

# Database connection issues
# Check file permissions and directory existence

# Report generation fails
# Ensure template files exist in config/templates/
```

### Performance Optimization
```bash
# Use faster scan profiles for large networks
python -m src.cli scan 192.168.0.0/16 --profile quick

# Limit concurrent scans
# Modify scanner configuration for parallel processing

# Use database for large scan datasets
python -m src.cli initdb
```

## 📈 Career Impact

### Skills Demonstrated
- **Python Development**
- **Network Security Tooling**
- **CLI Application Design**
- **Database Integration**
- **Report Generation**
- **Automation Development**

### Job Roles This Prepares You For
- **Security Engineer**
- **DevSecOps Engineer**
- **Security Automation Specialist**
- **Network Security Analyst**
- **Security Tool Developer**

### Certifications This Helps With
- **CompTIA Security+**
- **Python Programming Certifications**
- **Security Automation Certifications**
- **Network Security Certifications**

## 🔗 Additional Resources

- [Nmap Documentation](https://nmap.org/docs.html)
- [Python Nmap Library](https://pypi.org/project/python-nmap/)
- [Click Framework](https://click.palletsprojects.com/)
- [Rich Terminal Library](https://rich.readthedocs.io/)

---

**Next Project**: [Project 5: Honeypot Deployment](../05-honeypot-deployment/README.md)

**Previous Project**: [Project 3: Secure Network Architecture Design](../03-network-architecture/README.md) 
#!/usr/bin/env python3
import psutil
import os
import time
import threading
from datetime import datetime
import json
import logging
from collections import defaultdict
import signal
import sys
import argparse

class ProcessAnalyzer:
    def __init__(self):
        self.process_data = defaultdict(dict)
        self.running = True
        self.setup_logging()
        self.setup_signal_handlers()

    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('process_analysis.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger('ProcessAnalyzer')

    def setup_signal_handlers(self):
        """Setup signal handlers for graceful shutdown"""
        signal.signal(signal.SIGINT, self.handle_shutdown)
        signal.signal(signal.SIGTERM, self.handle_shutdown)

    def handle_shutdown(self, signum, frame):
        """Handle shutdown signals"""
        self.logger.info("Shutdown signal received. Saving data and exiting...")
        self.running = False
        self.save_analysis()
        sys.exit(0)

    def get_process_details(self, pid):
        """Get detailed information about a process"""
        try:
            process = psutil.Process(pid)
            return {
                'pid': pid,
                'name': process.name(),
                'username': process.username(),
                'create_time': datetime.fromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S'),
                'cpu_percent': process.cpu_percent(),
                'memory_percent': process.memory_percent(),
                'memory_info': dict(process.memory_info()._asdict()),
                'num_threads': process.num_threads(),
                'status': process.status(),
                'io_counters': dict(process.io_counters()._asdict()) if process.io_counters() else None,
                'connections': [dict(conn._asdict()) for conn in process.connections()],
                'open_files': [dict(file._asdict()) for file in process.open_files()],
                'cmdline': process.cmdline(),
                'environ': process.environ()
            }
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            self.logger.error(f"Error getting process details for PID {pid}: {e}")
            return None

    def analyze_process_tree(self, pid):
        """Analyze process tree starting from given PID"""
        try:
            process = psutil.Process(pid)
            children = process.children(recursive=True)
            
            tree_info = {
                'root': self.get_process_details(pid),
                'children': [self.get_process_details(child.pid) for child in children]
            }
            
            return tree_info
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            self.logger.error(f"Error analyzing process tree for PID {pid}: {e}")
            return None

    def monitor_process(self, pid, interval=1):
        """Monitor a specific process"""
        while self.running:
            try:
                process = psutil.Process(pid)
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # Get process metrics
                metrics = {
                    'timestamp': current_time,
                    'cpu_percent': process.cpu_percent(),
                    'memory_percent': process.memory_percent(),
                    'memory_info': dict(process.memory_info()._asdict()),
                    'io_counters': dict(process.io_counters()._asdict()) if process.io_counters() else None,
                    'num_threads': process.num_threads(),
                    'status': process.status()
                }
                
                # Store metrics
                self.process_data[pid][current_time] = metrics
                
                # Log significant changes
                self.check_anomalies(pid, metrics)
                
                time.sleep(interval)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                self.logger.error(f"Error monitoring process {pid}: {e}")
                break

    def check_anomalies(self, pid, metrics):
        """Check for anomalies in process metrics"""
        try:
            # CPU usage threshold
            if metrics['cpu_percent'] > 80:
                self.logger.warning(f"High CPU usage detected for PID {pid}: {metrics['cpu_percent']}%")
            
            # Memory usage threshold
            if metrics['memory_percent'] > 80:
                self.logger.warning(f"High memory usage detected for PID {pid}: {metrics['memory_percent']}%")
            
            # Thread count threshold
            if metrics['num_threads'] > 100:
                self.logger.warning(f"High thread count detected for PID {pid}: {metrics['num_threads']}")
            
            # Process status check
            if metrics['status'] == psutil.STATUS_ZOMBIE:
                self.logger.warning(f"Zombie process detected for PID {pid}")
        except Exception as e:
            self.logger.error(f"Error checking anomalies for PID {pid}: {e}")

    def save_analysis(self):
        """Save process analysis data"""
        try:
            with open('process_analysis.json', 'w') as f:
                json.dump(self.process_data, f, indent=4)
            self.logger.info("Analysis data saved to process_analysis.json")
        except Exception as e:
            self.logger.error(f"Error saving analysis data: {e}")

    def generate_report(self):
        """Generate analysis report"""
        try:
            report = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'total_processes_analyzed': len(self.process_data),
                'process_summary': {}
            }
            
            for pid, data in self.process_data.items():
                if data:
                    latest_metrics = data[max(data.keys())]
                    report['process_summary'][pid] = {
                        'name': psutil.Process(pid).name(),
                        'latest_cpu_percent': latest_metrics['cpu_percent'],
                        'latest_memory_percent': latest_metrics['memory_percent'],
                        'status': latest_metrics['status']
                    }
            
            with open('process_report.json', 'w') as f:
                json.dump(report, f, indent=4)
            self.logger.info("Analysis report generated: process_report.json")
        except Exception as e:
            self.logger.error(f"Error generating report: {e}")

def main():
    parser = argparse.ArgumentParser(description='Process Analyzer')
    parser.add_argument('-p', '--pid', type=int, help='PID to monitor')
    parser.add_argument('-i', '--interval', type=float, default=1.0, help='Monitoring interval in seconds')
    args = parser.parse_args()

    analyzer = ProcessAnalyzer()
    
    if args.pid:
        try:
            # Verify process exists
            psutil.Process(args.pid)
            
            # Start monitoring
            monitor_thread = threading.Thread(
                target=analyzer.monitor_process,
                args=(args.pid, args.interval)
            )
            monitor_thread.start()
            
            # Wait for monitoring thread
            monitor_thread.join()
        except psutil.NoSuchProcess:
            print(f"Process with PID {args.pid} does not exist")
            sys.exit(1)
    else:
        print("Please specify a PID to monitor")
        sys.exit(1)

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
import os
import sys
import time
import logging
import json
import threading
from datetime import datetime
import subprocess
import re
import signal
from collections import defaultdict
import psutil
import mmap
import struct
import ctypes
from ctypes import *
import argparse

class KernelAnalyzer:
    def __init__(self):
        self.running = True
        self.kernel_data = defaultdict(dict)
        self.setup_logging()
        self.setup_signal_handlers()
        self.load_kernel_modules()

    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('kernel_analysis.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger('KernelAnalyzer')

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

    def load_kernel_modules(self):
        """Load required kernel modules"""
        try:
            # Check if running as root
            if os.geteuid() != 0:
                self.logger.error("This script must be run as root")
                sys.exit(1)

            # Load required kernel modules
            modules = ['kprobes', 'ftrace']
            for module in modules:
                try:
                    subprocess.run(['modprobe', module], check=True)
                    self.logger.info(f"Loaded kernel module: {module}")
                except subprocess.CalledProcessError:
                    self.logger.error(f"Failed to load kernel module: {module}")
                    sys.exit(1)
        except Exception as e:
            self.logger.error(f"Error loading kernel modules: {e}")
            sys.exit(1)

    def get_kernel_version(self):
        """Get kernel version information"""
        try:
            with open('/proc/version', 'r') as f:
                return f.read().strip()
        except Exception as e:
            self.logger.error(f"Error getting kernel version: {e}")
            return None

    def get_kernel_parameters(self):
        """Get kernel parameters from /proc/sys"""
        try:
            parameters = {}
            for root, dirs, files in os.walk('/proc/sys'):
                for file in files:
                    try:
                        path = os.path.join(root, file)
                        with open(path, 'r') as f:
                            value = f.read().strip()
                            parameters[path] = value
                    except:
                        continue
            return parameters
        except Exception as e:
            self.logger.error(f"Error getting kernel parameters: {e}")
            return None

    def analyze_memory_management(self):
        """Analyze kernel memory management"""
        try:
            memory_info = {}
            
            # Get memory info from /proc/meminfo
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    key, value = line.split(':')
                    memory_info[key.strip()] = value.strip()
            
            # Get slab info
            with open('/proc/slabinfo', 'r') as f:
                memory_info['slab'] = f.read()
            
            # Get buddy info
            with open('/proc/buddyinfo', 'r') as f:
                memory_info['buddy'] = f.read()
            
            return memory_info
        except Exception as e:
            self.logger.error(f"Error analyzing memory management: {e}")
            return None

    def analyze_process_scheduling(self):
        """Analyze kernel process scheduling"""
        try:
            scheduling_info = {}
            
            # Get scheduler statistics
            with open('/proc/schedstat', 'r') as f:
                scheduling_info['schedstat'] = f.read()
            
            # Get CPU scheduling domains
            with open('/proc/sys/kernel/sched_domain/cpu0/domain0/flags', 'r') as f:
                scheduling_info['sched_domain_flags'] = f.read()
            
            # Get scheduler tunables
            for tunable in ['sched_min_granularity_ns', 'sched_latency_ns', 'sched_wakeup_granularity_ns']:
                with open(f'/proc/sys/kernel/{tunable}', 'r') as f:
                    scheduling_info[tunable] = f.read().strip()
            
            return scheduling_info
        except Exception as e:
            self.logger.error(f"Error analyzing process scheduling: {e}")
            return None

    def analyze_io_subsystem(self):
        """Analyze kernel I/O subsystem"""
        try:
            io_info = {}
            
            # Get I/O scheduler information
            with open('/sys/block/sda/queue/scheduler', 'r') as f:
                io_info['scheduler'] = f.read().strip()
            
            # Get I/O statistics
            with open('/proc/diskstats', 'r') as f:
                io_info['diskstats'] = f.read()
            
            # Get I/O scheduler tunables
            for tunable in ['read_ahead_kb', 'nr_requests', 'rotational']:
                with open(f'/sys/block/sda/queue/{tunable}', 'r') as f:
                    io_info[tunable] = f.read().strip()
            
            return io_info
        except Exception as e:
            self.logger.error(f"Error analyzing I/O subsystem: {e}")
            return None

    def analyze_network_stack(self):
        """Analyze kernel network stack"""
        try:
            network_info = {}
            
            # Get network statistics
            with open('/proc/net/snmp', 'r') as f:
                network_info['snmp'] = f.read()
            
            # Get network interface statistics
            with open('/proc/net/dev', 'r') as f:
                network_info['dev'] = f.read()
            
            # Get network protocol statistics
            for protocol in ['tcp', 'udp', 'icmp']:
                with open(f'/proc/net/{protocol}', 'r') as f:
                    network_info[protocol] = f.read()
            
            return network_info
        except Exception as e:
            self.logger.error(f"Error analyzing network stack: {e}")
            return None

    def monitor_kernel_events(self):
        """Monitor kernel events using ftrace"""
        try:
            # Setup ftrace
            with open('/sys/kernel/debug/tracing/tracing_on', 'w') as f:
                f.write('1')
            
            with open('/sys/kernel/debug/tracing/current_tracer', 'w') as f:
                f.write('function')
            
            # Start monitoring
            while self.running:
                with open('/sys/kernel/debug/tracing/trace', 'r') as f:
                    events = f.read()
                    self.analyze_kernel_events(events)
                time.sleep(1)
        except Exception as e:
            self.logger.error(f"Error monitoring kernel events: {e}")
        finally:
            # Cleanup ftrace
            with open('/sys/kernel/debug/tracing/tracing_on', 'w') as f:
                f.write('0')

    def analyze_kernel_events(self, events):
        """Analyze kernel events from ftrace output"""
        try:
            # Parse events and look for patterns
            for line in events.split('\n'):
                if 'syscall' in line:
                    self.logger.info(f"System call detected: {line}")
                elif 'irq' in line:
                    self.logger.info(f"Interrupt detected: {line}")
                elif 'sched' in line:
                    self.logger.info(f"Scheduling event detected: {line}")
        except Exception as e:
            self.logger.error(f"Error analyzing kernel events: {e}")

    def save_analysis(self):
        """Save kernel analysis data"""
        try:
            analysis = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'kernel_version': self.get_kernel_version(),
                'kernel_parameters': self.get_kernel_parameters(),
                'memory_management': self.analyze_memory_management(),
                'process_scheduling': self.analyze_process_scheduling(),
                'io_subsystem': self.analyze_io_subsystem(),
                'network_stack': self.analyze_network_stack()
            }
            
            with open('kernel_analysis.json', 'w') as f:
                json.dump(analysis, f, indent=4)
            self.logger.info("Analysis data saved to kernel_analysis.json")
        except Exception as e:
            self.logger.error(f"Error saving analysis data: {e}")

def main():
    parser = argparse.ArgumentParser(description='Kernel Analyzer')
    parser.add_argument('-m', '--monitor', action='store_true', help='Monitor kernel events')
    args = parser.parse_args()

    analyzer = KernelAnalyzer()
    
    if args.monitor:
        try:
            # Start kernel event monitoring
            monitor_thread = threading.Thread(target=analyzer.monitor_kernel_events)
            monitor_thread.start()
            
            # Wait for monitoring thread
            monitor_thread.join()
        except KeyboardInterrupt:
            analyzer.running = False
            monitor_thread.join()
    else:
        # Perform one-time analysis
        analyzer.save_analysis()

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
import psutil
import time
from datetime import datetime
import os

def get_size(bytes):
    """Convert bytes to human readable format"""
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def get_processes():
    """Get list of running processes"""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'memory_percent', 'cpu_percent']):
        try:
            pinfo = proc.info
            processes.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes

def print_system_info():
    """Print basic system information"""
    print("\n=== System Information ===")
    print(f"Boot Time: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"CPU Cores: {psutil.cpu_count()}")
    print(f"Total Memory: {get_size(psutil.virtual_memory().total)}")
    print(f"Available Memory: {get_size(psutil.virtual_memory().available)}")

def print_cpu_usage():
    """Print CPU usage information"""
    print("\n=== CPU Usage ===")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print("Per CPU Usage:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"CPU {i}: {percentage}%")

def print_memory_usage():
    """Print memory usage information"""
    print("\n=== Memory Usage ===")
    memory = psutil.virtual_memory()
    print(f"Total: {get_size(memory.total)}")
    print(f"Available: {get_size(memory.available)}")
    print(f"Used: {get_size(memory.used)}")
    print(f"Percentage: {memory.percent}%")

def print_disk_usage():
    """Print disk usage information"""
    print("\n=== Disk Usage ===")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"\nDrive: {partition.device}")
            print(f"Mountpoint: {partition.mountpoint}")
            print(f"File System: {partition.fstype}")
            print(f"Total: {get_size(usage.total)}")
            print(f"Used: {get_size(usage.used)}")
            print(f"Free: {get_size(usage.free)}")
            print(f"Percentage: {usage.percent}%")
        except:
            continue

def print_network_usage():
    """Print network usage information"""
    print("\n=== Network Usage ===")
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Bytes Received: {get_size(net_io.bytes_recv)}")
    print(f"Packets Sent: {net_io.packets_sent}")
    print(f"Packets Received: {net_io.packets_recv}")

def print_top_processes():
    """Print top processes by CPU and memory usage"""
    print("\n=== Top Processes ===")
    processes = get_processes()
    
    # Sort by CPU usage
    print("\nTop CPU Processes:")
    cpu_processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:5]
    for proc in cpu_processes:
        print(f"PID: {proc['pid']}, Name: {proc['name']}, CPU: {proc['cpu_percent']}%")
    
    # Sort by memory usage
    print("\nTop Memory Processes:")
    mem_processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:5]
    for proc in mem_processes:
        print(f"PID: {proc['pid']}, Name: {proc['name']}, Memory: {proc['memory_percent']}%")

def main():
    try:
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"=== System Monitor - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
            
            print_system_info()
            print_cpu_usage()
            print_memory_usage()
            print_disk_usage()
            print_network_usage()
            print_top_processes()
            
            print("\nPress Ctrl+C to exit")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main() 
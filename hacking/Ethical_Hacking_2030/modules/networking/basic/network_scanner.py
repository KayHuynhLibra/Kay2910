#!/usr/bin/env python3
import socket
import ipaddress
import threading
from queue import Queue
import time

def scan_port(target, port, open_ports):
    """Scan a single port on the target"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    except:
        pass

def get_target(ip):
    """Validate and return target IP"""
    try:
        ipaddress.ip_address(ip)
        return ip
    except ValueError:
        print("Invalid IP address")
        return None

def main():
    # Get target IP
    target = input("Enter target IP: ")
    target = get_target(target)
    if not target:
        return

    # Initialize variables
    open_ports = []
    port_queue = Queue()
    
    # Put ports in queue
    for port in range(1, 1025):
        port_queue.put(port)

    # Create threads
    threads = []
    for _ in range(100):
        thread = threading.Thread(target=worker, args=(target, port_queue, open_ports))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print results
    print("\nOpen ports:")
    for port in sorted(open_ports):
        try:
            service = socket.getservbyport(port)
            print(f"Port {port}: {service}")
        except:
            print(f"Port {port}: unknown")

def worker(target, port_queue, open_ports):
    """Worker function for threads"""
    while not port_queue.empty():
        port = port_queue.get()
        scan_port(target, port, open_ports)
        port_queue.task_done()

if __name__ == "__main__":
    main() 
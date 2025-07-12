#!/usr/bin/env python3
import scapy.all as scapy
import argparse
import sys
import time
from datetime import datetime
import threading
from queue import Queue
import json

class NetworkAnalyzer:
    def __init__(self):
        self.packet_count = 0
        self.packet_data = {}
        self.unique_ips = set()
        self.protocols = {}
        self.packet_queue = Queue()
        self.running = True

    def get_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--interface", dest="interface", help="Interface to capture packets")
        parser.add_argument("-f", "--filter", dest="filter", help="BPF filter")
        parser.add_argument("-o", "--output", dest="output", help="Output file for analysis")
        return parser.parse_args()

    def process_packet(self, packet):
        """Process each captured packet"""
        try:
            # Basic packet information
            packet_info = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'length': len(packet),
                'protocol': packet[scapy.IP].proto if scapy.IP in packet else 'Unknown',
            }

            # IP information
            if scapy.IP in packet:
                packet_info['src_ip'] = packet[scapy.IP].src
                packet_info['dst_ip'] = packet[scapy.IP].dst
                self.unique_ips.add(packet[scapy.IP].src)
                self.unique_ips.add(packet[scapy.IP].dst)

            # TCP/UDP information
            if scapy.TCP in packet:
                packet_info['src_port'] = packet[scapy.TCP].sport
                packet_info['dst_port'] = packet[scapy.TCP].dport
                packet_info['flags'] = packet[scapy.TCP].flags
            elif scapy.UDP in packet:
                packet_info['src_port'] = packet[scapy.UDP].sport
                packet_info['dst_port'] = packet[scapy.UDP].dport

            # Update protocol statistics
            proto = packet_info['protocol']
            self.protocols[proto] = self.protocols.get(proto, 0) + 1

            # Add to packet data
            self.packet_count += 1
            self.packet_data[self.packet_count] = packet_info

            # Print packet summary
            self.print_packet_summary(packet_info)

        except Exception as e:
            print(f"Error processing packet: {e}")

    def print_packet_summary(self, packet_info):
        """Print summary of captured packet"""
        print(f"\nPacket #{self.packet_count}")
        print(f"Time: {packet_info['timestamp']}")
        print(f"Length: {packet_info['length']} bytes")
        if 'src_ip' in packet_info:
            print(f"Source: {packet_info['src_ip']}:{packet_info.get('src_port', 'N/A')}")
            print(f"Destination: {packet_info['dst_ip']}:{packet_info.get('dst_port', 'N/A')}")
        print(f"Protocol: {packet_info['protocol']}")

    def packet_processor(self):
        """Process packets from queue"""
        while self.running:
            try:
                packet = self.packet_queue.get(timeout=1)
                self.process_packet(packet)
                self.packet_queue.task_done()
            except:
                continue

    def start_capture(self, interface, filter_string=None):
        """Start capturing packets"""
        print(f"Starting packet capture on interface {interface}")
        print("Press Ctrl+C to stop")

        # Start packet processor thread
        processor_thread = threading.Thread(target=self.packet_processor)
        processor_thread.start()

        try:
            # Start packet capture
            scapy.sniff(
                iface=interface,
                filter=filter_string,
                prn=lambda x: self.packet_queue.put(x),
                store=0
            )
        except KeyboardInterrupt:
            self.running = False
            processor_thread.join()
            self.print_statistics()

    def print_statistics(self):
        """Print capture statistics"""
        print("\nCapture Statistics:")
        print(f"Total packets captured: {self.packet_count}")
        print(f"Unique IP addresses: {len(self.unique_ips)}")
        print("\nProtocol Distribution:")
        for proto, count in self.protocols.items():
            print(f"Protocol {proto}: {count} packets")

    def save_analysis(self, output_file):
        """Save analysis to file"""
        analysis = {
            'statistics': {
                'total_packets': self.packet_count,
                'unique_ips': len(self.unique_ips),
                'protocols': self.protocols
            },
            'packet_data': self.packet_data
        }
        
        with open(output_file, 'w') as f:
            json.dump(analysis, f, indent=4)
        print(f"\nAnalysis saved to {output_file}")

def main():
    analyzer = NetworkAnalyzer()
    args = analyzer.get_arguments()

    if not args.interface:
        print("Please specify an interface")
        sys.exit(1)

    try:
        analyzer.start_capture(args.interface, args.filter)
        if args.output:
            analyzer.save_analysis(args.output)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
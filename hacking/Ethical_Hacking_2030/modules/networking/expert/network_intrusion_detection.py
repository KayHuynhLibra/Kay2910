#!/usr/bin/env python3
import scapy.all as scapy
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import pandas as pd
from datetime import datetime
import threading
from queue import Queue
import json
import logging
import sys
import os
from collections import defaultdict
import time

class NetworkIntrusionDetection:
    def __init__(self):
        self.packet_queue = Queue()
        self.running = True
        self.model = None
        self.feature_scaler = None
        self.anomaly_threshold = 0.95
        self.packet_features = []
        self.attack_patterns = defaultdict(int)
        self.setup_logging()

    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('ids.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger('NetworkIDS')

    def load_model(self, model_path):
        """Load pre-trained model"""
        try:
            self.model = joblib.load(model_path)
            self.logger.info(f"Model loaded from {model_path}")
        except Exception as e:
            self.logger.error(f"Error loading model: {e}")
            sys.exit(1)

    def extract_features(self, packet):
        """Extract features from packet for analysis"""
        try:
            features = {}
            
            # Basic packet features
            features['length'] = len(packet)
            features['timestamp'] = time.time()
            
            if scapy.IP in packet:
                # IP layer features
                features['ip_version'] = packet[scapy.IP].version
                features['ip_ihl'] = packet[scapy.IP].ihl
                features['ip_tos'] = packet[scapy.IP].tos
                features['ip_len'] = packet[scapy.IP].len
                features['ip_id'] = packet[scapy.IP].id
                features['ip_flags'] = packet[scapy.IP].flags
                features['ip_ttl'] = packet[scapy.IP].ttl
                
                # TCP features
                if scapy.TCP in packet:
                    features['tcp_sport'] = packet[scapy.TCP].sport
                    features['tcp_dport'] = packet[scapy.TCP].dport
                    features['tcp_seq'] = packet[scapy.TCP].seq
                    features['tcp_ack'] = packet[scapy.TCP].ack
                    features['tcp_flags'] = packet[scapy.TCP].flags
                    features['tcp_window'] = packet[scapy.TCP].window
                
                # UDP features
                elif scapy.UDP in packet:
                    features['udp_sport'] = packet[scapy.UDP].sport
                    features['udp_dport'] = packet[scapy.UDP].dport
                    features['udp_len'] = packet[scapy.UDP].len
                
                # ICMP features
                elif scapy.ICMP in packet:
                    features['icmp_type'] = packet[scapy.ICMP].type
                    features['icmp_code'] = packet[scapy.ICMP].code
                
                return features
        except Exception as e:
            self.logger.error(f"Error extracting features: {e}")
            return None

    def detect_anomaly(self, features):
        """Detect anomalies using the model"""
        try:
            # Convert features to numpy array
            feature_vector = np.array([list(features.values())])
            
            # Get anomaly score
            score = self.model.score_samples(feature_vector)
            
            # Check if score is below threshold
            if score < self.anomaly_threshold:
                return True, score
            return False, score
        except Exception as e:
            self.logger.error(f"Error in anomaly detection: {e}")
            return False, None

    def analyze_packet(self, packet):
        """Analyze packet for potential intrusions"""
        try:
            # Extract features
            features = self.extract_features(packet)
            if not features:
                return
            
            # Detect anomaly
            is_anomaly, score = self.detect_anomaly(features)
            
            if is_anomaly:
                # Log potential intrusion
                self.logger.warning(f"Potential intrusion detected! Anomaly score: {score}")
                
                # Analyze attack pattern
                self.analyze_attack_pattern(packet, features)
                
                # Take action
                self.handle_intrusion(packet, features)
        except Exception as e:
            self.logger.error(f"Error analyzing packet: {e}")

    def analyze_attack_pattern(self, packet, features):
        """Analyze and categorize attack patterns"""
        try:
            if scapy.TCP in packet:
                # Port scan detection
                if features['tcp_flags'] == 2:  # SYN flag
                    self.attack_patterns['port_scan'] += 1
                
                # SYN flood detection
                if features['tcp_flags'] == 2 and self.attack_patterns['port_scan'] > 100:
                    self.logger.warning("Potential SYN flood attack detected!")
                
                # Connection flood detection
                if features['tcp_flags'] == 18:  # SYN-ACK
                    self.attack_patterns['connection_flood'] += 1
            
            elif scapy.ICMP in packet:
                # ICMP flood detection
                self.attack_patterns['icmp_flood'] += 1
                if self.attack_patterns['icmp_flood'] > 50:
                    self.logger.warning("Potential ICMP flood attack detected!")
        except Exception as e:
            self.logger.error(f"Error analyzing attack pattern: {e}")

    def handle_intrusion(self, packet, features):
        """Handle detected intrusion"""
        try:
            # Log detailed information
            intrusion_info = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'source_ip': packet[scapy.IP].src if scapy.IP in packet else 'Unknown',
                'destination_ip': packet[scapy.IP].dst if scapy.IP in packet else 'Unknown',
                'protocol': packet[scapy.IP].proto if scapy.IP in packet else 'Unknown',
                'features': features
            }
            
            # Save intrusion information
            with open('intrusions.json', 'a') as f:
                json.dump(intrusion_info, f)
                f.write('\n')
            
            # Implement countermeasures
            self.implement_countermeasures(packet)
        except Exception as e:
            self.logger.error(f"Error handling intrusion: {e}")

    def implement_countermeasures(self, packet):
        """Implement countermeasures for detected intrusion"""
        try:
            if scapy.IP in packet:
                # Block source IP
                self.logger.info(f"Blocking IP: {packet[scapy.IP].src}")
                os.system(f"iptables -A INPUT -s {packet[scapy.IP].src} -j DROP")
                
                # Rate limiting
                if self.attack_patterns['port_scan'] > 100:
                    self.logger.info("Implementing rate limiting")
                    os.system(f"iptables -A INPUT -s {packet[scapy.IP].src} -m limit --limit 1/s -j ACCEPT")
        except Exception as e:
            self.logger.error(f"Error implementing countermeasures: {e}")

    def packet_processor(self):
        """Process packets from queue"""
        while self.running:
            try:
                packet = self.packet_queue.get(timeout=1)
                self.analyze_packet(packet)
                self.packet_queue.task_done()
            except:
                continue

    def start_monitoring(self, interface, filter_string=None):
        """Start network monitoring"""
        self.logger.info(f"Starting network monitoring on interface {interface}")
        
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
        """Print monitoring statistics"""
        self.logger.info("\nMonitoring Statistics:")
        self.logger.info(f"Total attack patterns detected: {sum(self.attack_patterns.values())}")
        self.logger.info("\nAttack Pattern Distribution:")
        for pattern, count in self.attack_patterns.items():
            self.logger.info(f"{pattern}: {count}")

def main():
    ids = NetworkIntrusionDetection()
    
    # Load pre-trained model
    model_path = "network_model.joblib"
    if os.path.exists(model_path):
        ids.load_model(model_path)
    else:
        print("Model file not found. Please train the model first.")
        sys.exit(1)
    
    # Start monitoring
    interface = input("Enter interface to monitor: ")
    filter_string = input("Enter BPF filter (optional): ")
    
    try:
        ids.start_monitoring(interface, filter_string if filter_string else None)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
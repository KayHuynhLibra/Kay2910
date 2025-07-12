import time
from collections import defaultdict
from typing import Dict, Tuple
import logging
from ..monitoring.metrics import track_request

logger = logging.getLogger(__name__)

class RateLimiter:
    def __init__(self, requests_per_minute: int = 60, block_duration: int = 300):
        self.requests_per_minute = requests_per_minute
        self.block_duration = block_duration
        self.requests: Dict[str, list] = defaultdict(list)
        self.blocked_ips: Dict[str, float] = {}

    @track_request
    def is_allowed(self, ip: str) -> Tuple[bool, str]:
        """
        Check if a request from the given IP is allowed.
        Returns (is_allowed, reason)
        """
        current_time = time.time()

        # Check if IP is blocked
        if ip in self.blocked_ips:
            if current_time - self.blocked_ips[ip] < self.block_duration:
                return False, "IP is blocked"
            else:
                del self.blocked_ips[ip]

        # Clean old requests
        self.requests[ip] = [t for t in self.requests[ip] 
                           if current_time - t < 60]

        # Check rate limit
        if len(self.requests[ip]) >= self.requests_per_minute:
            self.blocked_ips[ip] = current_time
            logger.warning(f"IP {ip} blocked due to rate limit exceeded")
            return False, "Rate limit exceeded"

        # Add new request
        self.requests[ip].append(current_time)
        return True, "Request allowed"

    def get_request_count(self, ip: str) -> int:
        """Get the number of requests from an IP in the last minute"""
        current_time = time.time()
        self.requests[ip] = [t for t in self.requests[ip] 
                           if current_time - t < 60]
        return len(self.requests[ip])

    def get_blocked_ips(self) -> Dict[str, float]:
        """Get currently blocked IPs and their block end times"""
        current_time = time.time()
        return {ip: end_time for ip, end_time in self.blocked_ips.items()
                if current_time - end_time < self.block_duration}

    def clear_old_data(self):
        """Clear old request and block data"""
        current_time = time.time()
        
        # Clear old requests
        for ip in list(self.requests.keys()):
            self.requests[ip] = [t for t in self.requests[ip] 
                               if current_time - t < 60]
            if not self.requests[ip]:
                del self.requests[ip]

        # Clear expired blocks
        self.blocked_ips = {ip: end_time for ip, end_time in self.blocked_ips.items()
                           if current_time - end_time < self.block_duration} 
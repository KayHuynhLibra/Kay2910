import pytest
import time
from ..security.rate_limiter import RateLimiter

def test_rate_limiter_initialization():
    limiter = RateLimiter(requests_per_minute=10, block_duration=60)
    assert limiter.requests_per_minute == 10
    assert limiter.block_duration == 60
    assert len(limiter.requests) == 0
    assert len(limiter.blocked_ips) == 0

def test_rate_limiter_allows_requests():
    limiter = RateLimiter(requests_per_minute=5, block_duration=60)
    ip = "192.168.1.1"

    # Should allow 5 requests
    for _ in range(5):
        allowed, reason = limiter.is_allowed(ip)
        assert allowed
        assert reason == "Request allowed"

    # 6th request should be blocked
    allowed, reason = limiter.is_allowed(ip)
    assert not allowed
    assert reason == "Rate limit exceeded"

def test_rate_limiter_block_duration():
    limiter = RateLimiter(requests_per_minute=1, block_duration=1)
    ip = "192.168.1.1"

    # First request allowed
    allowed, _ = limiter.is_allowed(ip)
    assert allowed

    # Second request blocked
    allowed, _ = limiter.is_allowed(ip)
    assert not allowed

    # Wait for block to expire
    time.sleep(1.1)

    # Should be allowed again
    allowed, _ = limiter.is_allowed(ip)
    assert allowed

def test_rate_limiter_request_count():
    limiter = RateLimiter(requests_per_minute=5, block_duration=60)
    ip = "192.168.1.1"

    # Make 3 requests
    for _ in range(3):
        limiter.is_allowed(ip)

    assert limiter.get_request_count(ip) == 3

def test_rate_limiter_clear_old_data():
    limiter = RateLimiter(requests_per_minute=5, block_duration=1)
    ip = "192.168.1.1"

    # Make some requests
    for _ in range(3):
        limiter.is_allowed(ip)

    # Wait for data to expire
    time.sleep(1.1)

    # Clear old data
    limiter.clear_old_data()

    assert len(limiter.requests) == 0
    assert len(limiter.blocked_ips) == 0

def test_rate_limiter_multiple_ips():
    limiter = RateLimiter(requests_per_minute=2, block_duration=60)
    ip1 = "192.168.1.1"
    ip2 = "192.168.1.2"

    # Make requests from different IPs
    for _ in range(2):
        allowed1, _ = limiter.is_allowed(ip1)
        allowed2, _ = limiter.is_allowed(ip2)
        assert allowed1
        assert allowed2

    # Both IPs should be blocked now
    allowed1, _ = limiter.is_allowed(ip1)
    allowed2, _ = limiter.is_allowed(ip2)
    assert not allowed1
    assert not allowed2

def test_rate_limiter_get_blocked_ips():
    limiter = RateLimiter(requests_per_minute=1, block_duration=60)
    ip = "192.168.1.1"

    # Make two requests to get blocked
    limiter.is_allowed(ip)
    limiter.is_allowed(ip)

    blocked_ips = limiter.get_blocked_ips()
    assert ip in blocked_ips
    assert len(blocked_ips) == 1 
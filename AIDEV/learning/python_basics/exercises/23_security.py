"""
Bài tập 23: Security

Mục tiêu:
- Hiểu cách bảo mật ứng dụng Python
- Thực hành với encryption và hashing
- Sử dụng authentication và authorization
"""

import hashlib
import hmac
import base64
import os
import json
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import jwt
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from passlib.context import CryptContext
import bcrypt
import re

# TODO: Password hashing
class PasswordHasher:
    """
    Password hashing implementation
    """
    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["bcrypt"],
            deprecated="auto"
        )
    
    def hash_password(self, password: str) -> str:
        """
        Hash a password
        """
        return self.pwd_context.hash(password)
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """
        Verify a password
        """
        return self.pwd_context.verify(password, hashed)

# TODO: JWT tokens
class JWTManager:
    """
    JWT token management
    """
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
    
    def create_token(self, data: Dict[str, Any], expires_delta: timedelta = None) -> str:
        """
        Create a JWT token
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.secret_key, algorithm="HS256")
    
    def verify_token(self, token: str) -> Dict[str, Any]:
        """
        Verify a JWT token
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.JWTError:
            raise ValueError("Invalid token")

# TODO: Encryption
class Encryptor:
    """
    Encryption implementation
    """
    def __init__(self, key: Optional[bytes] = None):
        if key is None:
            key = Fernet.generate_key()
        self.fernet = Fernet(key)
    
    def encrypt(self, data: str) -> str:
        """
        Encrypt data
        """
        return self.fernet.encrypt(data.encode()).decode()
    
    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypt data
        """
        return self.fernet.decrypt(encrypted_data.encode()).decode()

# TODO: HMAC
class HMACManager:
    """
    HMAC implementation
    """
    def __init__(self, key: bytes):
        self.key = key
    
    def create_hmac(self, message: str) -> str:
        """
        Create HMAC
        """
        h = hmac.new(self.key, message.encode(), hashlib.sha256)
        return base64.b64encode(h.digest()).decode()
    
    def verify_hmac(self, message: str, hmac_value: str) -> bool:
        """
        Verify HMAC
        """
        expected_hmac = self.create_hmac(message)
        return hmac.compare_digest(expected_hmac, hmac_value)

# TODO: Password validation
class PasswordValidator:
    """
    Password validation implementation
    """
    def __init__(self):
        self.min_length = 8
        self.require_uppercase = True
        self.require_lowercase = True
        self.require_digit = True
        self.require_special = True
    
    def validate(self, password: str) -> Tuple[bool, str]:
        """
        Validate password
        """
        if len(password) < self.min_length:
            return False, f"Password must be at least {self.min_length} characters long"
        
        if self.require_uppercase and not re.search(r"[A-Z]", password):
            return False, "Password must contain at least one uppercase letter"
        
        if self.require_lowercase and not re.search(r"[a-z]", password):
            return False, "Password must contain at least one lowercase letter"
        
        if self.require_digit and not re.search(r"\d", password):
            return False, "Password must contain at least one digit"
        
        if self.require_special and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False, "Password must contain at least one special character"
        
        return True, "Password is valid"

# TODO: CSRF protection
class CSRFProtection:
    """
    CSRF protection implementation
    """
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
    
    def generate_token(self) -> str:
        """
        Generate CSRF token
        """
        return base64.b64encode(os.urandom(32)).decode()
    
    def verify_token(self, token: str, stored_token: str) -> bool:
        """
        Verify CSRF token
        """
        return hmac.compare_digest(token, stored_token)

# TODO: Rate limiting
class RateLimiter:
    """
    Rate limiting implementation
    """
    def __init__(self, max_requests: int, time_window: int):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}
    
    def is_allowed(self, key: str) -> bool:
        """
        Check if request is allowed
        """
        now = datetime.utcnow()
        if key not in self.requests:
            self.requests[key] = []
        
        # Remove old requests
        self.requests[key] = [
            req_time for req_time in self.requests[key]
            if now - req_time < timedelta(seconds=self.time_window)
        ]
        
        if len(self.requests[key]) >= self.max_requests:
            return False
        
        self.requests[key].append(now)
        return True

# TODO: Input sanitization
class InputSanitizer:
    """
    Input sanitization implementation
    """
    def __init__(self):
        self.html_pattern = re.compile(r'<[^>]+>')
        self.sql_pattern = re.compile(r'(\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|ALTER)\b)', re.IGNORECASE)
    
    def sanitize(self, input_str: str) -> str:
        """
        Sanitize input
        """
        # Remove HTML tags
        sanitized = self.html_pattern.sub('', input_str)
        
        # Remove SQL injection attempts
        sanitized = self.sql_pattern.sub('', sanitized)
        
        # Escape special characters
        sanitized = sanitized.replace("'", "''")
        sanitized = sanitized.replace('"', '\\"')
        
        return sanitized

# TODO: Secure headers
class SecureHeaders:
    """
    Secure headers implementation
    """
    def __init__(self):
        self.headers = {
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'X-XSS-Protection': '1; mode=block',
            'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
            'Content-Security-Policy': "default-src 'self'",
            'Referrer-Policy': 'strict-origin-when-cross-origin'
        }
    
    def get_headers(self) -> Dict[str, str]:
        """
        Get secure headers
        """
        return self.headers

# TODO: Example usage
def example_usage():
    """
    Example usage of security features
    """
    # Password hashing
    print("Password hashing example:")
    hasher = PasswordHasher()
    password = "SecurePassword123!"
    hashed = hasher.hash_password(password)
    print(f"Original password: {password}")
    print(f"Hashed password: {hashed}")
    print(f"Verification: {hasher.verify_password(password, hashed)}")
    
    # JWT tokens
    print("\nJWT tokens example:")
    jwt_manager = JWTManager("your-secret-key")
    token = jwt_manager.create_token({"user_id": 123})
    print(f"Token: {token}")
    payload = jwt_manager.verify_token(token)
    print(f"Payload: {payload}")
    
    # Encryption
    print("\nEncryption example:")
    encryptor = Encryptor()
    data = "Sensitive data"
    encrypted = encryptor.encrypt(data)
    print(f"Original data: {data}")
    print(f"Encrypted data: {encrypted}")
    decrypted = encryptor.decrypt(encrypted)
    print(f"Decrypted data: {decrypted}")
    
    # HMAC
    print("\nHMAC example:")
    hmac_manager = HMACManager(b"your-secret-key")
    message = "Important message"
    hmac_value = hmac_manager.create_hmac(message)
    print(f"Message: {message}")
    print(f"HMAC: {hmac_value}")
    print(f"Verification: {hmac_manager.verify_hmac(message, hmac_value)}")
    
    # Password validation
    print("\nPassword validation example:")
    validator = PasswordValidator()
    password = "Weak"
    is_valid, message = validator.validate(password)
    print(f"Password: {password}")
    print(f"Validation: {message}")
    
    # CSRF protection
    print("\nCSRF protection example:")
    csrf = CSRFProtection("your-secret-key")
    token = csrf.generate_token()
    print(f"CSRF token: {token}")
    print(f"Verification: {csrf.verify_token(token, token)}")
    
    # Rate limiting
    print("\nRate limiting example:")
    limiter = RateLimiter(max_requests=5, time_window=60)
    key = "user123"
    for i in range(6):
        allowed = limiter.is_allowed(key)
        print(f"Request {i+1}: {'Allowed' if allowed else 'Blocked'}")
    
    # Input sanitization
    print("\nInput sanitization example:")
    sanitizer = InputSanitizer()
    input_str = "<script>alert('XSS')</script> SELECT * FROM users"
    sanitized = sanitizer.sanitize(input_str)
    print(f"Original input: {input_str}")
    print(f"Sanitized input: {sanitized}")
    
    # Secure headers
    print("\nSecure headers example:")
    headers = SecureHeaders()
    print("Secure headers:")
    for key, value in headers.get_headers().items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tạo một hệ thống xác thực cho một ứng dụng FastAPI
2. Tạo một hệ thống mã hóa cho một ứng dụng file transfer
3. Tạo một hệ thống bảo mật cho một ứng dụng chat
4. Tạo một hệ thống bảo mật cho một ứng dụng web với Nginx
5. Tạo một hệ thống bảo mật cho một hệ thống database
""" 
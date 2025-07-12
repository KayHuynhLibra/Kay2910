"""
Bài tập 14: Security

Mục tiêu:
- Hiểu cách bảo mật ứng dụng
- Thực hành với JWT và OAuth2
- Sử dụng encryption và hashing
"""

import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import bcrypt
import hashlib
import secrets
import re

# TODO: Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """
    Xác thực mật khẩu
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """
    Hash mật khẩu
    """
    return pwd_context.hash(password)

# TODO: JWT tokens
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    """
    Tạo JWT token
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """
    Xác thực JWT token
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )

# TODO: OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Lấy thông tin user từ token
    """
    payload = verify_token(token)
    return payload

# TODO: Password validation
def validate_password(password: str) -> bool:
    """
    Kiểm tra độ mạnh của mật khẩu
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

# TODO: CSRF protection
def generate_csrf_token():
    """
    Tạo CSRF token
    """
    return secrets.token_hex(32)

def verify_csrf_token(token: str, stored_token: str):
    """
    Xác thực CSRF token
    """
    return secrets.compare_digest(token, stored_token)

# TODO: Rate limiting
from collections import defaultdict
import time

class RateLimiter:
    def __init__(self, requests_per_minute: int):
        self.requests_per_minute = requests_per_minute
        self.requests = defaultdict(list)
    
    def is_allowed(self, ip: str) -> bool:
        """
        Kiểm tra rate limit
        """
        now = time.time()
        self.requests[ip] = [t for t in self.requests[ip] if now - t < 60]
        if len(self.requests[ip]) >= self.requests_per_minute:
            return False
        self.requests[ip].append(now)
        return True

# TODO: Input sanitization
def sanitize_input(input_str: str) -> str:
    """
    Làm sạch input
    """
    # Loại bỏ HTML tags
    input_str = re.sub(r'<[^>]+>', '', input_str)
    # Loại bỏ SQL injection
    input_str = re.sub(r'[\'";]', '', input_str)
    # Loại bỏ XSS
    input_str = input_str.replace('<', '&lt;').replace('>', '&gt;')
    return input_str

# TODO: Secure headers
def add_security_headers(response):
    """
    Thêm security headers
    """
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response

# TODO: File upload security
def validate_file_upload(file):
    """
    Kiểm tra file upload
    """
    # Kiểm tra file size
    if file.size > 5 * 1024 * 1024:  # 5MB
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File too large"
        )
    
    # Kiểm tra file type
    allowed_types = ["image/jpeg", "image/png", "application/pdf"]
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File type not allowed"
        )

# TODO: Session management
class SessionManager:
    def __init__(self):
        self.sessions = {}
    
    def create_session(self, user_id: str) -> str:
        """
        Tạo session mới
        """
        session_id = secrets.token_hex(32)
        self.sessions[session_id] = {
            "user_id": user_id,
            "created_at": datetime.utcnow(),
            "last_activity": datetime.utcnow()
        }
        return session_id
    
    def validate_session(self, session_id: str) -> bool:
        """
        Xác thực session
        """
        if session_id not in self.sessions:
            return False
        
        session = self.sessions[session_id]
        if datetime.utcnow() - session["last_activity"] > timedelta(hours=1):
            del self.sessions[session_id]
            return False
        
        session["last_activity"] = datetime.utcnow()
        return True

# TODO: Example usage
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Xử lý đăng nhập
    """
    # Kiểm tra rate limit
    rate_limiter = RateLimiter(requests_per_minute=5)
    if not rate_limiter.is_allowed(form_data.username):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests"
        )
    
    # Xác thực mật khẩu
    if not verify_password(form_data.password, get_password_hash(form_data.password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Tạo token
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

"""
Bài tập về nhà:
1. Tạo một hệ thống authentication cho một ứng dụng FastAPI
2. Tạo một hệ thống bảo mật cho một ứng dụng machine learning
3. Tạo một hệ thống bảo mật cho một hệ thống microservices
4. Tạo một hệ thống bảo mật cho một ứng dụng web với Nginx
5. Tạo một hệ thống bảo mật cho một hệ thống database
""" 
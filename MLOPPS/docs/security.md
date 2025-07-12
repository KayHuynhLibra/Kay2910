# Security Guide

## Overview
Hướng dẫn bảo mật cho MLOps platform, bao gồm authentication, authorization, data security, và compliance.

## Authentication

### JWT Authentication
```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta

# JWT configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Token generation
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Token validation
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username
```

### OAuth2 Integration
```python
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config

# OAuth2 configuration
config = Config('.env')
oauth = OAuth(config)

# Google OAuth2
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

# GitHub OAuth2
oauth.register(
    name='github',
    client_id=config('GITHUB_CLIENT_ID'),
    client_secret=config('GITHUB_CLIENT_SECRET'),
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)
```

## Authorization

### Role-Based Access Control (RBAC)
```python
from enum import Enum
from typing import List

class Role(str, Enum):
    ADMIN = "admin"
    DATA_SCIENTIST = "data_scientist"
    ENGINEER = "engineer"
    VIEWER = "viewer"

class Permission(str, Enum):
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    MANAGE = "manage"

# Role permissions mapping
ROLE_PERMISSIONS = {
    Role.ADMIN: [Permission.READ, Permission.WRITE, Permission.DELETE, Permission.MANAGE],
    Role.DATA_SCIENTIST: [Permission.READ, Permission.WRITE],
    Role.ENGINEER: [Permission.READ, Permission.WRITE],
    Role.VIEWER: [Permission.READ]
}

# Permission check
def check_permission(user_role: Role, required_permission: Permission) -> bool:
    return required_permission in ROLE_PERMISSIONS[user_role]
```

### API Authorization
```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

# API endpoint with authorization
@router.get("/models/{model_id}")
async def get_model(
    model_id: str,
    current_user: User = Depends(get_current_user),
    required_permission: Permission = Permission.READ
):
    if not check_permission(current_user.role, required_permission):
        raise HTTPException(
            status_code=403,
            detail="Not enough permissions"
        )
    return await get_model_by_id(model_id)
```

## Data Security

### Data Encryption
```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Encryption key generation
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return kdf.derive(password.encode())

# Data encryption
def encrypt_data(data: str, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(data.encode())

# Data decryption
def decrypt_data(encrypted_data: bytes, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()
```

### Data Masking
```python
import re
from typing import Any, Dict

# Data masking rules
MASKING_RULES = {
    'email': r'[^@]+@[^@]+\.[^@]+',
    'phone': r'\d{10}',
    'credit_card': r'\d{16}'
}

# Data masking function
def mask_sensitive_data(data: Dict[str, Any]) -> Dict[str, Any]:
    masked_data = data.copy()
    for field, value in data.items():
        for pattern in MASKING_RULES.values():
            if isinstance(value, str) and re.match(pattern, value):
                masked_data[field] = '***'
    return masked_data
```

## API Security

### Rate Limiting
```python
from fastapi import Request
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address

# Rate limiter configuration
limiter = Limiter(key_func=get_remote_address)

# Rate limited endpoint
@router.get("/predict")
@limiter.limit("100/minute")
async def predict(request: Request):
    return {"prediction": "result"}
```

### CORS Configuration
```python
from fastapi.middleware.cors import CORSMiddleware

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
    max_age=3600
)
```

## Model Security

### Input Validation
```python
from pydantic import BaseModel, Field, validator
from typing import List, Optional

# Input validation model
class PredictionRequest(BaseModel):
    features: List[float] = Field(..., min_items=1, max_items=100)
    model_id: str = Field(..., min_length=1, max_length=50)
    
    @validator('features')
    def validate_features(cls, v):
        if not all(0 <= x <= 1 for x in v):
            raise ValueError('Features must be between 0 and 1')
        return v
```

### Output Sanitization
```python
from typing import Dict, Any
import numpy as np

# Output sanitization
def sanitize_prediction(prediction: Dict[str, Any]) -> Dict[str, Any]:
    sanitized = {}
    for key, value in prediction.items():
        if isinstance(value, np.ndarray):
            sanitized[key] = value.tolist()
        elif isinstance(value, (int, float)):
            sanitized[key] = float(value)
        else:
            sanitized[key] = str(value)
    return sanitized
```

## Compliance

### GDPR Compliance
```python
from datetime import datetime
from typing import List, Optional

# GDPR data model
class UserData(BaseModel):
    user_id: str
    data_type: str
    created_at: datetime
    expires_at: Optional[datetime]
    consent_given: bool
    data_location: str

# Data retention check
def check_data_retention(user_data: UserData) -> bool:
    if not user_data.consent_given:
        return False
    if user_data.expires_at and user_data.expires_at < datetime.utcnow():
        return False
    return True
```

### HIPAA Compliance
```python
from typing import List, Dict
import re

# PHI detection
PHI_PATTERNS = {
    'ssn': r'\d{3}-\d{2}-\d{4}',
    'medical_record': r'MRN\d{8}',
    'health_insurance': r'HI\d{10}'
}

# PHI detection function
def detect_phi(text: str) -> List[Dict[str, str]]:
    phi_instances = []
    for phi_type, pattern in PHI_PATTERNS.items():
        matches = re.finditer(pattern, text)
        for match in matches:
            phi_instances.append({
                'type': phi_type,
                'value': match.group(),
                'position': match.span()
            })
    return phi_instances
```

## Security Monitoring

### Audit Logging
```python
import logging
from datetime import datetime
from typing import Dict, Any

# Audit logger configuration
audit_logger = logging.getLogger('audit')
audit_logger.setLevel(logging.INFO)
handler = logging.FileHandler('audit.log')
audit_logger.addHandler(handler)

# Audit log function
def log_audit_event(
    event_type: str,
    user_id: str,
    resource: str,
    action: str,
    details: Dict[str, Any]
):
    audit_logger.info(
        f"Event: {event_type} | "
        f"User: {user_id} | "
        f"Resource: {resource} | "
        f"Action: {action} | "
        f"Details: {details} | "
        f"Timestamp: {datetime.utcnow()}"
    )
```

### Security Alerts
```python
from typing import List, Dict
import smtplib
from email.mime.text import MIMEText

# Security alert configuration
ALERT_THRESHOLDS = {
    'failed_login_attempts': 5,
    'suspicious_api_calls': 10,
    'data_access_violations': 1
}

# Alert function
def send_security_alert(
    alert_type: str,
    severity: str,
    details: Dict[str, Any],
    recipients: List[str]
):
    message = MIMEText(
        f"Security Alert: {alert_type}\n"
        f"Severity: {severity}\n"
        f"Details: {details}"
    )
    message['Subject'] = f"Security Alert: {alert_type}"
    message['From'] = "security@example.com"
    message['To'] = ", ".join(recipients)
    
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('security@example.com', 'password')
        server.send_message(message)
```

## Best Practices

### Authentication
- Use strong password policies
- Implement multi-factor authentication
- Regular password rotation
- Secure session management
- Token-based authentication

### Authorization
- Principle of least privilege
- Role-based access control
- Regular permission review
- Access logging
- Permission audit

### Data Security
- Encrypt sensitive data
- Implement data masking
- Secure data transmission
- Regular security audits
- Data backup and recovery

### API Security
- Input validation
- Output sanitization
- Rate limiting
- CORS configuration
- API versioning

### Compliance
- Regular compliance audits
- Data retention policies
- Privacy controls
- Security documentation
- Incident response plan 
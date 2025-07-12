from pydantic import BaseModel, Field, EmailStr, validator
from typing import List, Optional
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    """Vai trò người dùng"""
    ADMIN = "admin"
    DATA_SCIENTIST = "data_scientist"
    ML_ENGINEER = "ml_engineer"
    DEVOPS = "devops"
    VIEWER = "viewer"

class UserStatus(str, Enum):
    """Trạng thái người dùng"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    DELETED = "deleted"

class User(BaseModel):
    """Schema người dùng"""
    id: str
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: Optional[str] = Field(None, max_length=100)
    role: UserRole
    status: UserStatus
    permissions: List[str] = Field(default_factory=list)
    is_active: bool = True
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime] = None

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    """Schema tạo người dùng mới"""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)
    full_name: Optional[str] = Field(None, max_length=100)
    role: UserRole = UserRole.VIEWER

    @validator("password")
    def validate_password(cls, v):
        """Validate password strength"""
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        if not any(c in "!@#$%^&*()" for c in v):
            raise ValueError("Password must contain at least one special character")
        return v

class UserUpdate(BaseModel):
    """Schema cập nhật người dùng"""
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = Field(None, max_length=100)
    role: Optional[UserRole] = None
    status: Optional[UserStatus] = None
    permissions: Optional[List[str]] = None
    is_active: Optional[bool] = None

class UserResponse(BaseModel):
    """Schema response người dùng"""
    id: str
    email: EmailStr
    username: str
    full_name: Optional[str]
    role: UserRole
    status: UserStatus
    permissions: List[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime
    last_login: Optional[datetime]

    class Config:
        orm_mode = True

class Token(BaseModel):
    """Schema token"""
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    refresh_token: Optional[str] = None

class TokenData(BaseModel):
    """Schema dữ liệu token"""
    sub: str
    exp: datetime
    role: UserRole
    permissions: List[str]

class LoginRequest(BaseModel):
    """Schema request đăng nhập"""
    username: str
    password: str

class RefreshTokenRequest(BaseModel):
    """Schema request refresh token"""
    refresh_token: str

class ChangePasswordRequest(BaseModel):
    """Schema request đổi mật khẩu"""
    current_password: str
    new_password: str = Field(..., min_length=8)

    @validator("new_password")
    def validate_new_password(cls, v):
        """Validate new password strength"""
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        if not any(c in "!@#$%^&*()" for c in v):
            raise ValueError("Password must contain at least one special character")
        return v

class ResetPasswordRequest(BaseModel):
    """Schema request reset mật khẩu"""
    email: EmailStr

class VerifyResetTokenRequest(BaseModel):
    """Schema request xác thực token reset"""
    token: str
    new_password: str = Field(..., min_length=8)

    @validator("new_password")
    def validate_new_password(cls, v):
        """Validate new password strength"""
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        if not any(c in "!@#$%^&*()" for c in v):
            raise ValueError("Password must contain at least one special character")
        return v 
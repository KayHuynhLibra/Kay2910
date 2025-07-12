from pydantic import BaseModel, Field, validator, EmailStr
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    """Vai trò người dùng"""
    ADMIN = "admin"
    DATA_SCIENTIST = "data_scientist"
    DATA_ENGINEER = "data_engineer"
    MLOPS_ENGINEER = "mlops_engineer"
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
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: str = Field(..., min_length=3, max_length=100)
    role: UserRole
    status: UserStatus
    permissions: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    updated_at: datetime
    last_login_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    """Schema tạo người dùng mới"""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: str = Field(..., min_length=3, max_length=100)
    password: str = Field(..., min_length=8)
    role: UserRole
    permissions: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class UserUpdate(BaseModel):
    """Schema cập nhật người dùng"""
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, min_length=3, max_length=100)
    role: Optional[UserRole] = None
    status: Optional[UserStatus] = None
    permissions: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None

class UserResponse(BaseModel):
    """Schema response người dùng"""
    id: str
    username: str
    email: EmailStr
    full_name: str
    role: UserRole
    status: UserStatus
    permissions: List[str]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    last_login_at: Optional[datetime]

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    """Schema đăng nhập"""
    username: str
    password: str

class UserToken(BaseModel):
    """Schema token người dùng"""
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    refresh_token: str

class UserPermission(BaseModel):
    """Schema quyền người dùng"""
    id: str
    user_id: str
    resource: str
    action: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class UserPermissionCreate(BaseModel):
    """Schema tạo quyền người dùng mới"""
    user_id: str
    resource: str
    action: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class UserPermissionResponse(BaseModel):
    """Schema response quyền người dùng"""
    id: str
    user_id: str
    resource: str
    action: str
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class UserActivity(BaseModel):
    """Schema hoạt động người dùng"""
    id: str
    user_id: str
    action: str
    resource: str
    resource_id: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime

    class Config:
        orm_mode = True

class UserActivityCreate(BaseModel):
    """Schema tạo hoạt động người dùng mới"""
    user_id: str
    action: str
    resource: str
    resource_id: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class UserActivityResponse(BaseModel):
    """Schema response hoạt động người dùng"""
    id: str
    user_id: str
    action: str
    resource: str
    resource_id: str
    metadata: Dict[str, Any]
    created_at: datetime

    class Config:
        orm_mode = True

class UserProfile(BaseModel):
    """Schema profile user"""
    id: str
    user_id: str
    bio: Optional[str] = Field(None, max_length=500)
    avatar: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserProfileCreate(BaseModel):
    """Schema tạo profile user mới"""
    user_id: str
    bio: Optional[str] = Field(None, max_length=500)
    avatar: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class UserProfileUpdate(BaseModel):
    """Schema cập nhật profile user"""
    bio: Optional[str] = Field(None, max_length=500)
    avatar: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class UserProfileResponse(BaseModel):
    """Schema response profile user"""
    id: str
    user_id: str
    bio: Optional[str]
    avatar: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserSettings(BaseModel):
    """Schema cài đặt user"""
    id: str
    user_id: str
    theme: str = "light"
    language: str = "en"
    notifications: Dict[str, bool] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserSettingsCreate(BaseModel):
    """Schema tạo cài đặt user mới"""
    user_id: str
    theme: str = "light"
    language: str = "en"
    notifications: Dict[str, bool] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class UserSettingsUpdate(BaseModel):
    """Schema cập nhật cài đặt user"""
    theme: Optional[str] = None
    language: Optional[str] = None
    notifications: Optional[Dict[str, bool]] = None
    metadata: Optional[Dict[str, Any]] = None

class UserSettingsResponse(BaseModel):
    """Schema response cài đặt user"""
    id: str
    user_id: str
    theme: str
    language: str
    notifications: Dict[str, bool]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserChangePassword(BaseModel):
    """Schema đổi mật khẩu user"""
    current_password: str
    new_password: str = Field(..., min_length=8)
    confirm_password: str = Field(..., min_length=8)

    @validator('confirm_password')
    def passwords_match(cls, v, values, **kwargs):
        if 'new_password' in values and v != values['new_password']:
            raise ValueError('passwords do not match')
        return v 
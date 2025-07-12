from pydantic import BaseModel, Field, validator, EmailStr
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class OrganizationStatus(str, Enum):
    """Trạng thái organization"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    DELETED = "deleted"

class Organization(BaseModel):
    """Schema organization"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: OrganizationStatus
    owner: str
    members: List[str] = Field(default_factory=list)
    projects: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    created_by: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class OrganizationCreate(BaseModel):
    """Schema tạo organization mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    owner: str
    members: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)

class OrganizationUpdate(BaseModel):
    """Schema cập nhật organization"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[OrganizationStatus] = None
    owner: Optional[str] = None
    members: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None

class OrganizationResponse(BaseModel):
    """Schema response organization"""
    id: str
    name: str
    description: Optional[str]
    status: OrganizationStatus
    owner: str
    members: List[str]
    projects: List[str]
    metadata: Dict[str, Any]
    tags: List[str]
    created_by: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class OrganizationMember(BaseModel):
    """Schema thành viên organization"""
    id: str
    organization_id: str
    user_id: str
    role: str
    permissions: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class OrganizationMemberCreate(BaseModel):
    """Schema tạo thành viên organization mới"""
    organization_id: str
    user_id: str
    role: str
    permissions: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class OrganizationMemberUpdate(BaseModel):
    """Schema cập nhật thành viên organization"""
    role: Optional[str] = None
    permissions: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None

class OrganizationMemberResponse(BaseModel):
    """Schema response thành viên organization"""
    id: str
    organization_id: str
    user_id: str
    role: str
    permissions: List[str]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class OrganizationSettings(BaseModel):
    """Schema cài đặt organization"""
    id: str
    organization_id: str
    settings: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class OrganizationSettingsCreate(BaseModel):
    """Schema tạo cài đặt organization mới"""
    organization_id: str
    settings: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class OrganizationSettingsUpdate(BaseModel):
    """Schema cập nhật cài đặt organization"""
    settings: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

class OrganizationSettingsResponse(BaseModel):
    """Schema response cài đặt organization"""
    id: str
    organization_id: str
    settings: Dict[str, Any]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class OrganizationInvitation(BaseModel):
    """Schema lời mời organization"""
    id: str
    organization_id: str
    email: EmailStr
    role: str
    permissions: List[str] = Field(default_factory=list)
    status: str
    token: str
    expires_at: datetime
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class OrganizationInvitationCreate(BaseModel):
    """Schema tạo lời mời organization mới"""
    organization_id: str
    email: EmailStr
    role: str
    permissions: List[str] = Field(default_factory=list)
    expires_at: datetime

class OrganizationInvitationUpdate(BaseModel):
    """Schema cập nhật lời mời organization"""
    status: Optional[str] = None
    role: Optional[str] = None
    permissions: Optional[List[str]] = None

class OrganizationInvitationResponse(BaseModel):
    """Schema response lời mời organization"""
    id: str
    organization_id: str
    email: EmailStr
    role: str
    permissions: List[str]
    status: str
    token: str
    expires_at: datetime
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True 
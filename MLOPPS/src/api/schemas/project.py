from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class ProjectStatus(str, Enum):
    """Trạng thái project"""
    DRAFT = "draft"
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    ARCHIVED = "archived"

class ProjectType(str, Enum):
    """Loại project"""
    RESEARCH = "research"
    PRODUCTION = "production"
    POC = "poc"
    OTHER = "other"

class Project(BaseModel):
    """Schema project"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: ProjectType
    status: ProjectStatus
    owner_id: str
    members: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class ProjectCreate(BaseModel):
    """Schema tạo project mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: ProjectType
    owner_id: str
    members: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ProjectUpdate(BaseModel):
    """Schema cập nhật project"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: Optional[ProjectType] = None
    status: Optional[ProjectStatus] = None
    members: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None

class ProjectResponse(BaseModel):
    """Schema response project"""
    id: str
    name: str
    description: Optional[str]
    type: ProjectType
    status: ProjectStatus
    owner_id: str
    members: List[str]
    tags: List[str]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime]
    completed_at: Optional[datetime]

    class Config:
        orm_mode = True

class ProjectMember(BaseModel):
    """Schema thành viên project"""
    id: str
    project_id: str
    user_id: str
    role: str
    permissions: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ProjectMemberCreate(BaseModel):
    """Schema tạo thành viên project mới"""
    project_id: str
    user_id: str
    role: str
    permissions: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ProjectMemberResponse(BaseModel):
    """Schema response thành viên project"""
    id: str
    project_id: str
    user_id: str
    role: str
    permissions: List[str]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ProjectResource(BaseModel):
    """Schema tài nguyên project"""
    id: str
    project_id: str
    name: str
    type: str
    path: str
    size: int
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ProjectResourceCreate(BaseModel):
    """Schema tạo tài nguyên project mới"""
    project_id: str
    name: str
    type: str
    path: str
    size: int
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ProjectResourceResponse(BaseModel):
    """Schema response tài nguyên project"""
    id: str
    project_id: str
    name: str
    type: str
    path: str
    size: int
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ProjectActivity(BaseModel):
    """Schema hoạt động project"""
    id: str
    project_id: str
    user_id: str
    action: str
    resource: str
    resource_id: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime

    class Config:
        orm_mode = True

class ProjectActivityCreate(BaseModel):
    """Schema tạo hoạt động project mới"""
    project_id: str
    user_id: str
    action: str
    resource: str
    resource_id: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ProjectActivityResponse(BaseModel):
    """Schema response hoạt động project"""
    id: str
    project_id: str
    user_id: str
    action: str
    resource: str
    resource_id: str
    metadata: Dict[str, Any]
    created_at: datetime

    class Config:
        orm_mode = True 
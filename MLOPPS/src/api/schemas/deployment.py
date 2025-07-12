from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class DeploymentStatus(str, Enum):
    """Trạng thái deployment"""
    PENDING = "pending"
    DEPLOYING = "deploying"
    RUNNING = "running"
    FAILED = "failed"
    SCALING = "scaling"
    UPDATING = "updating"
    ROLLING_BACK = "rolling_back"
    DELETED = "deleted"

class DeploymentType(str, Enum):
    """Loại deployment"""
    KUBERNETES = "kubernetes"
    DOCKER = "docker"
    CLOUD = "cloud"
    EDGE = "edge"
    OTHER = "other"

class ResourceType(str, Enum):
    """Loại tài nguyên"""
    CPU = "cpu"
    MEMORY = "memory"
    GPU = "gpu"
    STORAGE = "storage"

class Deployment(BaseModel):
    """Schema deployment"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: DeploymentType
    status: DeploymentStatus
    model_id: str
    version: str
    environment: str
    replicas: int = 1
    resources: Dict[str, Any] = Field(default_factory=dict)
    config: Dict[str, Any] = Field(default_factory=dict)
    endpoints: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_by: str
    created_at: datetime
    updated_at: datetime
    deployed_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class DeploymentCreate(BaseModel):
    """Schema tạo deployment mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: DeploymentType
    model_id: str
    version: str
    environment: str
    replicas: int = 1
    resources: Dict[str, Any] = Field(default_factory=dict)
    config: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DeploymentUpdate(BaseModel):
    """Schema cập nhật deployment"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[DeploymentStatus] = None
    replicas: Optional[int] = None
    resources: Optional[Dict[str, Any]] = None
    config: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

class DeploymentResponse(BaseModel):
    """Schema response deployment"""
    id: str
    name: str
    description: Optional[str]
    type: DeploymentType
    status: DeploymentStatus
    model_id: str
    version: str
    environment: str
    replicas: int
    resources: Dict[str, Any]
    config: Dict[str, Any]
    endpoints: List[str]
    metadata: Dict[str, Any]
    created_by: str
    created_at: datetime
    updated_at: datetime
    deployed_at: Optional[datetime]

    class Config:
        orm_mode = True

class DeploymentConfig(BaseModel):
    """Schema cấu hình deployment"""
    id: str
    deployment_id: str
    config: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class DeploymentConfigCreate(BaseModel):
    """Schema tạo cấu hình deployment mới"""
    deployment_id: str
    config: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DeploymentConfigUpdate(BaseModel):
    """Schema cập nhật cấu hình deployment"""
    config: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

class DeploymentConfigResponse(BaseModel):
    """Schema response cấu hình deployment"""
    id: str
    deployment_id: str
    config: Dict[str, Any]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class DeploymentEndpoint(BaseModel):
    """Schema endpoint deployment"""
    id: str
    deployment_id: str
    name: str
    url: str
    method: str
    headers: Dict[str, str] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class DeploymentEndpointCreate(BaseModel):
    """Schema tạo endpoint deployment mới"""
    deployment_id: str
    name: str
    url: str
    method: str
    headers: Dict[str, str] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DeploymentEndpointUpdate(BaseModel):
    """Schema cập nhật endpoint deployment"""
    name: Optional[str] = None
    url: Optional[str] = None
    method: Optional[str] = None
    headers: Optional[Dict[str, str]] = None
    metadata: Optional[Dict[str, Any]] = None

class DeploymentEndpointResponse(BaseModel):
    """Schema response endpoint deployment"""
    id: str
    deployment_id: str
    name: str
    url: str
    method: str
    headers: Dict[str, str]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class DeploymentLog(BaseModel):
    """Schema log deployment"""
    id: str
    deployment_id: str
    level: str
    message: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime

    class Config:
        orm_mode = True

class DeploymentLogCreate(BaseModel):
    """Schema tạo log deployment mới"""
    deployment_id: str
    level: str
    message: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DeploymentLogResponse(BaseModel):
    """Schema response log deployment"""
    id: str
    deployment_id: str
    level: str
    message: str
    metadata: Dict[str, Any]
    created_at: datetime

    class Config:
        orm_mode = True

class DeploymentScale(BaseModel):
    """Schema scale deployment"""
    id: str
    deployment_id: str
    replicas: int
    status: DeploymentStatus
    created_at: datetime
    completed_at: Optional[datetime] = None
    created_by: str

    class Config:
        orm_mode = True

class DeploymentScaleCreate(BaseModel):
    """Schema tạo scale deployment mới"""
    replicas: int

class DeploymentScaleResponse(BaseModel):
    """Schema response scale deployment"""
    id: str
    deployment_id: str
    replicas: int
    status: DeploymentStatus
    created_at: datetime
    completed_at: Optional[datetime]
    created_by: str

    class Config:
        orm_mode = True

class DeploymentRollback(BaseModel):
    """Schema rollback deployment"""
    id: str
    deployment_id: str
    version: str
    status: DeploymentStatus
    created_at: datetime
    completed_at: Optional[datetime] = None
    created_by: str

    class Config:
        orm_mode = True

class DeploymentRollbackCreate(BaseModel):
    """Schema tạo rollback deployment mới"""
    version: str

class DeploymentRollbackResponse(BaseModel):
    """Schema response rollback deployment"""
    id: str
    deployment_id: str
    version: str
    status: DeploymentStatus
    created_at: datetime
    completed_at: Optional[datetime]
    created_by: str

    class Config:
        orm_mode = True

class DeploymentHealth(BaseModel):
    """Schema health deployment"""
    id: str
    deployment_id: str
    status: str
    healthy_replicas: int
    total_replicas: int
    last_check: datetime
    details: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        orm_mode = True

class DeploymentHealthResponse(BaseModel):
    """Schema response health deployment"""
    id: str
    deployment_id: str
    status: str
    healthy_replicas: int
    total_replicas: int
    last_check: datetime
    details: Dict[str, Any]

    class Config:
        orm_mode = True

class DeploymentMetrics(BaseModel):
    """Schema metrics deployment"""
    id: str
    deployment_id: str
    timestamp: datetime
    cpu_usage: float
    memory_usage: float
    gpu_usage: Optional[float] = None
    request_count: int
    error_count: int
    latency: float
    details: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        orm_mode = True

class DeploymentMetricsResponse(BaseModel):
    """Schema response metrics deployment"""
    id: str
    deployment_id: str
    timestamp: datetime
    cpu_usage: float
    memory_usage: float
    gpu_usage: Optional[float]
    request_count: int
    error_count: int
    latency: float
    details: Dict[str, Any]

    class Config:
        orm_mode = True 
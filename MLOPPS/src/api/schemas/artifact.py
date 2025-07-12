from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class ArtifactType(str, Enum):
    """Loại artifact"""
    MODEL = "model"
    DATASET = "dataset"
    FEATURE = "feature"
    METRIC = "metric"
    CONFIG = "config"
    LOG = "log"
    VISUALIZATION = "visualization"
    DOCUMENT = "document"
    OTHER = "other"

class ArtifactFormat(str, Enum):
    """Định dạng artifact"""
    PICKLE = "pickle"
    JOBLIB = "joblib"
    H5 = "h5"
    ONNX = "onnx"
    TORCHSCRIPT = "torchscript"
    TENSORFLOW = "tensorflow"
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"
    EXCEL = "excel"
    IMAGE = "image"
    TEXT = "text"
    PDF = "pdf"
    OTHER = "other"

class ArtifactStatus(str, Enum):
    """Trạng thái artifact"""
    UPLOADING = "uploading"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"
    ARCHIVED = "archived"

class Artifact(BaseModel):
    """Schema artifact"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: ArtifactType
    format: ArtifactFormat
    status: ArtifactStatus
    size: int
    version: str
    location: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    created_by: str
    created_at: datetime
    updated_at: datetime
    parent_id: Optional[str] = None
    lineage: List[str] = Field(default_factory=list)

    class Config:
        orm_mode = True

class ArtifactCreate(BaseModel):
    """Schema tạo artifact mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: ArtifactType
    format: ArtifactFormat
    version: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    parent_id: Optional[str] = None
    lineage: List[str] = Field(default_factory=list)

class ArtifactUpdate(BaseModel):
    """Schema cập nhật artifact"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[ArtifactStatus] = None
    metadata: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None

class ArtifactResponse(BaseModel):
    """Schema response artifact"""
    id: str
    name: str
    description: Optional[str]
    type: ArtifactType
    format: ArtifactFormat
    status: ArtifactStatus
    size: int
    version: str
    location: str
    metadata: Dict[str, Any]
    tags: List[str]
    created_by: str
    created_at: datetime
    updated_at: datetime
    parent_id: Optional[str]
    lineage: List[str]

    class Config:
        orm_mode = True

class ArtifactVersion(BaseModel):
    """Schema phiên bản artifact"""
    id: str
    artifact_id: str
    version: str
    size: int
    location: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    is_current: bool = False

    class Config:
        orm_mode = True

class ArtifactVersionCreate(BaseModel):
    """Schema tạo phiên bản artifact mới"""
    version: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ArtifactVersionResponse(BaseModel):
    """Schema response phiên bản artifact"""
    id: str
    artifact_id: str
    version: str
    size: int
    location: str
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    is_current: bool

    class Config:
        orm_mode = True

class ArtifactTag(BaseModel):
    """Schema tag artifact"""
    id: str
    artifact_id: str
    name: str
    description: Optional[str] = Field(None, max_length=500)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ArtifactTagCreate(BaseModel):
    """Schema tạo tag artifact mới"""
    name: str
    description: Optional[str] = Field(None, max_length=500)

class ArtifactTagResponse(BaseModel):
    """Schema response tag artifact"""
    id: str
    artifact_id: str
    name: str
    description: Optional[str]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ArtifactLineage(BaseModel):
    """Schema lineage artifact"""
    id: str
    artifact_id: str
    parent_id: str
    relationship_type: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ArtifactLineageCreate(BaseModel):
    """Schema tạo lineage artifact mới"""
    parent_id: str
    relationship_type: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ArtifactLineageResponse(BaseModel):
    """Schema response lineage artifact"""
    id: str
    artifact_id: str
    parent_id: str
    relationship_type: str
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True 
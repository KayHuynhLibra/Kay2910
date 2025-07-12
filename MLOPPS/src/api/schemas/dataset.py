from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class DatasetType(str, Enum):
    """Loại dataset"""
    TRAINING = "training"
    VALIDATION = "validation"
    TEST = "test"
    PRODUCTION = "production"
    REFERENCE = "reference"
    OTHER = "other"

class DatasetStatus(str, Enum):
    """Trạng thái dataset"""
    DRAFT = "draft"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"
    ARCHIVED = "archived"

class DatasetFormat(str, Enum):
    """Định dạng dataset"""
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"
    EXCEL = "excel"
    HDF5 = "hdf5"
    PICKLE = "pickle"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    TEXT = "text"
    OTHER = "other"

class Dataset(BaseModel):
    """Schema dataset"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: DatasetType
    status: DatasetStatus
    format: DatasetFormat
    version: str
    size: int
    location: str
    schema: Dict[str, Any] = Field(default_factory=dict)
    statistics: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    created_by: str
    created_at: datetime
    updated_at: datetime
    parent_id: Optional[str] = None
    lineage: List[str] = Field(default_factory=list)

    class Config:
        orm_mode = True

class DatasetCreate(BaseModel):
    """Schema tạo dataset mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: DatasetType
    format: DatasetFormat
    location: str
    schema: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    parent_id: Optional[str] = None
    lineage: List[str] = Field(default_factory=list)

class DatasetUpdate(BaseModel):
    """Schema cập nhật dataset"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[DatasetStatus] = None
    schema: Optional[Dict[str, Any]] = None
    statistics: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None

class DatasetResponse(BaseModel):
    """Schema response dataset"""
    id: str
    name: str
    description: Optional[str]
    type: DatasetType
    status: DatasetStatus
    format: DatasetFormat
    version: str
    size: int
    location: str
    schema: Dict[str, Any]
    statistics: Dict[str, Any]
    metadata: Dict[str, Any]
    tags: List[str]
    created_by: str
    created_at: datetime
    updated_at: datetime
    parent_id: Optional[str]
    lineage: List[str]

    class Config:
        orm_mode = True

class DatasetVersion(BaseModel):
    """Schema phiên bản dataset"""
    id: str
    dataset_id: str
    version: str
    schema: Dict[str, Any] = Field(default_factory=dict)
    statistics: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    is_current: bool = False

    class Config:
        orm_mode = True

class DatasetVersionCreate(BaseModel):
    """Schema tạo phiên bản dataset mới"""
    version: str
    schema: Dict[str, Any] = Field(default_factory=dict)
    statistics: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DatasetVersionUpdate(BaseModel):
    """Schema cập nhật phiên bản dataset"""
    schema: Optional[Dict[str, Any]] = None
    statistics: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

class DatasetVersionResponse(BaseModel):
    """Schema response phiên bản dataset"""
    id: str
    dataset_id: str
    version: str
    schema: Dict[str, Any]
    statistics: Dict[str, Any]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    is_current: bool

    class Config:
        orm_mode = True

class DatasetSplit(BaseModel):
    """Schema split dataset"""
    id: str
    dataset_id: str
    name: str
    type: str
    size: int
    location: str
    statistics: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class DatasetSplitCreate(BaseModel):
    """Schema tạo split dataset mới"""
    dataset_id: str
    name: str
    type: str
    location: str
    statistics: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DatasetSplitUpdate(BaseModel):
    """Schema cập nhật split dataset"""
    name: Optional[str] = None
    statistics: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

class DatasetSplitResponse(BaseModel):
    """Schema response split dataset"""
    id: str
    dataset_id: str
    name: str
    type: str
    size: int
    location: str
    statistics: Dict[str, Any]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True 
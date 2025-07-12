from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class DataType(str, Enum):
    """Loại dữ liệu"""
    TRAINING = "training"
    VALIDATION = "validation"
    TEST = "test"
    PRODUCTION = "production"
    OTHER = "other"

class DataFormat(str, Enum):
    """Định dạng dữ liệu"""
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"
    EXCEL = "excel"
    IMAGE = "image"
    TEXT = "text"
    AUDIO = "audio"
    VIDEO = "video"
    OTHER = "other"

class DataStatus(str, Enum):
    """Trạng thái dữ liệu"""
    PENDING = "pending"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"
    ARCHIVED = "archived"

class Data(BaseModel):
    """Schema dữ liệu"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: DataType
    format: DataFormat
    status: DataStatus
    path: str
    size: int
    schema: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_by: str
    created_at: datetime
    updated_at: datetime
    processed_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class DataCreate(BaseModel):
    """Schema tạo dữ liệu mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: DataType
    format: DataFormat
    path: str
    size: int
    schema: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DataUpdate(BaseModel):
    """Schema cập nhật dữ liệu"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[DataStatus] = None
    schema: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

class DataResponse(BaseModel):
    """Schema response dữ liệu"""
    id: str
    name: str
    description: Optional[str]
    type: DataType
    format: DataFormat
    status: DataStatus
    path: str
    size: int
    schema: Dict[str, Any]
    metadata: Dict[str, Any]
    created_by: str
    created_at: datetime
    updated_at: datetime
    processed_at: Optional[datetime]

    class Config:
        orm_mode = True

class DataVersion(BaseModel):
    """Schema version dữ liệu"""
    id: str
    data_id: str
    version: str
    description: Optional[str]
    path: str
    size: int
    schema: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class DataVersionCreate(BaseModel):
    """Schema tạo version dữ liệu mới"""
    data_id: str
    version: str
    description: Optional[str]
    path: str
    size: int
    schema: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DataVersionResponse(BaseModel):
    """Schema response version dữ liệu"""
    id: str
    data_id: str
    version: str
    description: Optional[str]
    path: str
    size: int
    schema: Dict[str, Any]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class DataSchema(BaseModel):
    """Schema schema dữ liệu"""
    id: str
    data_id: str
    name: str
    type: str
    nullable: bool = True
    description: Optional[str]
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class DataSchemaCreate(BaseModel):
    """Schema tạo schema dữ liệu mới"""
    data_id: str
    name: str
    type: str
    nullable: bool = True
    description: Optional[str]
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DataSchemaResponse(BaseModel):
    """Schema response schema dữ liệu"""
    id: str
    data_id: str
    name: str
    type: str
    nullable: bool
    description: Optional[str]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class DataQuality(BaseModel):
    """Schema chất lượng dữ liệu"""
    id: str
    data_id: str
    metric: str
    value: float
    threshold: float
    status: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class DataQualityCreate(BaseModel):
    """Schema tạo chất lượng dữ liệu mới"""
    data_id: str
    metric: str
    value: float
    threshold: float
    status: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DataQualityResponse(BaseModel):
    """Schema response chất lượng dữ liệu"""
    id: str
    data_id: str
    metric: str
    value: float
    threshold: float
    status: str
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class Dataset(BaseModel):
    """Schema dataset"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: DataType
    format: DataFormat
    status: DataStatus
    size: int
    num_records: int
    features: List[str] = Field(default_factory=list)
    target: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_by: str
    created_at: datetime
    updated_at: datetime
    location: str

    class Config:
        orm_mode = True

class DatasetCreate(BaseModel):
    """Schema tạo dataset mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: DataType
    format: DataFormat
    features: List[str] = Field(default_factory=list)
    target: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DatasetUpdate(BaseModel):
    """Schema cập nhật dataset"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: Optional[DataType] = None
    status: Optional[DataStatus] = None
    features: Optional[List[str]] = None
    target: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class DatasetResponse(BaseModel):
    """Schema response dataset"""
    id: str
    name: str
    description: Optional[str]
    type: DataType
    format: DataFormat
    status: DataStatus
    size: int
    num_records: int
    features: List[str]
    target: Optional[str]
    metadata: Dict[str, Any]
    created_by: str
    created_at: datetime
    updated_at: datetime
    location: str

    class Config:
        orm_mode = True

class DataLineage(BaseModel):
    """Schema lineage dữ liệu"""
    id: str
    dataset_id: str
    version: str
    parent_datasets: List[str] = Field(default_factory=list)
    transformations: List[Dict[str, Any]] = Field(default_factory=list)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class DataLineageCreate(BaseModel):
    """Schema tạo lineage dữ liệu mới"""
    parent_datasets: List[str] = Field(default_factory=list)
    transformations: List[Dict[str, Any]] = Field(default_factory=list)

class DataDrift(BaseModel):
    """Schema drift dữ liệu"""
    id: str
    dataset_id: str
    version: str
    reference_version: str
    feature_drift: Dict[str, float] = Field(default_factory=dict)
    distribution_drift: Dict[str, float] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class DataDriftCreate(BaseModel):
    """Schema tạo đánh giá drift dữ liệu mới"""
    reference_version: str
    feature_drift: Dict[str, float] = Field(default_factory=dict)
    distribution_drift: Dict[str, float] = Field(default_factory=dict) 
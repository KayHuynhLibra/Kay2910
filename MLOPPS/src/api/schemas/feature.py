from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class FeatureType(str, Enum):
    """Loại feature"""
    NUMERICAL = "numerical"
    CATEGORICAL = "categorical"
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    TIME_SERIES = "time_series"
    COMPOSITE = "composite"

class FeatureStatus(str, Enum):
    """Trạng thái feature"""
    DRAFT = "draft"
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    ARCHIVED = "archived"

class Feature(BaseModel):
    """Schema feature"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: FeatureType
    status: FeatureStatus
    data_type: str
    default_value: Optional[Any] = None
    validation_rules: Dict[str, Any] = Field(default_factory=dict)
    statistics: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    created_by: str
    created_at: datetime
    updated_at: datetime
    version: str
    parent_id: Optional[str] = None
    lineage: List[str] = Field(default_factory=list)

    class Config:
        orm_mode = True

class FeatureCreate(BaseModel):
    """Schema tạo feature mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: FeatureType
    data_type: str
    default_value: Optional[Any] = None
    validation_rules: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    parent_id: Optional[str] = None
    lineage: List[str] = Field(default_factory=list)

class FeatureUpdate(BaseModel):
    """Schema cập nhật feature"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[FeatureStatus] = None
    default_value: Optional[Any] = None
    validation_rules: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None

class FeatureResponse(BaseModel):
    """Schema response feature"""
    id: str
    name: str
    description: Optional[str]
    type: FeatureType
    status: FeatureStatus
    data_type: str
    default_value: Optional[Any]
    validation_rules: Dict[str, Any]
    statistics: Dict[str, Any]
    metadata: Dict[str, Any]
    tags: List[str]
    created_by: str
    created_at: datetime
    updated_at: datetime
    version: str
    parent_id: Optional[str]
    lineage: List[str]

    class Config:
        orm_mode = True

class FeatureVersion(BaseModel):
    """Schema phiên bản feature"""
    id: str
    feature_id: str
    version: str
    validation_rules: Dict[str, Any] = Field(default_factory=dict)
    statistics: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    is_current: bool = False

    class Config:
        orm_mode = True

class FeatureVersionCreate(BaseModel):
    """Schema tạo phiên bản feature mới"""
    version: str
    validation_rules: Dict[str, Any] = Field(default_factory=dict)
    statistics: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class FeatureVersionResponse(BaseModel):
    """Schema response phiên bản feature"""
    id: str
    feature_id: str
    version: str
    validation_rules: Dict[str, Any]
    statistics: Dict[str, Any]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    is_current: bool

    class Config:
        orm_mode = True

class FeatureSet(BaseModel):
    """Schema feature set"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    features: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    created_by: str
    created_at: datetime
    updated_at: datetime
    version: str

    class Config:
        orm_mode = True

class FeatureSetCreate(BaseModel):
    """Schema tạo feature set mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    features: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)

class FeatureSetUpdate(BaseModel):
    """Schema cập nhật feature set"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    features: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None

class FeatureSetResponse(BaseModel):
    """Schema response feature set"""
    id: str
    name: str
    description: Optional[str]
    features: List[str]
    metadata: Dict[str, Any]
    tags: List[str]
    created_by: str
    created_at: datetime
    updated_at: datetime
    version: str

    class Config:
        orm_mode = True

class FeatureStore(BaseModel):
    """Schema feature store"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: str
    connection: Dict[str, Any] = Field(default_factory=dict)
    features: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_by: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class FeatureStoreCreate(BaseModel):
    """Schema tạo feature store mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: str
    connection: Dict[str, Any] = Field(default_factory=dict)
    features: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class FeatureStoreUpdate(BaseModel):
    """Schema cập nhật feature store"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    connection: Optional[Dict[str, Any]] = None
    features: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None

class FeatureStoreResponse(BaseModel):
    """Schema response feature store"""
    id: str
    name: str
    description: Optional[str]
    type: str
    connection: Dict[str, Any]
    features: List[str]
    metadata: Dict[str, Any]
    created_by: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True 
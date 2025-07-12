from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class ModelType(str, Enum):
    """Loại model"""
    CLASSIFICATION = "classification"
    REGRESSION = "regression"
    CLUSTERING = "clustering"
    DEEP_LEARNING = "deep_learning"
    NLP = "nlp"
    COMPUTER_VISION = "computer_vision"
    RECOMMENDATION = "recommendation"
    OTHER = "other"

class ModelStatus(str, Enum):
    """Trạng thái model"""
    DRAFT = "draft"
    TRAINING = "training"
    EVALUATING = "evaluating"
    READY = "ready"
    DEPLOYED = "deployed"
    FAILED = "failed"
    ARCHIVED = "archived"

class ModelFramework(str, Enum):
    """Framework của model"""
    TENSORFLOW = "tensorflow"
    PYTORCH = "pytorch"
    SCIKIT_LEARN = "scikit-learn"
    XGBOOST = "xgboost"
    LIGHTGBM = "lightgbm"
    CATBOOST = "catboost"
    KERAS = "keras"
    ONNX = "onnx"
    OTHER = "other"

class Model(BaseModel):
    """Schema model"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: ModelType
    status: ModelStatus
    framework: ModelFramework
    version: str
    hyperparameters: Dict[str, Any] = Field(default_factory=dict)
    metrics: Dict[str, float] = Field(default_factory=dict)
    artifacts: List[str] = Field(default_factory=list)
    features: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    created_by: str
    created_at: datetime
    updated_at: datetime
    parent_id: Optional[str] = None
    lineage: List[str] = Field(default_factory=list)
    trained_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class ModelCreate(BaseModel):
    """Schema tạo model mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: ModelType
    framework: ModelFramework
    hyperparameters: Dict[str, Any] = Field(default_factory=dict)
    features: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    parent_id: Optional[str] = None
    lineage: List[str] = Field(default_factory=list)

class ModelUpdate(BaseModel):
    """Schema cập nhật model"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[ModelStatus] = None
    hyperparameters: Optional[Dict[str, Any]] = None
    metrics: Optional[Dict[str, float]] = None
    artifacts: Optional[List[str]] = None
    features: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None

class ModelResponse(BaseModel):
    """Schema response model"""
    id: str
    name: str
    description: Optional[str]
    type: ModelType
    status: ModelStatus
    framework: ModelFramework
    version: str
    hyperparameters: Dict[str, Any]
    metrics: Dict[str, float]
    artifacts: List[str]
    features: List[str]
    metadata: Dict[str, Any]
    tags: List[str]
    created_by: str
    created_at: datetime
    updated_at: datetime
    parent_id: Optional[str]
    lineage: List[str]
    trained_at: Optional[datetime]

    class Config:
        orm_mode = True

class ModelVersion(BaseModel):
    """Schema phiên bản model"""
    id: str
    model_id: str
    version: str
    hyperparameters: Dict[str, Any] = Field(default_factory=dict)
    metrics: Dict[str, float] = Field(default_factory=dict)
    artifacts: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    is_current: bool = False

    class Config:
        orm_mode = True

class ModelVersionCreate(BaseModel):
    """Schema tạo phiên bản model mới"""
    version: str
    hyperparameters: Dict[str, Any] = Field(default_factory=dict)
    metrics: Dict[str, float] = Field(default_factory=dict)
    artifacts: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ModelVersionResponse(BaseModel):
    """Schema response phiên bản model"""
    id: str
    model_id: str
    version: str
    hyperparameters: Dict[str, Any]
    metrics: Dict[str, float]
    artifacts: List[str]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    is_current: bool

    class Config:
        orm_mode = True

class ModelDeployment(BaseModel):
    """Schema deployment model"""
    id: str
    model_id: str
    version: str
    environment: str
    status: str
    endpoint: Optional[str] = None
    replicas: int = 1
    resources: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class ModelDeploymentCreate(BaseModel):
    """Schema tạo deployment model mới"""
    model_id: str
    version: str
    environment: str
    replicas: int = 1
    resources: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ModelDeploymentUpdate(BaseModel):
    """Schema cập nhật deployment model"""
    status: Optional[str] = None
    replicas: Optional[int] = None
    resources: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

class ModelDeploymentResponse(BaseModel):
    """Schema response deployment model"""
    id: str
    model_id: str
    version: str
    environment: str
    status: str
    endpoint: Optional[str]
    replicas: int
    resources: Dict[str, Any]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class ModelMonitoring(BaseModel):
    """Schema monitoring model"""
    id: str
    model_id: str
    version: str
    metrics: Dict[str, float] = Field(default_factory=dict)
    alerts: List[Dict[str, Any]] = Field(default_factory=list)
    drift_metrics: Dict[str, float] = Field(default_factory=dict)
    performance_metrics: Dict[str, float] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ModelMonitoringCreate(BaseModel):
    """Schema tạo monitoring model mới"""
    model_id: str
    version: str
    metrics: Dict[str, float] = Field(default_factory=dict)
    alerts: List[Dict[str, Any]] = Field(default_factory=list)
    drift_metrics: Dict[str, float] = Field(default_factory=dict)
    performance_metrics: Dict[str, float] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ModelMonitoringUpdate(BaseModel):
    """Schema cập nhật monitoring model"""
    metrics: Optional[Dict[str, float]] = None
    alerts: Optional[List[Dict[str, Any]]] = None
    drift_metrics: Optional[Dict[str, float]] = None
    performance_metrics: Optional[Dict[str, float]] = None
    metadata: Optional[Dict[str, Any]] = None

class ModelMonitoringResponse(BaseModel):
    """Schema response monitoring model"""
    id: str
    model_id: str
    version: str
    metrics: Dict[str, float]
    alerts: List[Dict[str, Any]]
    drift_metrics: Dict[str, float]
    performance_metrics: Dict[str, float]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ModelArtifact(BaseModel):
    """Schema artifact model"""
    id: str
    model_id: str
    name: str
    type: str
    path: str
    size: int
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ModelArtifactCreate(BaseModel):
    """Schema tạo artifact model mới"""
    model_id: str
    name: str
    type: str
    path: str
    size: int
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ModelArtifactResponse(BaseModel):
    """Schema response artifact model"""
    id: str
    model_id: str
    name: str
    type: str
    path: str
    size: int
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ModelMetric(BaseModel):
    """Schema metric model"""
    id: str
    model_id: str
    name: str
    value: float
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ModelMetricCreate(BaseModel):
    """Schema tạo metric model mới"""
    model_id: str
    name: str
    value: float
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ModelMetricResponse(BaseModel):
    """Schema response metric model"""
    id: str
    model_id: str
    name: str
    value: float
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ModelParameter(BaseModel):
    """Schema parameter model"""
    id: str
    model_id: str
    name: str
    value: Any
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ModelParameterCreate(BaseModel):
    """Schema tạo parameter model mới"""
    model_id: str
    name: str
    value: Any
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ModelParameterResponse(BaseModel):
    """Schema response parameter model"""
    id: str
    model_id: str
    name: str
    value: Any
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True 
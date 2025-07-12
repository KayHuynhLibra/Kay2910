from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class ExperimentStatus(str, Enum):
    """Trạng thái experiment"""
    DRAFT = "draft"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    ARCHIVED = "archived"

class ExperimentType(str, Enum):
    """Loại experiment"""
    TRAINING = "training"
    EVALUATION = "evaluation"
    HYPERPARAMETER_TUNING = "hyperparameter_tuning"
    FEATURE_ENGINEERING = "feature_engineering"
    MODEL_COMPARISON = "model_comparison"

class Experiment(BaseModel):
    """Schema experiment"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: ExperimentType
    status: ExperimentStatus
    project_id: str
    metrics: Dict[str, float] = Field(default_factory=dict)
    parameters: Dict[str, Any] = Field(default_factory=dict)
    artifacts: List[str] = Field(default_factory=list)
    models: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    created_by: str
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    parent_id: Optional[str] = None
    lineage: List[str] = Field(default_factory=list)

    class Config:
        orm_mode = True

class ExperimentCreate(BaseModel):
    """Schema tạo experiment mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: ExperimentType
    project_id: str
    parameters: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)
    parent_id: Optional[str] = None
    lineage: List[str] = Field(default_factory=list)

class ExperimentUpdate(BaseModel):
    """Schema cập nhật experiment"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: Optional[ExperimentType] = None
    status: Optional[ExperimentStatus] = None
    metrics: Optional[Dict[str, float]] = None
    parameters: Optional[Dict[str, Any]] = None
    artifacts: Optional[List[str]] = None
    models: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
    tags: Optional[List[str]] = None

class ExperimentResponse(BaseModel):
    """Schema response experiment"""
    id: str
    name: str
    description: Optional[str]
    type: ExperimentType
    status: ExperimentStatus
    project_id: str
    metrics: Dict[str, float]
    parameters: Dict[str, Any]
    artifacts: List[str]
    models: List[str]
    metadata: Dict[str, Any]
    tags: List[str]
    created_by: str
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime]
    ended_at: Optional[datetime]
    parent_id: Optional[str]
    lineage: List[str]

    class Config:
        orm_mode = True

class ExperimentRun(BaseModel):
    """Schema experiment run"""
    id: str
    experiment_id: str
    status: str
    metrics: Dict[str, float] = Field(default_factory=dict)
    parameters: Dict[str, Any] = Field(default_factory=dict)
    artifacts: List[str] = Field(default_factory=list)
    models: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class ExperimentRunCreate(BaseModel):
    """Schema tạo experiment run mới"""
    experiment_id: str
    parameters: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ExperimentRunUpdate(BaseModel):
    """Schema cập nhật experiment run"""
    status: Optional[str] = None
    metrics: Optional[Dict[str, float]] = None
    parameters: Optional[Dict[str, Any]] = None
    artifacts: Optional[List[str]] = None
    models: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None

class ExperimentRunResponse(BaseModel):
    """Schema response experiment run"""
    id: str
    experiment_id: str
    status: str
    metrics: Dict[str, float]
    parameters: Dict[str, Any]
    artifacts: List[str]
    models: List[str]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    started_at: Optional[datetime]
    ended_at: Optional[datetime]

    class Config:
        orm_mode = True

class ExperimentMetrics(BaseModel):
    """Schema metrics experiment"""
    id: str
    experiment_id: str
    run_id: str
    metrics: Dict[str, float] = Field(default_factory=dict)
    parameters: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ExperimentMetricsCreate(BaseModel):
    """Schema tạo metrics experiment mới"""
    experiment_id: str
    run_id: str
    metrics: Dict[str, float] = Field(default_factory=dict)
    parameters: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ExperimentMetricsUpdate(BaseModel):
    """Schema cập nhật metrics experiment"""
    metrics: Optional[Dict[str, float]] = None
    parameters: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

class ExperimentMetricsResponse(BaseModel):
    """Schema response metrics experiment"""
    id: str
    experiment_id: str
    run_id: str
    metrics: Dict[str, float]
    parameters: Dict[str, Any]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ExperimentComparison(BaseModel):
    """Schema so sánh experiment"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    experiment_ids: List[str] = Field(default_factory=list)
    metrics: Dict[str, List[float]] = Field(default_factory=dict)
    parameters: Dict[str, List[Any]] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ExperimentComparisonCreate(BaseModel):
    """Schema tạo so sánh experiment mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    experiment_ids: List[str] = Field(default_factory=list)

class ExperimentComparisonResponse(BaseModel):
    """Schema response so sánh experiment"""
    id: str
    name: str
    description: Optional[str]
    experiment_ids: List[str]
    metrics: Dict[str, List[float]]
    parameters: Dict[str, List[Any]]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ExperimentArtifact(BaseModel):
    """Schema artifact experiment"""
    id: str
    experiment_id: str
    run_id: str
    name: str
    type: str
    path: str
    size: int
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ExperimentArtifactCreate(BaseModel):
    """Schema tạo artifact experiment mới"""
    experiment_id: str
    run_id: str
    name: str
    type: str
    path: str
    size: int
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ExperimentArtifactResponse(BaseModel):
    """Schema response artifact experiment"""
    id: str
    experiment_id: str
    run_id: str
    name: str
    type: str
    path: str
    size: int
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str

    class Config:
        orm_mode = True 
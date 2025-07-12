from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class PipelineStatus(str, Enum):
    """Trạng thái pipeline"""
    DRAFT = "draft"
    SCHEDULED = "scheduled"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    PAUSED = "paused"
    CANCELLED = "cancelled"

class PipelineType(str, Enum):
    """Loại pipeline"""
    TRAINING = "training"
    EVALUATION = "evaluation"
    INFERENCE = "inference"
    DATA_PROCESSING = "data_processing"
    FEATURE_ENGINEERING = "feature_engineering"
    MODEL_SERVING = "model_serving"

class PipelineTrigger(str, Enum):
    """Loại trigger pipeline"""
    MANUAL = "manual"
    SCHEDULE = "schedule"
    EVENT = "event"
    API = "api"

class Pipeline(BaseModel):
    """Schema pipeline"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: PipelineType
    status: PipelineStatus
    trigger: PipelineTrigger
    schedule: Optional[str] = None
    steps: List[Dict[str, Any]] = Field(default_factory=list)
    parameters: Dict[str, Any] = Field(default_factory=dict)
    artifacts: Dict[str, str] = Field(default_factory=dict)
    created_by: str
    created_at: datetime
    updated_at: datetime
    last_run_at: Optional[datetime] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        orm_mode = True

class PipelineCreate(BaseModel):
    """Schema tạo pipeline mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: PipelineType
    trigger: PipelineTrigger
    schedule: Optional[str] = None
    steps: List[Dict[str, Any]] = Field(default_factory=list)
    parameters: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class PipelineUpdate(BaseModel):
    """Schema cập nhật pipeline"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[PipelineStatus] = None
    trigger: Optional[PipelineTrigger] = None
    schedule: Optional[str] = None
    steps: Optional[List[Dict[str, Any]]] = None
    parameters: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

class PipelineResponse(BaseModel):
    """Schema response pipeline"""
    id: str
    name: str
    description: Optional[str]
    type: PipelineType
    status: PipelineStatus
    trigger: PipelineTrigger
    schedule: Optional[str]
    steps: List[Dict[str, Any]]
    parameters: Dict[str, Any]
    artifacts: Dict[str, str]
    created_by: str
    created_at: datetime
    updated_at: datetime
    last_run_at: Optional[datetime]
    metadata: Dict[str, Any]

    class Config:
        orm_mode = True

class PipelineRun(BaseModel):
    """Schema pipeline run"""
    id: str
    pipeline_id: str
    run_number: int
    status: PipelineStatus
    parameters: Dict[str, Any] = Field(default_factory=dict)
    artifacts: Dict[str, str] = Field(default_factory=dict)
    started_at: datetime
    completed_at: Optional[datetime] = None
    created_by: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        orm_mode = True

class PipelineRunCreate(BaseModel):
    """Schema tạo pipeline run mới"""
    parameters: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class PipelineRunUpdate(BaseModel):
    """Schema cập nhật pipeline run"""
    status: Optional[PipelineStatus] = None
    parameters: Optional[Dict[str, Any]] = None
    artifacts: Optional[Dict[str, str]] = None
    metadata: Optional[Dict[str, Any]] = None

class PipelineRunResponse(BaseModel):
    """Schema response pipeline run"""
    id: str
    pipeline_id: str
    run_number: int
    status: PipelineStatus
    parameters: Dict[str, Any]
    artifacts: Dict[str, str]
    started_at: datetime
    completed_at: Optional[datetime]
    created_by: str
    metadata: Dict[str, Any]

    class Config:
        orm_mode = True

class PipelineStep(BaseModel):
    """Schema pipeline step"""
    id: str
    pipeline_id: str
    run_id: str
    name: str
    status: PipelineStatus
    start_time: datetime
    end_time: Optional[datetime] = None
    inputs: Dict[str, Any] = Field(default_factory=dict)
    outputs: Dict[str, Any] = Field(default_factory=dict)
    logs: List[str] = Field(default_factory=list)
    error: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        orm_mode = True

class PipelineStepResponse(BaseModel):
    """Schema response pipeline step"""
    id: str
    pipeline_id: str
    run_id: str
    name: str
    status: PipelineStatus
    start_time: datetime
    end_time: Optional[datetime]
    inputs: Dict[str, Any]
    outputs: Dict[str, Any]
    logs: List[str]
    error: Optional[str]
    metadata: Dict[str, Any]

    class Config:
        orm_mode = True

class PipelineSchedule(BaseModel):
    """Schema pipeline schedule"""
    id: str
    pipeline_id: str
    cron_expression: str
    timezone: str
    is_active: bool = True
    last_run_at: Optional[datetime] = None
    next_run_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    created_by: str
    metadata: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        orm_mode = True

class PipelineScheduleCreate(BaseModel):
    """Schema tạo pipeline schedule mới"""
    cron_expression: str
    timezone: str
    is_active: bool = True
    metadata: Dict[str, Any] = Field(default_factory=dict)

class PipelineScheduleUpdate(BaseModel):
    """Schema cập nhật pipeline schedule"""
    cron_expression: Optional[str] = None
    timezone: Optional[str] = None
    is_active: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None

class PipelineScheduleResponse(BaseModel):
    """Schema response pipeline schedule"""
    id: str
    pipeline_id: str
    cron_expression: str
    timezone: str
    is_active: bool
    last_run_at: Optional[datetime]
    next_run_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    created_by: str
    metadata: Dict[str, Any]

    class Config:
        orm_mode = True 
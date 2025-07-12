from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class MetricType(str, Enum):
    """Loại metric"""
    COUNTER = "counter"
    GAUGE = "gauge"
    HISTOGRAM = "histogram"
    SUMMARY = "summary"

class AlertSeverity(str, Enum):
    """Mức độ nghiêm trọng của alert"""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

class AlertStatus(str, Enum):
    """Trạng thái alert"""
    ACTIVE = "active"
    ACKNOWLEDGED = "acknowledged"
    RESOLVED = "resolved"
    EXPIRED = "expired"

class AlertType(str, Enum):
    """Loại alert"""
    SYSTEM = "system"
    MODEL = "model"
    DATA = "data"
    API = "api"
    SECURITY = "security"

class Alert(BaseModel):
    """Schema alert"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: AlertType
    severity: AlertSeverity
    status: AlertStatus
    source: str
    metric: str
    threshold: float
    current_value: float
    triggered_at: datetime
    resolved_at: Optional[datetime] = None
    acknowledged_at: Optional[datetime] = None
    acknowledged_by: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        orm_mode = True

class AlertCreate(BaseModel):
    """Schema tạo alert mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: AlertType
    severity: AlertSeverity
    source: str
    metric: str
    threshold: float
    metadata: Dict[str, Any] = Field(default_factory=dict)

class AlertUpdate(BaseModel):
    """Schema cập nhật alert"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    severity: Optional[AlertSeverity] = None
    status: Optional[AlertStatus] = None
    threshold: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None

class AlertResponse(BaseModel):
    """Schema response alert"""
    id: str
    name: str
    description: Optional[str]
    type: AlertType
    severity: AlertSeverity
    status: AlertStatus
    source: str
    metric: str
    threshold: float
    current_value: float
    triggered_at: datetime
    resolved_at: Optional[datetime]
    acknowledged_at: Optional[datetime]
    acknowledged_by: Optional[str]
    metadata: Dict[str, Any]

    class Config:
        orm_mode = True

class Metric(BaseModel):
    """Schema metric"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: MetricType
    labels: Dict[str, str] = Field(default_factory=dict)
    value: float
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class MetricCreate(BaseModel):
    """Schema tạo metric mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: MetricType
    labels: Dict[str, str] = Field(default_factory=dict)
    value: float
    timestamp: datetime
    metadata: Dict[str, Any] = Field(default_factory=dict)

class MetricUpdate(BaseModel):
    """Schema cập nhật metric"""
    description: Optional[str] = Field(None, max_length=500)
    labels: Optional[Dict[str, str]] = None
    value: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None

class MetricResponse(BaseModel):
    """Schema response metric"""
    id: str
    name: str
    description: Optional[str]
    type: MetricType
    labels: Dict[str, str]
    value: float
    timestamp: datetime
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Dashboard(BaseModel):
    """Schema dashboard"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    panels: List[Dict[str, Any]] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class DashboardCreate(BaseModel):
    """Schema tạo dashboard mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    panels: List[Dict[str, Any]] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class DashboardUpdate(BaseModel):
    """Schema cập nhật dashboard"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    panels: Optional[List[Dict[str, Any]]] = None
    metadata: Optional[Dict[str, Any]] = None

class DashboardResponse(BaseModel):
    """Schema response dashboard"""
    id: str
    name: str
    description: Optional[str]
    panels: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class Log(BaseModel):
    """Schema log"""
    id: str
    level: str
    message: str
    source: str
    timestamp: datetime
    trace_id: Optional[str] = None
    span_id: Optional[str] = None
    labels: Dict[str, str] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        orm_mode = True

class LogCreate(BaseModel):
    """Schema tạo log mới"""
    level: str
    message: str
    source: str
    trace_id: Optional[str] = None
    span_id: Optional[str] = None
    labels: Dict[str, str] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class LogResponse(BaseModel):
    """Schema response log"""
    id: str
    level: str
    message: str
    source: str
    timestamp: datetime
    trace_id: Optional[str]
    span_id: Optional[str]
    labels: Dict[str, str]
    metadata: Dict[str, Any]

    class Config:
        orm_mode = True

class AlertRule(BaseModel):
    """Schema alert rule"""
    id: str
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    severity: AlertSeverity
    metric_id: str
    condition: Dict[str, Any] = Field(default_factory=dict)
    threshold: float
    duration: str
    labels: Dict[str, str] = Field(default_factory=dict)
    annotations: Dict[str, str] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True

class AlertRuleCreate(BaseModel):
    """Schema tạo alert rule mới"""
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    severity: AlertSeverity
    metric_id: str
    condition: Dict[str, Any] = Field(default_factory=dict)
    threshold: float
    duration: str
    labels: Dict[str, str] = Field(default_factory=dict)
    annotations: Dict[str, str] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class AlertRuleUpdate(BaseModel):
    """Schema cập nhật alert rule"""
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    severity: Optional[AlertSeverity] = None
    condition: Optional[Dict[str, Any]] = None
    threshold: Optional[float] = None
    duration: Optional[str] = None
    labels: Optional[Dict[str, str]] = None
    annotations: Optional[Dict[str, str]] = None
    metadata: Optional[Dict[str, Any]] = None

class AlertRuleResponse(BaseModel):
    """Schema response alert rule"""
    id: str
    name: str
    description: Optional[str]
    severity: AlertSeverity
    metric_id: str
    condition: Dict[str, Any]
    threshold: float
    duration: str
    labels: Dict[str, str]
    annotations: Dict[str, str]
    metadata: Dict[str, Any]
    created_at: datetime
    created_by: str
    updated_at: datetime

    class Config:
        orm_mode = True 
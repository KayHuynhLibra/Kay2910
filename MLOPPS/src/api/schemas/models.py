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

class ModelStatus(str, Enum):
    """Trạng thái model"""
    DRAFT = "draft"
    TRAINING = "training"
    EVALUATING = "evaluating"
    READY = "ready"
    DEPLOYED = "deployed"
    FAILED = "failed"

class ModelCreate(BaseModel):
    """Schema tạo model mới"""
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    type: ModelType
    version: str = Field(..., regex=r"^\d+\.\d+\.\d+$")
    hyperparameters: Dict[str, Any] = Field(default_factory=dict)
    features: List[str] = Field(default_factory=list)
    target: str
    metrics: Optional[Dict[str, float]] = Field(default_factory=dict)

    @validator("version")
    def validate_version(cls, v):
        """Validate version format"""
        try:
            major, minor, patch = map(int, v.split("."))
            if major < 0 or minor < 0 or patch < 0:
                raise ValueError("Version numbers must be non-negative")
            return v
        except ValueError:
            raise ValueError("Version must be in format X.Y.Z")

class ModelUpdate(BaseModel):
    """Schema cập nhật model"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[ModelStatus]
    hyperparameters: Optional[Dict[str, Any]]
    metrics: Optional[Dict[str, float]]

class ModelResponse(BaseModel):
    """Schema response model"""
    id: str
    name: str
    description: Optional[str]
    type: ModelType
    version: str
    status: ModelStatus
    hyperparameters: Dict[str, Any]
    features: List[str]
    target: str
    metrics: Dict[str, float]
    created_at: datetime
    updated_at: datetime
    created_by: str

    class Config:
        orm_mode = True

class ModelList(BaseModel):
    """Schema danh sách model"""
    total: int
    items: List[ModelResponse]
    page: int
    size: int
    pages: int

class ModelMetrics(BaseModel):
    """Schema metrics của model"""
    model_id: str
    accuracy: Optional[float]
    precision: Optional[float]
    recall: Optional[float]
    f1_score: Optional[float]
    rmse: Optional[float]
    mae: Optional[float]
    r2_score: Optional[float]
    confusion_matrix: Optional[Dict[str, int]]
    feature_importance: Optional[Dict[str, float]]
    training_time: Optional[float]
    inference_time: Optional[float]
    drift_score: Optional[float]
    last_updated: datetime

    class Config:
        orm_mode = True

class ModelPrediction(BaseModel):
    """Schema dự đoán của model"""
    model_id: str
    prediction: Any
    probability: Optional[float]
    features: Dict[str, Any]
    timestamp: datetime

    class Config:
        orm_mode = True

class ModelTrainingConfig(BaseModel):
    """Schema cấu hình training"""
    train_size: float = Field(0.8, ge=0.1, le=0.9)
    validation_size: float = Field(0.1, ge=0.05, le=0.3)
    test_size: float = Field(0.1, ge=0.05, le=0.3)
    random_state: int = 42
    cross_validation: bool = True
    n_splits: int = Field(5, ge=2, le=10)
    early_stopping: bool = True
    patience: int = Field(10, ge=1)
    max_epochs: int = Field(100, ge=1)
    batch_size: int = Field(32, ge=1)
    learning_rate: float = Field(0.001, ge=0.0001, le=1.0)

    @validator("train_size", "validation_size", "test_size")
    def validate_split_sizes(cls, v, values):
        """Validate tổng các split size bằng 1"""
        if "train_size" in values and "validation_size" in values:
            if values["train_size"] + values["validation_size"] + v != 1.0:
                raise ValueError("Sum of split sizes must equal 1.0")
        return v 
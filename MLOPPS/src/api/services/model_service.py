from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid

from ..schemas.models import (
    ModelCreate,
    ModelUpdate,
    ModelResponse,
    ModelList,
    ModelMetrics,
    ModelStatus
)
from ..utils.exceptions import ModelNotFoundError, ValidationError
from ...models.registry.model_registry import ModelRegistry
from ...models.training.trainer import ModelTrainer
from ...models.evaluation.metrics import ModelEvaluator
from ...models.monitoring.drift_detection import DriftDetector

class ModelService:
    """Service quản lý model"""

    def __init__(self):
        self.model_registry = ModelRegistry()
        self.model_trainer = ModelTrainer()
        self.model_evaluator = ModelEvaluator()
        self.drift_detector = DriftDetector()

    async def create_model(self, model: ModelCreate, user_id: str) -> ModelResponse:
        """
        Tạo model mới
        
        Args:
            model: Thông tin model cần tạo
            user_id: ID của người tạo
            
        Returns:
            ModelResponse: Thông tin model đã tạo
            
        Raises:
            ValidationError: Lỗi validation
        """
        # Validate input
        if not model.features:
            raise ValidationError("Features cannot be empty")
        
        # Create model record
        model_id = str(uuid.uuid4())
        model_data = {
            "id": model_id,
            "name": model.name,
            "description": model.description,
            "type": model.type,
            "version": model.version,
            "status": ModelStatus.DRAFT,
            "hyperparameters": model.hyperparameters,
            "features": model.features,
            "target": model.target,
            "metrics": model.metrics or {},
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "created_by": user_id
        }
        
        # Save to registry
        await self.model_registry.register_model(model_data)
        
        return ModelResponse(**model_data)

    async def list_models(
        self,
        skip: int = 0,
        limit: int = 10
    ) -> ModelList:
        """
        Lấy danh sách model
        
        Args:
            skip: Số lượng bản ghi bỏ qua
            limit: Số lượng bản ghi tối đa
            
        Returns:
            ModelList: Danh sách model
        """
        # Get models from registry
        models = await self.model_registry.list_models(skip, limit)
        total = await self.model_registry.count_models()
        
        return ModelList(
            total=total,
            items=[ModelResponse(**model) for model in models],
            page=skip // limit + 1,
            size=limit,
            pages=(total + limit - 1) // limit
        )

    async def get_model(self, model_id: str) -> ModelResponse:
        """
        Lấy thông tin model
        
        Args:
            model_id: ID của model
            
        Returns:
            ModelResponse: Thông tin model
            
        Raises:
            ModelNotFoundError: Model không tồn tại
        """
        # Get model from registry
        model = await self.model_registry.get_model(model_id)
        if not model:
            raise ModelNotFoundError(f"Model {model_id} not found")
            
        return ModelResponse(**model)

    async def update_model(
        self,
        model_id: str,
        model: ModelUpdate
    ) -> ModelResponse:
        """
        Cập nhật thông tin model
        
        Args:
            model_id: ID của model
            model: Thông tin cập nhật
            
        Returns:
            ModelResponse: Thông tin model đã cập nhật
            
        Raises:
            ModelNotFoundError: Model không tồn tại
            ValidationError: Lỗi validation
        """
        # Get existing model
        existing_model = await self.model_registry.get_model(model_id)
        if not existing_model:
            raise ModelNotFoundError(f"Model {model_id} not found")
            
        # Update model data
        update_data = model.dict(exclude_unset=True)
        update_data["updated_at"] = datetime.utcnow()
        
        # Save to registry
        updated_model = await self.model_registry.update_model(
            model_id,
            update_data
        )
        
        return ModelResponse(**updated_model)

    async def delete_model(self, model_id: str) -> None:
        """
        Xóa model
        
        Args:
            model_id: ID của model
            
        Raises:
            ModelNotFoundError: Model không tồn tại
        """
        # Check if model exists
        if not await self.model_registry.get_model(model_id):
            raise ModelNotFoundError(f"Model {model_id} not found")
            
        # Delete from registry
        await self.model_registry.delete_model(model_id)

    async def get_model_metrics(
        self,
        model_id: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> ModelMetrics:
        """
        Lấy metrics của model
        
        Args:
            model_id: ID của model
            start_date: Ngày bắt đầu
            end_date: Ngày kết thúc
            
        Returns:
            ModelMetrics: Metrics của model
            
        Raises:
            ModelNotFoundError: Model không tồn tại
        """
        # Get model
        model = await self.model_registry.get_model(model_id)
        if not model:
            raise ModelNotFoundError(f"Model {model_id} not found")
            
        # Get metrics
        metrics = await self.model_evaluator.get_metrics(
            model_id,
            start_date,
            end_date
        )
        
        # Get drift score
        drift_score = await self.drift_detector.get_drift_score(
            model_id,
            start_date,
            end_date
        )
        
        return ModelMetrics(
            model_id=model_id,
            **metrics,
            drift_score=drift_score,
            last_updated=datetime.utcnow()
        )

    async def train_model(
        self,
        model_id: str,
        training_config: Dict[str, Any]
    ) -> ModelResponse:
        """
        Training model
        
        Args:
            model_id: ID của model
            training_config: Cấu hình training
            
        Returns:
            ModelResponse: Thông tin model sau khi training
            
        Raises:
            ModelNotFoundError: Model không tồn tại
            ValidationError: Lỗi validation
        """
        # Get model
        model = await self.model_registry.get_model(model_id)
        if not model:
            raise ModelNotFoundError(f"Model {model_id} not found")
            
        # Update status
        await self.model_registry.update_model(
            model_id,
            {"status": ModelStatus.TRAINING}
        )
        
        try:
            # Train model
            trained_model = await self.model_trainer.train(
                model_id,
                training_config
            )
            
            # Evaluate model
            metrics = await self.model_evaluator.evaluate(
                model_id,
                trained_model
            )
            
            # Update model
            update_data = {
                "status": ModelStatus.READY,
                "metrics": metrics,
                "updated_at": datetime.utcnow()
            }
            
            updated_model = await self.model_registry.update_model(
                model_id,
                update_data
            )
            
            return ModelResponse(**updated_model)
            
        except Exception as e:
            # Update status to failed
            await self.model_registry.update_model(
                model_id,
                {
                    "status": ModelStatus.FAILED,
                    "updated_at": datetime.utcnow()
                }
            )
            raise e 
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from datetime import datetime

from ..schemas.models import (
    ModelCreate,
    ModelUpdate,
    ModelResponse,
    ModelList,
    ModelMetrics
)
from ..services.model_service import ModelService
from ..middleware.auth import get_current_user
from ..utils.exceptions import ModelNotFoundError, ValidationError

router = APIRouter(prefix="/models", tags=["models"])

@router.post("/", response_model=ModelResponse, status_code=status.HTTP_201_CREATED)
async def create_model(
    model: ModelCreate,
    current_user = Depends(get_current_user),
    model_service: ModelService = Depends()
):
    """
    Tạo một model mới
    
    Args:
        model: Thông tin model cần tạo
        current_user: Người dùng hiện tại
        model_service: Service quản lý model
        
    Returns:
        ModelResponse: Thông tin model đã tạo
        
    Raises:
        HTTPException: Lỗi validation hoặc server
    """
    try:
        return await model_service.create_model(model, current_user)
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

@router.get("/", response_model=ModelList)
async def list_models(
    skip: int = 0,
    limit: int = 10,
    current_user = Depends(get_current_user),
    model_service: ModelService = Depends()
):
    """
    Lấy danh sách các model
    
    Args:
        skip: Số lượng bản ghi bỏ qua
        limit: Số lượng bản ghi tối đa
        current_user: Người dùng hiện tại
        model_service: Service quản lý model
        
    Returns:
        ModelList: Danh sách model
    """
    return await model_service.list_models(skip, limit)

@router.get("/{model_id}", response_model=ModelResponse)
async def get_model(
    model_id: str,
    current_user = Depends(get_current_user),
    model_service: ModelService = Depends()
):
    """
    Lấy thông tin chi tiết của một model
    
    Args:
        model_id: ID của model
        current_user: Người dùng hiện tại
        model_service: Service quản lý model
        
    Returns:
        ModelResponse: Thông tin model
        
    Raises:
        HTTPException: Model không tồn tại
    """
    try:
        return await model_service.get_model(model_id)
    except ModelNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Model not found"
        )

@router.put("/{model_id}", response_model=ModelResponse)
async def update_model(
    model_id: str,
    model: ModelUpdate,
    current_user = Depends(get_current_user),
    model_service: ModelService = Depends()
):
    """
    Cập nhật thông tin của một model
    
    Args:
        model_id: ID của model
        model: Thông tin cập nhật
        current_user: Người dùng hiện tại
        model_service: Service quản lý model
        
    Returns:
        ModelResponse: Thông tin model đã cập nhật
        
    Raises:
        HTTPException: Model không tồn tại hoặc lỗi validation
    """
    try:
        return await model_service.update_model(model_id, model)
    except ModelNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Model not found"
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{model_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_model(
    model_id: str,
    current_user = Depends(get_current_user),
    model_service: ModelService = Depends()
):
    """
    Xóa một model
    
    Args:
        model_id: ID của model
        current_user: Người dùng hiện tại
        model_service: Service quản lý model
        
    Raises:
        HTTPException: Model không tồn tại
    """
    try:
        await model_service.delete_model(model_id)
    except ModelNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Model not found"
        )

@router.get("/{model_id}/metrics", response_model=ModelMetrics)
async def get_model_metrics(
    model_id: str,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    current_user = Depends(get_current_user),
    model_service: ModelService = Depends()
):
    """
    Lấy metrics của một model
    
    Args:
        model_id: ID của model
        start_date: Ngày bắt đầu
        end_date: Ngày kết thúc
        current_user: Người dùng hiện tại
        model_service: Service quản lý model
        
    Returns:
        ModelMetrics: Metrics của model
        
    Raises:
        HTTPException: Model không tồn tại
    """
    try:
        return await model_service.get_model_metrics(
            model_id,
            start_date,
            end_date
        )
    except ModelNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Model not found"
        ) 
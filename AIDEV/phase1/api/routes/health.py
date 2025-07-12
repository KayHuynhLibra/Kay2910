from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...core.database import get_db
from ...core.monitoring import Monitoring
from ...config.settings import settings

router = APIRouter()

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": settings.VERSION,
        "debug": settings.DEBUG
    }

@router.get("/metrics")
async def metrics():
    return Monitoring.get_metrics() 
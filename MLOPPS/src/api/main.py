# Core imports
from fastapi import FastAPI, HTTPException  # Framework cho API và xử lý lỗi HTTP
from pydantic import BaseModel  # Validation và serialization cho request/response
import mlflow  # Quản lý model lifecycle và versioning
import logging  # Ghi log hệ thống
from typing import Dict, Any  # Type hints cho Python
import os  # Thao tác với hệ thống file

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,  # Level log: INFO
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Format log
)
logger = logging.getLogger(__name__)

# Khởi tạo FastAPI app
app = FastAPI(
    title="MLOps API",  # Tên API
    description="API for MLOps project",  # Mô tả API
    version="1.0.0"  # Phiên bản API
)

# Load model từ MLflow
MODEL_PATH = os.getenv("MODEL_PATH", "/app/models/production")  # Đường dẫn model
try:
    model = mlflow.pyfunc.load_model(MODEL_PATH)  # Load model từ MLflow
    logger.info(f"Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    model = None

# Định nghĩa cấu trúc request
class PredictionRequest(BaseModel):
    features: Dict[str, Any]  # Dictionary chứa features cho prediction

# Định nghĩa cấu trúc response
class PredictionResponse(BaseModel):
    prediction: float  # Giá trị dự đoán
    confidence: float  # Độ tin cậy của dự đoán

# Health check endpoint
@app.get("/health")
async def health_check():
    """Kiểm tra sức khỏe của API"""
    return {"status": "healthy"}

# Readiness check endpoint
@app.get("/ready")
async def readiness_check():
    """Kiểm tra readiness của API và model"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    return {"status": "ready"}

# Prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """Endpoint dự đoán sử dụng model đã load"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Thực hiện dự đoán
        prediction = model.predict(request.features)
        
        # Tính toán độ tin cậy (ví dụ)
        confidence = 0.95  # Nên được implement dựa trên model
        
        return PredictionResponse(
            prediction=float(prediction[0]),
            confidence=confidence
        )
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Model information endpoint
@app.get("/model/info")
async def model_info():
    """Lấy thông tin về model đang sử dụng"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    return {
        "model_type": type(model).__name__,
        "model_path": MODEL_PATH,
        "input_schema": model.metadata.get_input_schema(),
        "output_schema": model.metadata.get_output_schema()
    }

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Chạy server trên port 8000 
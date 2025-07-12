from fastapi import FastAPI, HTTPException, Depends, Security, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any, List, Optional
from datetime import datetime
import uvicorn
import psutil
import os
from ..security.rate_limiter import RateLimiter

from ..agents import ChatAgent, LearningAgent
from ..data import DataManager
from ..models import ModelManager
from ..security import SecurityManager
from ..monitoring.metrics import update_system_metrics

app = FastAPI(
    title="AI System API",
    description="API for AI System with chat, learning, and model management capabilities",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Initialize rate limiter
rate_limiter = RateLimiter(requests_per_minute=60, block_duration=300)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize managers
security_manager = SecurityManager({"security_dir": "security"})
data_manager = DataManager({"data_dir": "data"})
model_manager = ModelManager({"model_dir": "models"})
chat_agent = ChatAgent("chat_agent", {"max_history": 100})
learning_agent = LearningAgent("learning_agent", {"max_training_history": 100})

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Rate limiting middleware
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    allowed, reason = rate_limiter.is_allowed(client_ip)
    
    if not allowed:
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded. {reason}"
        )
    
    response = await call_next(request)
    return response

# Dependency for getting current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    if not security_manager.authorize(token, "read"):
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token

# Health check endpoints
@app.get("/health")
async def health_check():
    """Health check endpoint for liveness probe"""
    try:
        # Check if all managers are initialized
        if not all([security_manager, data_manager, model_manager, chat_agent, learning_agent]):
            raise HTTPException(status_code=503, detail="One or more components are not initialized")
        
        # Check system resources
        process = psutil.Process()
        memory_usage = process.memory_info().rss / 1024 / 1024  # Convert to MB
        cpu_usage = process.cpu_percent()
        
        if memory_usage > 900:  # 900MB threshold
            raise HTTPException(status_code=503, detail="High memory usage")
        if cpu_usage > 80:  # 80% threshold
            raise HTTPException(status_code=503, detail="High CPU usage")
        
        # Update system metrics
        update_system_metrics()
        
        return {
            "status": "healthy",
            "memory_usage_mb": memory_usage,
            "cpu_usage_percent": cpu_usage,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

@app.get("/ready")
async def readiness_check():
    """Readiness check endpoint for readiness probe"""
    try:
        # Check if all required directories exist
        required_dirs = ["data", "models", "security", "logs"]
        for dir_name in required_dirs:
            if not os.path.exists(dir_name):
                raise HTTPException(status_code=503, detail=f"Required directory {dir_name} does not exist")
        
        # Check if all managers are ready
        if not all([
            security_manager.is_ready(),
            data_manager.is_ready(),
            model_manager.is_ready(),
            chat_agent.is_ready(),
            learning_agent.is_ready()
        ]):
            raise HTTPException(status_code=503, detail="One or more components are not ready")
        
        return {
            "status": "ready",
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))

# Authentication endpoints
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = security_manager.authenticate(form_data.username, form_data.password)
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": token, "token_type": "bearer"}

# User management endpoints
@app.post("/users")
async def create_user(username: str, password: str, role: str = "user"):
    if security_manager.create_user(username, password, role):
        return {"message": "User created successfully"}
    raise HTTPException(status_code=400, detail="User already exists")

@app.put("/users/{username}")
async def update_user(username: str, updates: Dict[str, Any], token: str = Depends(get_current_user)):
    if security_manager.update_user(username, updates):
        return {"message": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{username}")
async def delete_user(username: str, token: str = Depends(get_current_user)):
    if security_manager.delete_user(username):
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

# Chat endpoints
@app.post("/chat")
async def chat(message: str, context: Optional[Dict[str, Any]] = None, token: str = Depends(get_current_user)):
    result = await chat_agent.process({"message": message, "context": context or {}})
    return result

@app.get("/chat/history")
async def get_chat_history(limit: Optional[int] = None, token: str = Depends(get_current_user)):
    return chat_agent.get_conversation_history(limit)

# Learning endpoints
@app.post("/learn/train")
async def train_model(
    model_name: str,
    data: Dict[str, Any],
    parameters: Optional[Dict[str, Any]] = None,
    token: str = Depends(get_current_user)
):
    result = await learning_agent.process({
        "action": "train",
        "model_name": model_name,
        "data": data,
        "parameters": parameters
    })
    return result

@app.post("/learn/evaluate")
async def evaluate_model(
    model_name: str,
    data: Dict[str, Any],
    token: str = Depends(get_current_user)
):
    result = await learning_agent.process({
        "action": "evaluate",
        "model_name": model_name,
        "data": data
    })
    return result

@app.post("/learn/predict")
async def predict(
    model_name: str,
    data: Dict[str, Any],
    token: str = Depends(get_current_user)
):
    result = await learning_agent.process({
        "action": "predict",
        "model_name": model_name,
        "data": data
    })
    return result

# Data management endpoints
@app.post("/data")
async def save_dataset(
    dataset_name: str,
    data: Dict[str, Any],
    version: Optional[str] = None,
    token: str = Depends(get_current_user)
):
    try:
        data_manager.save_dataset(dataset_name, data, version)
        return {"message": "Dataset saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/data/{dataset_name}")
async def get_dataset(
    dataset_name: str,
    version: Optional[str] = None,
    token: str = Depends(get_current_user)
):
    try:
        return data_manager.load_dataset(dataset_name, version)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/data")
async def list_datasets(token: str = Depends(get_current_user)):
    return data_manager.list_datasets()

# Model management endpoints
@app.post("/models")
async def save_model(
    model_name: str,
    model: Dict[str, Any],
    version: Optional[str] = None,
    token: str = Depends(get_current_user)
):
    try:
        model_manager.save_model(model_name, model, version)
        return {"message": "Model saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/models/{model_name}")
async def get_model(
    model_name: str,
    version: Optional[str] = None,
    token: str = Depends(get_current_user)
):
    try:
        return model_manager.get_model(model_name, version)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/models")
async def list_models(token: str = Depends(get_current_user)):
    return model_manager.list_models()

# Add rate limiter status endpoint
@app.get("/rate-limiter/status")
async def get_rate_limiter_status():
    return {
        "blocked_ips": rate_limiter.get_blocked_ips(),
        "requests_per_minute": rate_limiter.requests_per_minute,
        "block_duration": rate_limiter.block_duration
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 
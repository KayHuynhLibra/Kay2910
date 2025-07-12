import asyncio
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List
import uvicorn
from agents.coordinator import Coordinator
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

# Create FastAPI app
app = FastAPI(title="AI System API")

# Initialize coordinator
coordinator = Coordinator("main_coordinator", {
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    "max_memory_size": 1000,
    "max_history": 10
})

# Pydantic models
class AgentRequest(BaseModel):
    type: str
    agent_type: str = None
    agent_id: str = None
    config: Dict[str, Any] = {}
    data: Dict[str, Any] = {}

class SystemStatus(BaseModel):
    status: str
    agents: List[Dict[str, Any]]
    total_agents: int

# Startup event
@app.on_event("startup")
async def startup_event():
    await coordinator.start()
    logging.info("AI System started")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    await coordinator.stop()
    logging.info("AI System stopped")

# API endpoints
@app.post("/agents", response_model=Dict[str, Any])
async def handle_agent_request(request: AgentRequest):
    """Handle agent-related requests"""
    try:
        result = await coordinator.process(request.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/system/status", response_model=SystemStatus)
async def get_system_status():
    """Get system status"""
    try:
        status = coordinator.get_system_status()
        return SystemStatus(
            status="running",
            agents=[
                {
                    "agent_id": agent_id,
                    "type": agent.__class__.__name__,
                    "status": agent.get_status()
                }
                for agent_id, agent in coordinator.agents.items()
            ],
            total_agents=len(coordinator.agents)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to AI System API",
        "version": "1.0.0",
        "status": "running"
    }

if __name__ == "__main__":
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    
    # Run the application
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    ) 
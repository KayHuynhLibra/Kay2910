from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.monitoring import Monitoring
from .api.routes import auth, health
from .config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request timing middleware
app.middleware("http")(Monitoring.request_timing_middleware)

# Include routers
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])
app.include_router(health.router, prefix="/api/v1", tags=["health"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to AI System API",
        "version": settings.VERSION,
        "docs_url": "/docs"
    } 
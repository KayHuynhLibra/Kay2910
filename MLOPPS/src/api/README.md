# API Module

## Overview
The API module implements the REST API for the MLOps platform using FastAPI. It provides endpoints for model management, predictions, monitoring, and system administration.

## Directory Structure

### 1. Endpoints (`endpoints/`)
- `models.py`: Model management endpoints
- `predictions.py`: Prediction endpoints
- `monitoring.py`: Monitoring endpoints
- `admin.py`: Administration endpoints

### 2. Middleware (`middleware/`)
- `auth.py`: Authentication middleware
- `logging.py`: Request logging middleware
- `rate_limit.py`: Rate limiting middleware
- `error_handler.py`: Error handling middleware

### 3. Schemas (`schemas/`)
- `models.py`: Model-related Pydantic schemas
- `predictions.py`: Prediction-related schemas
- `monitoring.py`: Monitoring-related schemas
- `admin.py`: Administration-related schemas

### 4. Services (`services/`)
- `model_service.py`: Model management service
- `prediction_service.py`: Prediction service
- `monitoring_service.py`: Monitoring service
- `admin_service.py`: Administration service

### 5. Utils (`utils/`)
- `dependencies.py`: FastAPI dependencies
- `validators.py`: Input validators
- `response_models.py`: Response models
- `exceptions.py`: Custom exceptions

## API Documentation
The API documentation is available at `/docs` when running the server. It includes:
- OpenAPI specification
- Interactive API documentation
- Request/response examples
- Authentication requirements

## Authentication
The API uses JWT-based authentication with the following features:
- Token generation and validation
- Role-based access control
- Rate limiting per user
- Session management

## Error Handling
Standardized error responses with:
- HTTP status codes
- Error messages
- Error codes
- Stack traces (in development)

## Rate Limiting
- 100 requests per minute per API key
- Rate limit headers in responses
- Configurable limits per endpoint

## Testing
- Unit tests for each endpoint
- Integration tests for API flows
- Performance tests for critical endpoints
- Security tests for authentication

## Example Usage
```python
from fastapi import FastAPI, Depends
from api.middleware.auth import get_current_user
from api.schemas.models import ModelCreate
from api.services.model_service import ModelService

app = FastAPI()

@app.post("/models/")
async def create_model(
    model: ModelCreate,
    current_user = Depends(get_current_user),
    model_service: ModelService = Depends()
):
    return await model_service.create_model(model, current_user)
```

## Development Guidelines
1. Use type hints for all function parameters
2. Document all endpoints with docstrings
3. Implement proper error handling
4. Write unit tests for all endpoints
5. Follow REST API best practices
6. Use dependency injection for services
7. Implement proper logging
8. Add OpenAPI documentation 
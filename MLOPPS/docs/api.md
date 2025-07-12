# API Documentation

## Overview
MLOps API cung cấp các endpoints để quản lý và tương tác với các mô hình machine learning. API được xây dựng trên FastAPI và tuân thủ RESTful principles.

## Authentication
Tất cả các requests phải được xác thực bằng JWT token trong header:
```
Authorization: Bearer <token>
```

## Base URL
```
https://api.example.com/v1
```

## Endpoints

### Model Management

#### List Models
```http
GET /models
```
**Response**
```json
{
  "models": [
    {
      "id": "model-123",
      "name": "xgboost-classifier",
      "version": "1.0.0",
      "status": "active",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### Get Model Details
```http
GET /models/{model_id}
```
**Response**
```json
{
  "id": "model-123",
  "name": "xgboost-classifier",
  "version": "1.0.0",
  "status": "active",
  "metrics": {
    "accuracy": 0.95,
    "precision": 0.94,
    "recall": 0.93
  },
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-02T00:00:00Z"
}
```

#### Deploy Model
```http
POST /models/{model_id}/deploy
```
**Request Body**
```json
{
  "environment": "production",
  "resources": {
    "cpu": "1",
    "memory": "2Gi"
  }
}
```
**Response**
```json
{
  "deployment_id": "deploy-123",
  "status": "deploying",
  "created_at": "2024-01-01T00:00:00Z"
}
```

### Predictions

#### Make Prediction
```http
POST /predict
```
**Request Body**
```json
{
  "model_id": "model-123",
  "features": {
    "feature1": 0.5,
    "feature2": 0.3
  }
}
```
**Response**
```json
{
  "prediction": 0.8,
  "confidence": 0.95,
  "model_version": "1.0.0"
}
```

#### Batch Prediction
```http
POST /predict/batch
```
**Request Body**
```json
{
  "model_id": "model-123",
  "features": [
    {
      "feature1": 0.5,
      "feature2": 0.3
    },
    {
      "feature1": 0.7,
      "feature2": 0.4
    }
  ]
}
```
**Response**
```json
{
  "predictions": [
    {
      "prediction": 0.8,
      "confidence": 0.95
    },
    {
      "prediction": 0.6,
      "confidence": 0.90
    }
  ],
  "model_version": "1.0.0"
}
```

### Model Monitoring

#### Get Model Metrics
```http
GET /models/{model_id}/metrics
```
**Query Parameters**
- `start_time`: ISO 8601 timestamp
- `end_time`: ISO 8601 timestamp
- `metric_type`: accuracy, latency, etc.

**Response**
```json
{
  "metrics": [
    {
      "timestamp": "2024-01-01T00:00:00Z",
      "value": 0.95,
      "type": "accuracy"
    }
  ]
}
```

#### Get Model Drift
```http
GET /models/{model_id}/drift
```
**Response**
```json
{
  "drift_score": 0.15,
  "features": [
    {
      "name": "feature1",
      "drift_score": 0.2
    }
  ],
  "last_updated": "2024-01-01T00:00:00Z"
}
```

### Data Management

#### Upload Training Data
```http
POST /data/upload
```
**Request Body**
```json
{
  "dataset_name": "training-data",
  "data_type": "csv",
  "description": "Training dataset for model v1.0.0"
}
```
**Response**
```json
{
  "upload_id": "upload-123",
  "status": "uploading",
  "created_at": "2024-01-01T00:00:00Z"
}
```

#### Get Dataset Info
```http
GET /data/{dataset_id}
```
**Response**
```json
{
  "id": "dataset-123",
  "name": "training-data",
  "size": "1.5GB",
  "rows": 10000,
  "columns": [
    "feature1",
    "feature2"
  ],
  "created_at": "2024-01-01T00:00:00Z"
}
```

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid request parameters",
  "details": {
    "field": "feature1",
    "message": "Value must be between 0 and 1"
  }
}
```

### 401 Unauthorized
```json
{
  "error": "Authentication required",
  "message": "Invalid or expired token"
}
```

### 404 Not Found
```json
{
  "error": "Resource not found",
  "message": "Model with ID model-123 not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error",
  "message": "An unexpected error occurred"
}
```

## Rate Limiting
- 100 requests per minute per API key
- Rate limit headers included in response:
  - `X-RateLimit-Limit`
  - `X-RateLimit-Remaining`
  - `X-RateLimit-Reset`

## Versioning
API version được chỉ định trong URL path:
```
https://api.example.com/v1/...
```

## SDK Examples

### Python
```python
from mlops_client import MLOpsClient

client = MLOpsClient(api_key="your-api-key")

# Make prediction
prediction = client.predict(
    model_id="model-123",
    features={"feature1": 0.5, "feature2": 0.3}
)

# Get model metrics
metrics = client.get_model_metrics(
    model_id="model-123",
    start_time="2024-01-01T00:00:00Z",
    end_time="2024-01-02T00:00:00Z"
)
```

### JavaScript
```javascript
const mlops = new MLOpsClient('your-api-key');

// Make prediction
const prediction = await mlops.predict({
  modelId: 'model-123',
  features: { feature1: 0.5, feature2: 0.3 }
});

// Get model metrics
const metrics = await mlops.getModelMetrics({
  modelId: 'model-123',
  startTime: '2024-01-01T00:00:00Z',
  endTime: '2024-01-02T00:00:00Z'
});
``` 
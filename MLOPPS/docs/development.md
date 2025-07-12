# Development Guide

## Development Environment Setup

### Prerequisites
- Python 3.9+
- Git
- Docker
- IDE (VS Code, PyCharm, etc.)
- Virtual environment tool (venv, conda)

### Local Setup
1. Clone repository:
```bash
git clone https://github.com/your-org/mlops-project.git
cd mlops-project
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

4. Setup pre-commit hooks:
```bash
pre-commit install
```

### IDE Configuration

#### VS Code
1. Install extensions:
   - Python
   - Pylance
   - Python Test Explorer
   - Docker
   - Kubernetes

2. Settings (`settings.json`):
```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.testing.pytestEnabled": true
}
```

#### PyCharm
1. Enable:
   - Code inspection
   - Auto-imports
   - Code formatting
   - Git integration

2. Configure Python interpreter:
   - Use virtual environment
   - Install requirements

## Code Structure

### Project Layout
```
mlops-project/
├── src/
│   ├── api/
│   ├── data/
│   ├── models/
│   ├── monitoring/
│   └── utils/
├── tests/
├── configs/
├── deployment/
├── docs/
└── scripts/
```

### Key Components
1. **API Layer**
   - FastAPI endpoints
   - Request/response models
   - Authentication/authorization

2. **Data Layer**
   - Data ingestion
   - Data validation
   - Feature engineering
   - Data versioning

3. **Model Layer**
   - Model training
   - Model evaluation
   - Model registry
   - Model serving

4. **Monitoring Layer**
   - Metrics collection
   - Logging
   - Alerting
   - Dashboarding

## Development Workflow

### Branch Strategy
1. Main branches:
   - `main`: Production code
   - `develop`: Development code

2. Feature branches:
   - `feature/feature-name`
   - `bugfix/bug-name`
   - `hotfix/issue-name`

### Git Workflow
1. Create feature branch:
```bash
git checkout develop
git pull
git checkout -b feature/new-feature
```

2. Make changes:
```bash
git add .
git commit -m "feat: add new feature"
```

3. Push changes:
```bash
git push origin feature/new-feature
```

4. Create pull request:
   - Title: Clear description
   - Description: Detailed explanation
   - Reviewers: Team members
   - Labels: Appropriate tags

### Code Review Process
1. Self-review:
   - Run tests
   - Check linting
   - Verify documentation

2. Peer review:
   - Code quality
   - Test coverage
   - Documentation
   - Performance
   - Security

3. CI/CD checks:
   - Build
   - Tests
   - Linting
   - Security scan

## Testing

### Unit Tests
```python
# tests/test_model.py
def test_model_prediction():
    model = Model()
    prediction = model.predict([1, 2, 3])
    assert prediction > 0
```

### Integration Tests
```python
# tests/integration/test_api.py
def test_prediction_endpoint():
    response = client.post("/predict", json={"features": [1, 2, 3]})
    assert response.status_code == 200
```

### Test Coverage
```bash
pytest --cov=src tests/
coverage report
coverage html
```

## Code Quality

### Linting
```bash
# Run linters
flake8 src tests
black src tests
isort src tests
mypy src tests
```

### Type Hints
```python
from typing import List, Dict, Optional

def process_data(
    data: List[Dict[str, float]],
    threshold: Optional[float] = None
) -> Dict[str, float]:
    pass
```

### Documentation
```python
def train_model(
    data: pd.DataFrame,
    target: str,
    params: Dict[str, Any]
) -> Model:
    """Train machine learning model.

    Args:
        data: Training data
        target: Target variable
        params: Model parameters

    Returns:
        Trained model

    Raises:
        ValueError: If data is empty
    """
    pass
```

## Performance Optimization

### Profiling
```python
import cProfile
import pstats

def profile_function():
    profiler = cProfile.Profile()
    profiler.enable()
    # Your code here
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats()
```

### Memory Management
```python
import gc

def process_large_data():
    # Process data
    gc.collect()  # Force garbage collection
```

## Security Best Practices

### Input Validation
```python
from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    features: List[float] = Field(..., min_items=1, max_items=100)
    model_id: str = Field(..., min_length=1, max_length=50)
```

### Secure Configuration
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    database_url: str

    class Config:
        env_file = ".env"
```

## Deployment

### Local Development
```bash
# Run with Docker
docker-compose up

# Run with Kubernetes
kubectl apply -f deployment/kubernetes/dev/
```

### Testing Deployment
```bash
# Run integration tests
pytest tests/integration/

# Check API health
curl http://localhost:8000/health
```

## Troubleshooting

### Common Issues
1. **Dependency Issues**
   - Clear cache: `pip cache purge`
   - Reinstall: `pip install -r requirements.txt --no-cache-dir`

2. **Test Failures**
   - Check test data
   - Verify environment variables
   - Check test dependencies

3. **Performance Issues**
   - Profile code
   - Check resource usage
   - Optimize database queries

### Debugging
1. **Logging**
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")
```

2. **Debugger**
```python
import pdb

def complex_function():
    pdb.set_trace()  # Set breakpoint
    # Your code here
```

## Resources

### Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

### Tools
- [VS Code](https://code.visualstudio.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Postman](https://www.postman.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)

### Learning Resources
- [Python Best Practices](https://docs.python-guide.org/)
- [MLOps Best Practices](https://ml-ops.org/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/) 
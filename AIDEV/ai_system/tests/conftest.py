import pytest
import os
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Create logs directory if it doesn't exist
logs_dir = project_root / "logs"
logs_dir.mkdir(exist_ok=True)

@pytest.fixture(scope="session")
def test_data_dir():
    """Fixture to provide test data directory."""
    data_dir = project_root / "tests" / "test_data"
    data_dir.mkdir(exist_ok=True)
    return data_dir

@pytest.fixture(scope="session")
def test_config():
    """Fixture to provide test configuration."""
    return {
        "required_fields": ["test_field"],
        "cache_ttl": 3600,
        "log_level": "INFO",
        "max_memory_size": 1000
    }

@pytest.fixture(scope="session")
def test_logger():
    """Fixture to provide test logger."""
    import logging
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)
    
    # Create handlers
    file_handler = logging.FileHandler(logs_dir / "test.log")
    console_handler = logging.StreamHandler()
    
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger 
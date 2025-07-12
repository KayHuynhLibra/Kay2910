# Utils Module

## Overview
The Utils module provides common utilities and helper functions used across the MLOps platform. It includes configuration management, logging, validation, and other shared functionality.

## Directory Structure

### 1. Config (`config/`)
- `config_manager.py`: Configuration management
- `env_loader.py`: Environment variable loading
- `config_validator.py`: Configuration validation
- `config_loader.py`: Configuration loading

### 2. Logging (`logging/`)
- `logger.py`: Logging setup
- `log_formatter.py`: Log formatting
- `log_handler.py`: Log handlers
- `log_utils.py`: Logging utilities

### 3. Validation (`validation/`)
- `validator.py`: Input validation
- `schema_validator.py`: Schema validation
- `type_checker.py`: Type checking
- `constraint_validator.py`: Constraint validation

### 4. Security (`security/`)
- `encryption.py`: Encryption utilities
- `hashing.py`: Hashing functions
- `token.py`: Token management
- `permissions.py`: Permission checking

### 5. File (`file/`)
- `file_handler.py`: File operations
- `file_validator.py`: File validation
- `file_compression.py`: File compression
- `file_utils.py`: File utilities

### 6. Time (`time/`)
- `time_utils.py`: Time utilities
- `scheduler.py`: Task scheduling
- `timezone.py`: Timezone handling
- `date_utils.py`: Date utilities

### 7. Testing (`testing/`)
- `test_utils.py`: Testing utilities
- `mock_data.py`: Mock data generation
- `test_helpers.py`: Test helpers
- `assertions.py`: Custom assertions

## Common Utilities

### 1. Configuration Management
```python
from utils.config.config_manager import ConfigManager
from utils.config.env_loader import EnvLoader
from utils.config.config_validator import ConfigValidator

# Initialize components
config_manager = ConfigManager()
env_loader = EnvLoader()
config_validator = ConfigValidator()

# Load configuration
config = config_manager.load_config(
    config_path=config_path,
    env=environment
)

# Load environment variables
env_vars = env_loader.load_env(
    env_file=env_file
)

# Validate configuration
validation_result = config_validator.validate(
    config=config,
    schema=config_schema
)
```

### 2. Logging Setup
```python
from utils.logging.logger import Logger
from utils.logging.log_formatter import LogFormatter
from utils.logging.log_handler import LogHandler

# Initialize components
logger = Logger()
formatter = LogFormatter()
handler = LogHandler()

# Configure logging
logger.configure(
    level=log_level,
    format=log_format,
    handlers=log_handlers
)

# Create formatter
log_format = formatter.create_format(
    format_template=format_template
)

# Add handler
handler.add_handler(
    handler_type=handler_type,
    config=handler_config
)
```

### 3. Input Validation
```python
from utils.validation.validator import Validator
from utils.validation.schema_validator import SchemaValidator
from utils.validation.type_checker import TypeChecker

# Initialize components
validator = Validator()
schema_validator = SchemaValidator()
type_checker = TypeChecker()

# Validate input
validation_result = validator.validate(
    data=input_data,
    rules=validation_rules
)

# Validate schema
schema_result = schema_validator.validate(
    data=input_data,
    schema=data_schema
)

# Check types
type_result = type_checker.check_types(
    data=input_data,
    expected_types=type_spec
)
```

## Utility Features

### 1. Configuration
- Environment-based configuration
- Configuration validation
- Secure configuration storage
- Dynamic configuration updates

### 2. Logging
- Structured logging
- Log rotation
- Log levels
- Log formatting
- Log handlers

### 3. Validation
- Input validation
- Schema validation
- Type checking
- Constraint validation
- Custom validators

### 4. Security
- Encryption/decryption
- Hashing
- Token management
- Permission checking
- Security utilities

## Development Guidelines
1. Implement proper error handling
2. Use type hints for all functions
3. Write comprehensive tests
4. Document all public interfaces
5. Follow utility best practices
6. Implement proper logging
7. Use configuration management
8. Add performance monitoring

## Testing
- Unit tests for each utility
- Integration tests for components
- Performance tests for critical functions
- Load tests for file operations

## Example Configuration
```yaml
utils:
  config:
    environment: development
    config_path: configs/
    validation: strict
  logging:
    level: INFO
    format: json
    rotation: daily
    compression: true
  validation:
    strict: true
    type_checking: true
    schema_validation: true
  security:
    encryption: aes-256-gcm
    hashing: sha-256
    token_expiry: 3600
  file:
    max_size: 100MB
    allowed_types:
      - json
      - yaml
      - csv
    compression: true
  time:
    timezone: UTC
    date_format: ISO8601
    scheduler:
      max_jobs: 100
      interval: 60s
``` 
"""
Bài tập 19: Logging

Mục tiêu:
- Hiểu cách sử dụng logging
- Thực hành với logging module
- Sử dụng log handlers và formatters
"""

import logging
import logging.handlers
import json
from datetime import datetime
import os
import sys
from typing import Dict, Any

# TODO: Basic logging
def setup_basic_logging():
    """
    Setup basic logging
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

# TODO: File logging
def setup_file_logging(filename: str):
    """
    Setup file logging
    """
    logger = logging.getLogger('file_logger')
    logger.setLevel(logging.INFO)
    
    # Create file handler
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(file_handler)
    
    return logger

# TODO: Rotating file logging
def setup_rotating_file_logging(
    filename: str,
    max_bytes: int = 1024 * 1024,  # 1MB
    backup_count: int = 5
):
    """
    Setup rotating file logging
    """
    logger = logging.getLogger('rotating_file_logger')
    logger.setLevel(logging.INFO)
    
    # Create rotating file handler
    rotating_handler = logging.handlers.RotatingFileHandler(
        filename,
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    rotating_handler.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    rotating_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(rotating_handler)
    
    return logger

# TODO: JSON logging
class JSONFormatter(logging.Formatter):
    """
    JSON formatter for logging
    """
    def format(self, record: logging.LogRecord) -> str:
        """
        Format log record as JSON
        """
        log_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }
        
        # Add extra fields if present
        if hasattr(record, 'extra'):
            log_data.update(record.extra)
        
        return json.dumps(log_data)

def setup_json_logging(filename: str):
    """
    Setup JSON logging
    """
    logger = logging.getLogger('json_logger')
    logger.setLevel(logging.INFO)
    
    # Create file handler
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(logging.INFO)
    
    # Create JSON formatter
    json_formatter = JSONFormatter()
    file_handler.setFormatter(json_formatter)
    
    # Add handler to logger
    logger.addHandler(file_handler)
    
    return logger

# TODO: Custom logger
class CustomLogger:
    """
    Custom logger implementation
    """
    def __init__(self, name: str, log_file: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Create file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Create console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def info(self, message: str, **kwargs):
        """
        Log info message
        """
        self.logger.info(message, extra=kwargs)
    
    def error(self, message: str, **kwargs):
        """
        Log error message
        """
        self.logger.error(message, extra=kwargs)
    
    def warning(self, message: str, **kwargs):
        """
        Log warning message
        """
        self.logger.warning(message, extra=kwargs)
    
    def debug(self, message: str, **kwargs):
        """
        Log debug message
        """
        self.logger.debug(message, extra=kwargs)

# TODO: Logging decorator
def log_function_call(logger: logging.Logger):
    """
    Decorator to log function calls
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger.info(
                f"Calling function: {func.__name__}",
                extra={
                    'function': func.__name__,
                    'args': args,
                    'kwargs': kwargs
                }
            )
            try:
                result = func(*args, **kwargs)
                logger.info(
                    f"Function {func.__name__} completed successfully",
                    extra={'function': func.__name__}
                )
                return result
            except Exception as e:
                logger.error(
                    f"Function {func.__name__} failed",
                    extra={
                        'function': func.__name__,
                        'error': str(e)
                    }
                )
                raise
        return wrapper
    return decorator

# TODO: Logging context manager
class LoggingContext:
    """
    Context manager for logging
    """
    def __init__(self, logger: logging.Logger, level: int = logging.INFO):
        self.logger = logger
        self.level = level
        self.old_level = logger.level
    
    def __enter__(self):
        self.logger.setLevel(self.level)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.setLevel(self.old_level)
        if exc_type is not None:
            self.logger.error(
                f"Exception occurred: {exc_type.__name__}: {exc_val}",
                exc_info=True
            )

# TODO: Logging filter
class CustomFilter(logging.Filter):
    """
    Custom filter for logging
    """
    def __init__(self, level: int):
        super().__init__()
        self.level = level
    
    def filter(self, record: logging.LogRecord) -> bool:
        """
        Filter log records
        """
        return record.levelno >= self.level

# TODO: Logging handler
class CustomHandler(logging.Handler):
    """
    Custom handler for logging
    """
    def __init__(self, filename: str):
        super().__init__()
        self.filename = filename
    
    def emit(self, record: logging.LogRecord):
        """
        Emit log record
        """
        try:
            with open(self.filename, 'a') as f:
                f.write(self.format(record) + '\n')
        except Exception:
            self.handleError(record)

# TODO: Example usage
def example_usage():
    """
    Example usage of logging
    """
    # Setup basic logging
    setup_basic_logging()
    logger = logging.getLogger(__name__)
    
    # Log messages
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.debug("This is a debug message")
    
    # Setup file logging
    file_logger = setup_file_logging('app.log')
    file_logger.info("This is a file log message")
    
    # Setup rotating file logging
    rotating_logger = setup_rotating_file_logging('rotating.log')
    rotating_logger.info("This is a rotating file log message")
    
    # Setup JSON logging
    json_logger = setup_json_logging('json.log')
    json_logger.info("This is a JSON log message")
    
    # Use custom logger
    custom_logger = CustomLogger('custom', 'custom.log')
    custom_logger.info("This is a custom log message")
    
    # Use logging decorator
    @log_function_call(logger)
    def example_function():
        return "Example function result"
    
    example_function()
    
    # Use logging context manager
    with LoggingContext(logger):
        logger.info("This message is logged with custom level")
    
    # Use custom filter
    logger.addFilter(CustomFilter(logging.WARNING))
    logger.info("This message is filtered out")
    logger.warning("This message is logged")
    
    # Use custom handler
    custom_handler = CustomHandler('custom_handler.log')
    custom_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(custom_handler)
    logger.info("This message is handled by custom handler")

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tạo một hệ thống logging cho một ứng dụng FastAPI
2. Tạo một hệ thống logging cho một ứng dụng machine learning
3. Tạo một hệ thống logging cho một hệ thống microservices
4. Tạo một hệ thống logging cho một ứng dụng web với Nginx
5. Tạo một hệ thống logging cho một hệ thống database
""" 
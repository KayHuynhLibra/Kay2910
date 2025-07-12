"""
Bài tập 47: Debugging

Mục tiêu:
- Hiểu cách debug trong Python
- Thực hành với debugger và logging
- Sử dụng debugging tools
"""

import os
import sys
import time
import pytest
import unittest
import logging
import traceback
import pdb
import psutil
import numpy as np
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import json
import re
from functools import wraps
from contextlib import contextmanager

# TODO: Basic debugging
def basic_debugging():
    """
    Basic debugging example.
    """
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        print("Stack trace:")
        traceback.print_exc()
    
    return "Done"

# TODO: Debugger
def debugger():
    """
    Debugger example.
    """
    def complex_function():
        x = 1
        y = 2
        pdb.set_trace()  # Breakpoint
        z = x + y
        return z
    
    return complex_function()

# TODO: Logging
def logging_example():
    """
    Logging example.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('debug.log'),
            logging.StreamHandler()
        ]
    )
    
    # Create logger
    logger = logging.getLogger(__name__)
    
    # Log messages
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
    
    return "Done"

# TODO: Stack trace
def stack_trace():
    """
    Stack trace example.
    """
    def function_a():
        return function_b()
    
    def function_b():
        return function_c()
    
    def function_c():
        return traceback.extract_stack()
    
    return function_a()

# TODO: Exception handling
def exception_handling():
    """
    Exception handling example.
    """
    def risky_function():
        try:
            x = 1 / 0
        except ZeroDivisionError as e:
            print(f"Caught error: {e}")
        finally:
            print("Cleanup code")
    
    return risky_function()

# TODO: Debug decorator
def debug_decorator():
    """
    Debug decorator example.
    """
    def debug(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        return wrapper
    
    @debug
    def add(a, b):
        return a + b
    
    return add(1, 2)

# TODO: Debug context manager
def debug_context_manager():
    """
    Debug context manager example.
    """
    @contextmanager
    def debug_context():
        print("Entering context")
        try:
            yield
        except Exception as e:
            print(f"Caught error: {e}")
        finally:
            print("Exiting context")
    
    with debug_context():
        x = 1 / 0
    
    return "Done"

# TODO: Custom logging filter
def custom_logging_filter():
    """
    Custom logging filter example.
    """
    class DebugFilter(logging.Filter):
        def filter(self, record):
            return record.levelno == logging.DEBUG
    
    # Configure logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    
    # Add filter
    debug_filter = DebugFilter()
    logger.addFilter(debug_filter)
    
    # Log messages
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    
    return "Done"

# TODO: Custom logging handler
def custom_logging_handler():
    """
    Custom logging handler example.
    """
    class ConsoleHandler(logging.Handler):
        def emit(self, record):
            msg = self.format(record)
            print(f"Custom handler: {msg}")
    
    # Configure logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Add handler
    handler = ConsoleHandler()
    handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    logger.addHandler(handler)
    
    # Log messages
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    
    return "Done"

# TODO: Custom logging formatter
def custom_logging_formatter():
    """
    Custom logging formatter example.
    """
    class CustomFormatter(logging.Formatter):
        def format(self, record):
            record.custom_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return super().format(record)
    
    # Configure logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Add handler with custom formatter
    handler = logging.StreamHandler()
    formatter = CustomFormatter('%(custom_time)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    # Log messages
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    
    return "Done"

# TODO: Custom debug logger
def custom_debug_logger():
    """
    Custom debug logger example.
    """
    class DebugLogger:
        def __init__(self, name):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.DEBUG)
            
            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
            self.logger.addHandler(console_handler)
            
            # File handler
            file_handler = logging.FileHandler('debug.log')
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            self.logger.addHandler(file_handler)
        
        def debug(self, message):
            self.logger.debug(message)
        
        def info(self, message):
            self.logger.info(message)
        
        def warning(self, message):
            self.logger.warning(message)
        
        def error(self, message):
            self.logger.error(message)
    
    # Create logger
    logger = DebugLogger(__name__)
    
    # Log messages
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    
    return "Done"

# TODO: Example usage
def example_usage():
    """
    Example usage of debugging features.
    """
    # Basic debugging
    print("Basic debugging:")
    basic_debugging()
    
    # Debugger
    print("\nDebugger:")
    debugger()
    
    # Logging
    print("\nLogging:")
    logging_example()
    
    # Stack trace
    print("\nStack trace:")
    print(stack_trace())
    
    # Exception handling
    print("\nException handling:")
    exception_handling()
    
    # Debug decorator
    print("\nDebug decorator:")
    print(debug_decorator())
    
    # Debug context manager
    print("\nDebug context manager:")
    debug_context_manager()
    
    # Custom logging filter
    print("\nCustom logging filter:")
    custom_logging_filter()
    
    # Custom logging handler
    print("\nCustom logging handler:")
    custom_logging_handler()
    
    # Custom logging formatter
    print("\nCustom logging formatter:")
    custom_logging_formatter()
    
    # Custom debug logger
    print("\nCustom debug logger:")
    custom_debug_logger()

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tạo hệ thống debugging cho một ứng dụng FastAPI
2. Tạo hệ thống debugging cho một ứng dụng machine learning
3. Tạo hệ thống debugging cho một hệ thống microservices
4. Tạo hệ thống debugging cho một ứng dụng web với Nginx
5. Tạo hệ thống debugging cho một hệ thống database
""" 
"""
Bài tập 35: Debugging

Mục tiêu:
- Hiểu cách debug ứng dụng Python
- Thực hành với debuggers và logging
- Sử dụng debugging tools
"""

import os
import sys
import time
import pytest
import unittest
import pdb
import logging
import traceback
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
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return None
    
    result = divide(10, 0)
    return result

# TODO: Debugger
def debugger():
    """
    Debugger example.
    """
    def complex_function(a, b, c):
        pdb.set_trace()  # Set breakpoint
        result = a + b
        result *= c
        return result
    
    return complex_function(1, 2, 3)

# TODO: Logging
def logging_example():
    """
    Logging example.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger(__name__)
    
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
    
    return logger

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
    def risky_operation():
        try:
            result = 10 / 0
        except ZeroDivisionError as e:
            print(f"Caught exception: {e}")
            return None
        except Exception as e:
            print(f"Caught unexpected exception: {e}")
            return None
        else:
            print("No exception occurred")
            return result
        finally:
            print("Cleanup code executed")
    
    return risky_operation()

# TODO: Debug decorator
def debug_decorator():
    """
    Debug decorator example.
    """
    def debug(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            try:
                result = func(*args, **kwargs)
                print(f"{func.__name__} returned: {result}")
                return result
            except Exception as e:
                print(f"{func.__name__} raised: {e}")
                raise
        return wrapper
    
    @debug
    def add(a, b):
        return a + b
    
    return add(1, 2)

# TODO: Debug context
def debug_context():
    """
    Debug context example.
    """
    @contextmanager
    def debug_context():
        print("Entering debug context")
        try:
            yield
        except Exception as e:
            print(f"Caught exception in context: {e}")
            raise
        finally:
            print("Exiting debug context")
    
    with debug_context():
        result = 10 / 0
    
    return result

# TODO: Debug filter
def debug_filter():
    """
    Debug filter example.
    """
    class DebugFilter(logging.Filter):
        def filter(self, record):
            return record.levelno >= logging.DEBUG
    
    logger = logging.getLogger(__name__)
    logger.addFilter(DebugFilter())
    
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    
    return logger

# TODO: Debug handler
def debug_handler():
    """
    Debug handler example.
    """
    class DebugHandler(logging.Handler):
        def emit(self, record):
            try:
                msg = self.format(record)
                print(f"Debug: {msg}")
            except Exception:
                self.handleError(record)
    
    logger = logging.getLogger(__name__)
    handler = DebugHandler()
    logger.addHandler(handler)
    
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    
    return logger

# TODO: Debug formatter
def debug_formatter():
    """
    Debug formatter example.
    """
    class DebugFormatter(logging.Formatter):
        def format(self, record):
            record.msg = f"[DEBUG] {record.msg}"
            return super().format(record)
    
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = DebugFormatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    
    return logger

# TODO: Debug logger
def debug_logger():
    """
    Debug logger example.
    """
    class DebugLogger:
        def __init__(self, name):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.DEBUG)
            
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        
        def debug(self, message):
            self.logger.debug(message)
        
        def info(self, message):
            self.logger.info(message)
        
        def warning(self, message):
            self.logger.warning(message)
        
        def error(self, message):
            self.logger.error(message)
        
        def critical(self, message):
            self.logger.critical(message)
    
    logger = DebugLogger(__name__)
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    
    return logger

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
    debug_decorator()
    
    # Debug context
    print("\nDebug context:")
    try:
        debug_context()
    except Exception as e:
        print(f"Caught exception: {e}")
    
    # Debug filter
    print("\nDebug filter:")
    debug_filter()
    
    # Debug handler
    print("\nDebug handler:")
    debug_handler()
    
    # Debug formatter
    print("\nDebug formatter:")
    debug_formatter()
    
    # Debug logger
    print("\nDebug logger:")
    debug_logger()

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tạo debugging system cho một ứng dụng FastAPI
2. Tạo debugging system cho một ứng dụng machine learning
3. Tạo debugging system cho một hệ thống microservices
4. Tạo debugging system cho một ứng dụng web với Nginx
5. Tạo debugging system cho một hệ thống database
""" 
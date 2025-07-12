"""
Bài tập 29: Debugging

Mục tiêu:
- Hiểu cách debug ứng dụng Python
- Thực hành với debugger và logging
- Sử dụng debugging tools
"""

import os
import sys
import time
import logging
import pdb
import traceback
import inspect
import linecache
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import json
import re

# TODO: Basic debugging
def basic_debugging():
    """
    Basic debugging example.
    """
    def divide(a: int, b: int) -> float:
        return a / b
    
    try:
        result = divide(10, 0)
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
        pdb.set_trace()

# TODO: Logging
def logging_example():
    """
    Logging example.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='debug.log'
    )
    
    def process_data(data: List[int]) -> List[int]:
        logging.debug(f"Processing data: {data}")
        try:
            result = [x * 2 for x in data]
            logging.info(f"Processed data: {result}")
            return result
        except Exception as e:
            logging.error(f"Error processing data: {e}")
            raise
    
    return process_data([1, 2, 3])

# TODO: Debugger
def debugger_example():
    """
    Debugger example.
    """
    def complex_function(a: int, b: int) -> int:
        pdb.set_trace()
        result = 0
        for i in range(a):
            result += i
            if i > b:
                break
        return result
    
    return complex_function(10, 5)

# TODO: Stack trace
def stack_trace_example():
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
    def process_item(item: Any) -> Any:
        try:
            return item * 2
        except TypeError:
            print("Type error occurred")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    return {
        'valid': process_item(5),
        'invalid': process_item("string")
    }

# TODO: Debug decorator
def debug_decorator():
    """
    Debug decorator example.
    """
    def debug(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            try:
                result = func(*args, **kwargs)
                print(f"{func.__name__} returned: {result}")
                return result
            except Exception as e:
                print(f"Error in {func.__name__}: {e}")
                raise
        return wrapper
    
    @debug
    def add(a: int, b: int) -> int:
        return a + b
    
    return add(5, 3)

# TODO: Debug context manager
def debug_context():
    """
    Debug context manager example.
    """
    class DebugContext:
        def __init__(self, name: str):
            self.name = name
        
        def __enter__(self):
            print(f"Entering {self.name}")
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type:
                print(f"Error in {self.name}: {exc_val}")
            print(f"Exiting {self.name}")
    
    with DebugContext("test"):
        print("Inside context")
        raise ValueError("Test error")

# TODO: Debug filter
def debug_filter():
    """
    Debug filter example.
    """
    class DebugFilter(logging.Filter):
        def filter(self, record):
            return record.levelno >= logging.DEBUG
    
    logger = logging.getLogger("debug")
    logger.addFilter(DebugFilter())
    logger.setLevel(logging.DEBUG)
    
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

# TODO: Debug handler
def debug_handler():
    """
    Debug handler example.
    """
    class DebugHandler(logging.Handler):
        def emit(self, record):
            try:
                msg = self.format(record)
                print(f"DEBUG: {msg}")
            except Exception:
                self.handleError(record)
    
    logger = logging.getLogger("debug")
    handler = DebugHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    
    logger.debug("Debug message")

# TODO: Debug formatter
def debug_formatter():
    """
    Debug formatter example.
    """
    class DebugFormatter(logging.Formatter):
        def format(self, record):
            record.filename = os.path.basename(record.filename)
            record.funcName = record.funcName
            record.lineno = record.lineno
            return super().format(record)
    
    logger = logging.getLogger("debug")
    handler = logging.StreamHandler()
    formatter = DebugFormatter('%(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    
    logger.debug("Debug message")

# TODO: Debug logger
def debug_logger():
    """
    Debug logger example.
    """
    class DebugLogger:
        def __init__(self, name: str):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.DEBUG)
            
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        
        def debug(self, message: str):
            self.logger.debug(message)
        
        def info(self, message: str):
            self.logger.info(message)
        
        def warning(self, message: str):
            self.logger.warning(message)
        
        def error(self, message: str):
            self.logger.error(message)
        
        def critical(self, message: str):
            self.logger.critical(message)
    
    logger = DebugLogger("debug")
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

# TODO: Example usage
def example_usage():
    """
    Example usage of debugging features.
    """
    # Basic debugging
    print("Basic debugging:")
    basic_debugging()
    
    # Logging
    print("\nLogging:")
    logging_example()
    
    # Debugger
    print("\nDebugger:")
    debugger_example()
    
    # Stack trace
    print("\nStack trace:")
    print(stack_trace_example())
    
    # Exception handling
    print("\nException handling:")
    print(exception_handling())
    
    # Debug decorator
    print("\nDebug decorator:")
    print(debug_decorator())
    
    # Debug context
    print("\nDebug context:")
    try:
        debug_context()
    except ValueError as e:
        print(f"Caught error: {e}")
    
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
"""
Bài tập 49: Documentation

Mục tiêu:
- Hiểu cách viết documentation trong Python
- Thực hành với docstrings và comments
- Sử dụng documentation tools
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

# TODO: Basic docstring
def basic_docstring():
    """
    Basic docstring example.
    """
    return "Done"

# TODO: Function docstring
def function_docstring(a: int, b: int) -> int:
    """
    Add two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Sum of a and b
    
    Raises:
        TypeError: If a or b is not an integer
    
    Examples:
        >>> function_docstring(1, 2)
        3
        >>> function_docstring(-1, 1)
        0
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Arguments must be integers")
    return a + b

# TODO: Class docstring
class ClassDocstring:
    """
    A class with a docstring.
    
    Attributes:
        name (str): Name of the instance
        value (int): Value of the instance
    
    Methods:
        get_name(): Get the name
        get_value(): Get the value
        set_value(value): Set the value
    """
    
    def __init__(self, name: str, value: int):
        """
        Initialize the class.
        
        Args:
            name (str): Name of the instance
            value (int): Value of the instance
        """
        self.name = name
        self.value = value
    
    def get_name(self) -> str:
        """
        Get the name.
        
        Returns:
            str: Name of the instance
        """
        return self.name
    
    def get_value(self) -> int:
        """
        Get the value.
        
        Returns:
            int: Value of the instance
        """
        return self.value
    
    def set_value(self, value: int) -> None:
        """
        Set the value.
        
        Args:
            value (int): New value
        
        Raises:
            ValueError: If value is negative
        """
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.value = value

# TODO: Type hints
def type_hints(a: int, b: float, c: str, d: List[int], e: Dict[str, int], f: Optional[int] = None) -> Tuple[int, float, str]:
    """
    Function with type hints.
    
    Args:
        a (int): Integer parameter
        b (float): Float parameter
        c (str): String parameter
        d (List[int]): List of integers
        e (Dict[str, int]): Dictionary of string to integer
        f (Optional[int], optional): Optional integer parameter. Defaults to None.
    
    Returns:
        Tuple[int, float, str]: Tuple of integer, float, and string
    """
    return a, b, c

# TODO: Examples
def examples():
    """
    Function with examples.
    
    Examples:
        >>> examples()
        'Done'
        
        >>> examples()
        'Done'
    """
    return "Done"

# TODO: Exceptions
def exceptions():
    """
    Function with exceptions.
    
    Raises:
        ValueError: If input is invalid
        TypeError: If input is wrong type
        RuntimeError: If something goes wrong
    """
    raise ValueError("Invalid input")

# TODO: Return values
def return_values() -> str:
    """
    Function with return value.
    
    Returns:
        str: A string value
    """
    return "Done"

# TODO: Arguments
def arguments(a: int, b: int = 0, *args: int, **kwargs: int) -> int:
    """
    Function with arguments.
    
    Args:
        a (int): Required argument
        b (int, optional): Optional argument. Defaults to 0.
        *args (int): Variable number of arguments
        **kwargs (int): Keyword arguments
    
    Returns:
        int: Sum of all arguments
    """
    return a + b + sum(args) + sum(kwargs.values())

# TODO: Attributes
class Attributes:
    """
    Class with attributes.
    
    Attributes:
        name (str): Name of the instance
        value (int): Value of the instance
        items (List[str]): List of items
    """
    
    def __init__(self, name: str, value: int, items: List[str]):
        self.name = name
        self.value = value
        self.items = items

# TODO: References
def references():
    """
    Function with references.
    
    References:
        [1] Python Documentation, https://docs.python.org/
        [2] PEP 257, https://www.python.org/dev/peps/pep-0257/
    """
    return "Done"

# TODO: Notes
def notes():
    """
    Function with notes.
    
    Notes:
        This function is used for demonstration purposes.
        It doesn't do anything useful.
    """
    return "Done"

# TODO: Warnings
def warnings():
    """
    Function with warnings.
    
    Warnings:
        This function is deprecated.
        Use new_function() instead.
    """
    return "Done"

# TODO: Example usage
def example_usage():
    """
    Example usage of documentation features.
    """
    # Basic docstring
    print("Basic docstring:")
    print(basic_docstring.__doc__)
    
    # Function docstring
    print("\nFunction docstring:")
    print(function_docstring.__doc__)
    
    # Class docstring
    print("\nClass docstring:")
    print(ClassDocstring.__doc__)
    
    # Type hints
    print("\nType hints:")
    print(type_hints.__annotations__)
    
    # Examples
    print("\nExamples:")
    print(examples.__doc__)
    
    # Exceptions
    print("\nExceptions:")
    print(exceptions.__doc__)
    
    # Return values
    print("\nReturn values:")
    print(return_values.__doc__)
    
    # Arguments
    print("\nArguments:")
    print(arguments.__doc__)
    
    # Attributes
    print("\nAttributes:")
    print(Attributes.__doc__)
    
    # References
    print("\nReferences:")
    print(references.__doc__)
    
    # Notes
    print("\nNotes:")
    print(notes.__doc__)
    
    # Warnings
    print("\nWarnings:")
    print(warnings.__doc__)

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tạo documentation cho một ứng dụng FastAPI
2. Tạo documentation cho một ứng dụng machine learning
3. Tạo documentation cho một hệ thống microservices
4. Tạo documentation cho một ứng dụng web với Nginx
5. Tạo documentation cho một hệ thống database
""" 
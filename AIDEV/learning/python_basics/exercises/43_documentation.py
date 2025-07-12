"""
Bài tập 43: Documentation

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
    
    This is a simple function that demonstrates
    how to write a basic docstring.
    """
    return "Basic docstring"

# TODO: Function docstring
def function_docstring(a: int, b: int) -> int:
    """
    Function docstring example.
    
    This function demonstrates how to write a
    detailed function docstring with parameters
    and return value.
    
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
    Class docstring example.
    
    This class demonstrates how to write a
    detailed class docstring with attributes
    and methods.
    
    Attributes:
        name (str): Name of the instance
        value (int): Value of the instance
    
    Examples:
        >>> instance = ClassDocstring("test", 42)
        >>> instance.name
        'test'
        >>> instance.value
        42
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
        Get the name of the instance.
        
        Returns:
            str: Name of the instance
        """
        return self.name
    
    def get_value(self) -> int:
        """
        Get the value of the instance.
        
        Returns:
            int: Value of the instance
        """
        return self.value

# TODO: Type hints
def type_hints(a: int, b: float, c: str, d: List[int], e: Dict[str, int]) -> Tuple[int, float, str]:
    """
    Type hints example.
    
    This function demonstrates how to use type
    hints in Python.
    
    Args:
        a (int): Integer parameter
        b (float): Float parameter
        c (str): String parameter
        d (List[int]): List of integers
        e (Dict[str, int]): Dictionary of strings to integers
    
    Returns:
        Tuple[int, float, str]: Tuple of return values
    """
    return a, b, c

# TODO: Examples
def examples():
    """
    Examples in docstring.
    
    This function demonstrates how to include
    examples in docstrings.
    
    Examples:
        >>> examples()
        'Examples'
        
        >>> examples()
        'Examples'
    """
    return "Examples"

# TODO: Exceptions
def exceptions():
    """
    Exceptions in docstring.
    
    This function demonstrates how to document
    exceptions in docstrings.
    
    Raises:
        ValueError: If the input is invalid
        TypeError: If the input is of wrong type
        RuntimeError: If an error occurs during execution
    """
    raise ValueError("Invalid input")

# TODO: Return values
def return_values() -> str:
    """
    Return values in docstring.
    
    This function demonstrates how to document
    return values in docstrings.
    
    Returns:
        str: A string describing the return value
    """
    return "Return value"

# TODO: Arguments
def arguments(a: int, b: int, c: Optional[int] = None) -> int:
    """
    Arguments in docstring.
    
    This function demonstrates how to document
    arguments in docstrings.
    
    Args:
        a (int): First required argument
        b (int): Second required argument
        c (Optional[int], optional): Optional argument. Defaults to None.
    
    Returns:
        int: Sum of arguments
    """
    if c is None:
        return a + b
    return a + b + c

# TODO: Attributes
class Attributes:
    """
    Attributes in docstring.
    
    This class demonstrates how to document
    attributes in docstrings.
    
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
    References in docstring.
    
    This function demonstrates how to include
    references in docstrings.
    
    See Also:
        :func:`basic_docstring`
        :class:`ClassDocstring`
        :meth:`ClassDocstring.get_name`
    
    References:
        [1] Python Documentation, https://docs.python.org/
        [2] PEP 257, https://www.python.org/dev/peps/pep-0257/
    """
    return "References"

# TODO: Notes
def notes():
    """
    Notes in docstring.
    
    This function demonstrates how to include
    notes in docstrings.
    
    Notes:
        This is a note about the function.
        It can span multiple lines.
        
        It can also include code examples:
        
        >>> notes()
        'Notes'
    """
    return "Notes"

# TODO: Warnings
def warnings():
    """
    Warnings in docstring.
    
    This function demonstrates how to include
    warnings in docstrings.
    
    Warning:
        This function is deprecated.
        Use :func:`new_function` instead.
    
    .. deprecated:: 1.0
        Use :func:`new_function` instead.
    """
    return "Warnings"

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
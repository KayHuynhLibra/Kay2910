"""
Bài tập 31: Documentation

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

# TODO: Basic docstring
def basic_docstring():
    """
    Basic docstring example.
    
    This function demonstrates how to write a basic docstring.
    
    Returns:
        None
    """
    pass

# TODO: Function docstring
def function_docstring(a: int, b: int) -> int:
    """
    Function docstring example.
    
    This function adds two numbers together.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: Sum of a and b
    
    Raises:
        ValueError: If a or b is not an integer
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Arguments must be integers")
    return a + b

# TODO: Class docstring
class ClassDocstring:
    """
    Class docstring example.
    
    This class demonstrates how to write a class docstring.
    
    Attributes:
        name (str): Name of the class
        value (int): Value of the class
    """
    
    def __init__(self, name: str, value: int):
        """
        Initialize the class.
        
        Args:
            name (str): Name of the class
            value (int): Value of the class
        """
        self.name = name
        self.value = value
    
    def method(self) -> str:
        """
        Method docstring example.
        
        This method returns a string representation of the class.
        
        Returns:
            str: String representation of the class
        """
        return f"{self.name}: {self.value}"

# TODO: Module docstring
"""
Module docstring example.

This module demonstrates how to write a module docstring.
It includes examples of function, class, and method docstrings.
"""

# TODO: Type hints
def type_hints(a: int, b: float) -> str:
    """
    Type hints example.
    
    Args:
        a (int): Integer parameter
        b (float): Float parameter
    
    Returns:
        str: String result
    """
    return f"{a} + {b} = {a + b}"

# TODO: Examples
def examples():
    """
    Examples in docstring.
    
    This function demonstrates how to include examples in docstrings.
    
    Examples:
        >>> examples()
        'This is an example'
    """
    return "This is an example"

# TODO: Raises
def raises():
    """
    Raises in docstring.
    
    This function demonstrates how to document exceptions.
    
    Raises:
        ValueError: If the input is invalid
        TypeError: If the input is of wrong type
    """
    raise ValueError("Invalid input")

# TODO: Returns
def returns() -> int:
    """
    Returns in docstring.
    
    This function demonstrates how to document return values.
    
    Returns:
        int: The result of the calculation
    """
    return 42

# TODO: Args
def args(a: int, b: int, c: Optional[int] = None) -> int:
    """
    Args in docstring.
    
    This function demonstrates how to document arguments.
    
    Args:
        a (int): First argument
        b (int): Second argument
        c (Optional[int], optional): Third argument. Defaults to None.
    
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
    
    This class demonstrates how to document attributes.
    
    Attributes:
        name (str): Name of the object
        value (int): Value of the object
        items (List[str]): List of items
    """
    
    def __init__(self, name: str, value: int, items: List[str]):
        self.name = name
        self.value = value
        self.items = items

# TODO: See also
def see_also():
    """
    See also in docstring.
    
    This function demonstrates how to include references to other functions.
    
    See Also:
        function_docstring: For a similar function
        ClassDocstring: For a related class
    """
    pass

# TODO: Notes
def notes():
    """
    Notes in docstring.
    
    This function demonstrates how to include notes in docstrings.
    
    Notes:
        This is a note about the function.
        It can span multiple lines.
    """
    pass

# TODO: Warnings
def warnings():
    """
    Warnings in docstring.
    
    This function demonstrates how to include warnings in docstrings.
    
    Warnings:
        This function is deprecated.
        Use function_docstring instead.
    """
    pass

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
    
    # Module docstring
    print("\nModule docstring:")
    print(__doc__)
    
    # Type hints
    print("\nType hints:")
    print(type_hints.__annotations__)
    
    # Examples
    print("\nExamples:")
    print(examples.__doc__)
    
    # Raises
    print("\nRaises:")
    print(raises.__doc__)
    
    # Returns
    print("\nReturns:")
    print(returns.__doc__)
    
    # Args
    print("\nArgs:")
    print(args.__doc__)
    
    # Attributes
    print("\nAttributes:")
    print(Attributes.__doc__)
    
    # See also
    print("\nSee also:")
    print(see_also.__doc__)
    
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
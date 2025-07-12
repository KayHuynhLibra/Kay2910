"""
Bài tập 25: Documentation

Mục tiêu:
- Hiểu cách viết documentation trong Python
- Thực hành với docstrings và comments
- Sử dụng documentation tools
"""

import os
import sys
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import json
import re

# TODO: Basic docstring
def basic_function(param1: str, param2: int) -> str:
    """
    A basic function with docstring.

    Args:
        param1 (str): First parameter description.
        param2 (int): Second parameter description.

    Returns:
        str: Return value description.

    Raises:
        ValueError: If param2 is negative.

    Examples:
        >>> basic_function("test", 1)
        'test1'
    """
    if param2 < 0:
        raise ValueError("param2 must be positive")
    return f"{param1}{param2}"

# TODO: Class docstring
class ExampleClass:
    """
    A class with docstring.

    This class demonstrates how to write class documentation.

    Attributes:
        name (str): The name of the instance.
        value (int): The value of the instance.

    Examples:
        >>> instance = ExampleClass("test", 1)
        >>> instance.name
        'test'
    """
    
    def __init__(self, name: str, value: int):
        """
        Initialize the class.

        Args:
            name (str): The name to set.
            value (int): The value to set.
        """
        self.name = name
        self.value = value
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get information about the instance.

        Returns:
            Dict[str, Any]: A dictionary containing instance information.

        Examples:
            >>> instance = ExampleClass("test", 1)
            >>> instance.get_info()
            {'name': 'test', 'value': 1}
        """
        return {
            "name": self.name,
            "value": self.value
        }

# TODO: Module docstring
"""
This module demonstrates documentation in Python.

It includes examples of:
- Function documentation
- Class documentation
- Module documentation
- Type hints
- Examples
- Raises
- Returns
- Args
- Attributes
"""

# TODO: Type hints
def type_hints_example(
    param1: str,
    param2: int,
    param3: List[str],
    param4: Optional[Dict[str, Any]] = None
) -> Tuple[str, int]:
    """
    Function with type hints.

    Args:
        param1 (str): First parameter.
        param2 (int): Second parameter.
        param3 (List[str]): Third parameter.
        param4 (Optional[Dict[str, Any]], optional): Fourth parameter. Defaults to None.

    Returns:
        Tuple[str, int]: A tuple containing param1 and param2.
    """
    return param1, param2

# TODO: Examples
def examples_function(x: int, y: int) -> int:
    """
    Function with examples.

    Args:
        x (int): First number.
        y (int): Second number.

    Returns:
        int: The sum of x and y.

    Examples:
        >>> examples_function(1, 2)
        3
        >>> examples_function(-1, 1)
        0
        >>> examples_function(0, 0)
        0
    """
    return x + y

# TODO: Raises
def raises_function(value: int) -> int:
    """
    Function with raises documentation.

    Args:
        value (int): The value to process.

    Returns:
        int: The processed value.

    Raises:
        ValueError: If value is negative.
        TypeError: If value is not an integer.
    """
    if not isinstance(value, int):
        raise TypeError("value must be an integer")
    if value < 0:
        raise ValueError("value must be positive")
    return value * 2

# TODO: Returns
def returns_function(data: List[int]) -> Dict[str, Any]:
    """
    Function with returns documentation.

    Args:
        data (List[int]): List of integers.

    Returns:
        Dict[str, Any]: A dictionary containing:
            - sum: The sum of all numbers
            - average: The average of all numbers
            - count: The number of elements
    """
    return {
        "sum": sum(data),
        "average": sum(data) / len(data) if data else 0,
        "count": len(data)
    }

# TODO: Args
def args_function(
    required: str,
    optional: int = 0,
    *args: str,
    **kwargs: Any
) -> str:
    """
    Function with args documentation.

    Args:
        required (str): Required parameter.
        optional (int, optional): Optional parameter. Defaults to 0.
        *args (str): Variable length argument list.
        **kwargs (Any): Arbitrary keyword arguments.

    Returns:
        str: A string containing all arguments.
    """
    return f"{required}{optional}{args}{kwargs}"

# TODO: Attributes
class AttributesClass:
    """
    Class with attributes documentation.

    Attributes:
        public_attr (str): Public attribute.
        _protected_attr (int): Protected attribute.
        __private_attr (float): Private attribute.
    """
    
    def __init__(self):
        self.public_attr = "public"
        self._protected_attr = 1
        self.__private_attr = 1.0

# TODO: See also
def see_also_function():
    """
    Function with see also documentation.

    See also:
        :func:`basic_function`
        :class:`ExampleClass`
        :mod:`documentation`
    """
    pass

# TODO: Notes
def notes_function():
    """
    Function with notes documentation.

    Notes:
        This is a note about the function.
        It can span multiple lines.
        It can contain important information.
    """
    pass

# TODO: Warnings
def warnings_function():
    """
    Function with warnings documentation.

    Warning:
        This function is deprecated.
        Use :func:`new_function` instead.
    """
    pass

# TODO: Example usage
def example_usage():
    """
    Example usage of documentation features.
    """
    # Basic function
    result = basic_function("test", 1)
    print(f"Basic function result: {result}")
    
    # Class
    instance = ExampleClass("test", 1)
    info = instance.get_info()
    print(f"Class info: {info}")
    
    # Type hints
    result = type_hints_example("test", 1, ["a", "b"])
    print(f"Type hints result: {result}")
    
    # Examples
    result = examples_function(1, 2)
    print(f"Examples result: {result}")
    
    # Raises
    try:
        result = raises_function(-1)
    except ValueError as e:
        print(f"Raises error: {e}")
    
    # Returns
    result = returns_function([1, 2, 3])
    print(f"Returns result: {result}")
    
    # Args
    result = args_function("test", 1, "a", "b", key="value")
    print(f"Args result: {result}")
    
    # Attributes
    instance = AttributesClass()
    print(f"Attributes: {instance.public_attr}")

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
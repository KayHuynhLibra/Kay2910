"""
Bài tập 30: Testing

Mục tiêu:
- Hiểu cách viết tests trong Python
- Thực hành với pytest và unittest
- Sử dụng testing tools
"""

import os
import sys
import time
import pytest
import unittest
from unittest.mock import Mock, patch
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import json
import re

# TODO: Basic test
def basic_test():
    """
    Basic test example.
    """
    def add(a: int, b: int) -> int:
        return a + b
    
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# TODO: Test class
class TestCalculator(unittest.TestCase):
    """
    Test class example.
    """
    def setUp(self):
        self.calculator = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2), 3)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(0, 0), 0)
    
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(3, 2), 1)
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertEqual(self.calculator.subtract(0, 0), 0)
    
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(0, 0), 0)
    
    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calculator.divide(1, 0)

# TODO: Test fixture
@pytest.fixture
def calculator():
    return Calculator()

def test_calculator_add(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_calculator_subtract(calculator):
    assert calculator.subtract(3, 2) == 1
    assert calculator.subtract(1, 1) == 0
    assert calculator.subtract(0, 0) == 0

def test_calculator_multiply(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(0, 0) == 0

def test_calculator_divide(calculator):
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        calculator.divide(1, 0)

# TODO: Test mock
def test_mock():
    """
    Test mock example.
    """
    mock = Mock()
    mock.method.return_value = 42
    assert mock.method() == 42
    mock.method.assert_called_once()

# TODO: Test patch
def test_patch():
    """
    Test patch example.
    """
    with patch('builtins.print') as mock_print:
        print('test')
        mock_print.assert_called_once_with('test')

# TODO: Test parametrize
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected

# TODO: Test skip
@pytest.mark.skip(reason="Not implemented yet")
def test_skip():
    assert False

# TODO: Test xfail
@pytest.mark.xfail
def test_xfail():
    assert False

# TODO: Test timeout
@pytest.mark.timeout(1)
def test_timeout():
    time.sleep(2)

# TODO: Test coverage
def test_coverage():
    """
    Test coverage example.
    """
    def function(a: int, b: int) -> int:
        if a > b:
            return a
        return b
    
    assert function(1, 2) == 2
    assert function(2, 1) == 2

# TODO: Test async
@pytest.mark.asyncio
async def test_async():
    """
    Test async example.
    """
    async def async_function():
        return 42
    
    assert await async_function() == 42

# TODO: Test context
def test_context():
    """
    Test context example.
    """
    class TestContext:
        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
    
    with TestContext() as context:
        assert context is not None

# TODO: Test exception
def test_exception():
    """
    Test exception example.
    """
    def function():
        raise ValueError("test")
    
    with pytest.raises(ValueError) as excinfo:
        function()
    assert str(excinfo.value) == "test"

# TODO: Test setup/teardown
class TestSetupTeardown(unittest.TestCase):
    def setUp(self):
        self.data = []
    
    def tearDown(self):
        self.data = None
    
    def test_setup_teardown(self):
        self.data.append(1)
        assert len(self.data) == 1

# TODO: Example usage
def example_usage():
    """
    Example usage of testing features.
    """
    # Basic test
    print("Basic test:")
    basic_test()
    
    # Test class
    print("\nTest class:")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    # Test fixture
    print("\nTest fixture:")
    pytest.main(['-v'])
    
    # Test mock
    print("\nTest mock:")
    test_mock()
    
    # Test patch
    print("\nTest patch:")
    test_patch()
    
    # Test parametrize
    print("\nTest parametrize:")
    pytest.main(['-v'])
    
    # Test skip
    print("\nTest skip:")
    pytest.main(['-v'])
    
    # Test xfail
    print("\nTest xfail:")
    pytest.main(['-v'])
    
    # Test timeout
    print("\nTest timeout:")
    pytest.main(['-v'])
    
    # Test coverage
    print("\nTest coverage:")
    test_coverage()
    
    # Test async
    print("\nTest async:")
    pytest.main(['-v'])
    
    # Test context
    print("\nTest context:")
    test_context()
    
    # Test exception
    print("\nTest exception:")
    test_exception()
    
    # Test setup/teardown
    print("\nTest setup/teardown:")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tạo test suite cho một ứng dụng FastAPI
2. Tạo test suite cho một ứng dụng machine learning
3. Tạo test suite cho một hệ thống microservices
4. Tạo test suite cho một ứng dụng web với Nginx
5. Tạo test suite cho một hệ thống database
""" 
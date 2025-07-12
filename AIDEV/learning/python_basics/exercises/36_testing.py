"""
Bài tập 36: Testing

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
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import json
import re
from functools import wraps
from contextlib import contextmanager

# TODO: Basic tests
def test_basic():
    """
    Basic test example.
    """
    def add(a, b):
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
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(1, 0)

# TODO: Test fixtures
@pytest.fixture
def calculator():
    """
    Calculator fixture.
    """
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
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)

# TODO: Test mocks
def test_mock():
    """
    Mock test example.
    """
    from unittest.mock import Mock, patch
    
    mock = Mock()
    mock.method.return_value = 42
    
    assert mock.method() == 42
    mock.method.assert_called_once()
    
    with patch('builtins.print') as mock_print:
        print('Hello, World!')
        mock_print.assert_called_once_with('Hello, World!')

# TODO: Test parametrization
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# TODO: Test skipping
@pytest.mark.skip(reason="Not implemented yet")
def test_skip():
    assert False

# TODO: Test expected failure
@pytest.mark.xfail
def test_expected_failure():
    assert False

# TODO: Test timeout
@pytest.mark.timeout(1)
def test_timeout():
    time.sleep(2)

# TODO: Test coverage
def test_coverage():
    """
    Coverage test example.
    """
    def function(a, b):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return 0
    
    assert function(2, 1) == 2
    assert function(1, 2) == 2
    assert function(1, 1) == 0

# TODO: Test async
@pytest.mark.asyncio
async def test_async():
    """
    Async test example.
    """
    async def async_function():
        return 42
    
    result = await async_function()
    assert result == 42

# TODO: Test context
def test_context():
    """
    Context test example.
    """
    @contextmanager
    def test_context():
        print("Entering context")
        try:
            yield
        finally:
            print("Exiting context")
    
    with test_context():
        print("Inside context")

# TODO: Test exception
def test_exception():
    """
    Exception test example.
    """
    def function():
        raise ValueError("Test exception")
    
    with pytest.raises(ValueError) as excinfo:
        function()
    assert str(excinfo.value) == "Test exception"

# TODO: Test setup/teardown
class TestSetupTeardown(unittest.TestCase):
    """
    Setup/teardown test example.
    """
    def setUp(self):
        print("Setting up test")
    
    def tearDown(self):
        print("Tearing down test")
    
    def test_something(self):
        print("Running test")
        assert True

# TODO: Example usage
def example_usage():
    """
    Example usage of testing features.
    """
    # Basic tests
    print("Running basic tests...")
    test_basic()
    
    # Test class
    print("\nRunning test class...")
    unittest.main(argv=[''], exit=False)
    
    # Test fixtures
    print("\nRunning test fixtures...")
    pytest.main(['-v'])
    
    # Test mocks
    print("\nRunning test mocks...")
    test_mock()
    
    # Test parametrization
    print("\nRunning test parametrization...")
    test_add_parametrized(1, 2, 3)
    
    # Test skipping
    print("\nRunning test skipping...")
    test_skip()
    
    # Test expected failure
    print("\nRunning test expected failure...")
    test_expected_failure()
    
    # Test timeout
    print("\nRunning test timeout...")
    try:
        test_timeout()
    except Exception as e:
        print(f"Timeout test failed: {e}")
    
    # Test coverage
    print("\nRunning test coverage...")
    test_coverage()
    
    # Test async
    print("\nRunning test async...")
    import asyncio
    asyncio.run(test_async())
    
    # Test context
    print("\nRunning test context...")
    test_context()
    
    # Test exception
    print("\nRunning test exception...")
    test_exception()
    
    # Test setup/teardown
    print("\nRunning test setup/teardown...")
    unittest.main(argv=[''], exit=False)

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
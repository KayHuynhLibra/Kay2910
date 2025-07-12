"""
Bài tập 42: Testing

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
from unittest.mock import Mock, patch, MagicMock

# TODO: Basic tests
def basic_tests():
    """
    Basic tests example.
    """
    def add(a, b):
        return a + b
    
    # Test function
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
    return "Basic tests passed"

# TODO: Test class
class TestCalculator(unittest.TestCase):
    """
    Test class example.
    """
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 0), 0)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 1), 0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)

# TODO: Test fixtures
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
    assert calculator.divide(0, 1) == 0
    with pytest.raises(ZeroDivisionError):
        calculator.divide(1, 0)

# TODO: Test mocks
def test_mocks():
    """
    Test mocks example.
    """
    # Create mock
    mock = Mock()
    mock.method.return_value = 42
    
    # Test mock
    assert mock.method() == 42
    mock.method.assert_called_once()
    
    # Test mock with arguments
    mock.method(1, 2, 3)
    mock.method.assert_called_with(1, 2, 3)
    
    # Test mock with patch
    with patch('builtins.print') as mock_print:
        print('Hello, World!')
        mock_print.assert_called_with('Hello, World!')
    
    return "Mock tests passed"

# TODO: Test parameterization
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_parameterized(a, b, expected):
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
    assert True

# TODO: Test coverage
def test_coverage():
    """
    Test coverage example.
    """
    def function_to_test():
        if True:
            return True
        return False
    
    assert function_to_test() is True

# TODO: Test async
@pytest.mark.asyncio
async def test_async():
    async def async_function():
        return 42
    
    assert await async_function() == 42

# TODO: Test context manager
def test_context_manager():
    """
    Test context manager example.
    """
    @contextmanager
    def test_context():
        print("Setup")
        yield
        print("Teardown")
    
    with test_context():
        print("Test")

# TODO: Test exceptions
def test_exceptions():
    """
    Test exceptions example.
    """
    def function_that_raises():
        raise ValueError("Test exception")
    
    with pytest.raises(ValueError) as exc_info:
        function_that_raises()
    
    assert str(exc_info.value) == "Test exception"

# TODO: Test setup/teardown
class TestSetupTeardown(unittest.TestCase):
    def setUp(self):
        print("Setup")
    
    def tearDown(self):
        print("Teardown")
    
    def test_something(self):
        print("Test")
        assert True

# TODO: Example usage
def example_usage():
    """
    Example usage of testing features.
    """
    # Basic tests
    print("Basic tests:")
    print(basic_tests())
    
    # Test class
    print("\nTest class:")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    # Test fixtures
    print("\nTest fixtures:")
    pytest.main(['-v'])
    
    # Test mocks
    print("\nTest mocks:")
    print(test_mocks())
    
    # Test parameterization
    print("\nTest parameterization:")
    pytest.main(['-v', 'test_add_parameterized'])
    
    # Test skipping
    print("\nTest skipping:")
    pytest.main(['-v', 'test_skip'])
    
    # Test expected failure
    print("\nTest expected failure:")
    pytest.main(['-v', 'test_expected_failure'])
    
    # Test timeout
    print("\nTest timeout:")
    pytest.main(['-v', 'test_timeout'])
    
    # Test coverage
    print("\nTest coverage:")
    pytest.main(['--cov=.', 'test_coverage'])
    
    # Test async
    print("\nTest async:")
    pytest.main(['-v', 'test_async'])
    
    # Test context manager
    print("\nTest context manager:")
    test_context_manager()
    
    # Test exceptions
    print("\nTest exceptions:")
    test_exceptions()
    
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
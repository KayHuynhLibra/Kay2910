"""
Bài tập 48: Testing

Mục tiêu:
- Hiểu cách viết test trong Python
- Thực hành với unittest và pytest
- Sử dụng testing tools
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
from unittest.mock import Mock, patch, MagicMock

# TODO: Basic tests
def basic_tests():
    """
    Basic tests example.
    """
    def add(a, b):
        return a + b
    
    # Assertions
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
    return "All tests passed"

# TODO: Test class
def test_class():
    """
    Test class example.
    """
    class Calculator:
        def add(self, a, b):
            return a + b
        
        def subtract(self, a, b):
            return a - b
        
        def multiply(self, a, b):
            return a * b
        
        def divide(self, a, b):
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
    
    class TestCalculator(unittest.TestCase):
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
    
    # Run tests
    unittest.main(argv=[''], exit=False)
    
    return "All tests passed"

# TODO: Test fixtures
def test_fixtures():
    """
    Test fixtures example.
    """
    @pytest.fixture
    def calculator():
        class Calculator:
            def add(self, a, b):
                return a + b
        return Calculator()
    
    def test_add(calculator):
        assert calculator.add(1, 2) == 3
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0
    
    return "All tests passed"

# TODO: Test mocks
def test_mocks():
    """
    Test mocks example.
    """
    class Database:
        def get_data(self):
            return "Real data"
    
    def process_data(db):
        data = db.get_data()
        return f"Processed: {data}"
    
    # Create mock
    mock_db = Mock(spec=Database)
    mock_db.get_data.return_value = "Mock data"
    
    # Test with mock
    result = process_data(mock_db)
    assert result == "Processed: Mock data"
    mock_db.get_data.assert_called_once()
    
    return "All tests passed"

# TODO: Test parameterization
def test_parameterization():
    """
    Test parameterization example.
    """
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
    ])
    def test_add(a, b, expected):
        assert a + b == expected
    
    return "All tests passed"

# TODO: Test skipping
def test_skipping():
    """
    Test skipping example.
    """
    @pytest.mark.skip(reason="Not implemented yet")
    def test_future_feature():
        assert False
    
    return "All tests passed"

# TODO: Test expected failure
def test_expected_failure():
    """
    Test expected failure example.
    """
    @pytest.mark.xfail
    def test_broken_feature():
        assert False
    
    return "All tests passed"

# TODO: Test timeout
def test_timeout():
    """
    Test timeout example.
    """
    @pytest.mark.timeout(1)
    def test_slow_function():
        time.sleep(2)
        assert True
    
    return "All tests passed"

# TODO: Test coverage
def test_coverage():
    """
    Test coverage example.
    """
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    
    # Test all functions
    assert add(1, 2) == 3
    assert subtract(3, 2) == 1
    assert multiply(2, 3) == 6
    assert divide(6, 2) == 3
    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass
    
    return "All tests passed"

# TODO: Test async
def test_async():
    """
    Test async example.
    """
    import asyncio
    
    async def async_add(a, b):
        await asyncio.sleep(0.1)
        return a + b
    
    async def test_async_add():
        result = await async_add(1, 2)
        assert result == 3
    
    asyncio.run(test_async_add())
    
    return "All tests passed"

# TODO: Test context manager
def test_context_manager():
    """
    Test context manager example.
    """
    @contextmanager
    def temp_file():
        filename = "temp.txt"
        with open(filename, "w") as f:
            f.write("test")
        try:
            yield filename
        finally:
            os.remove(filename)
    
    with temp_file() as filename:
        assert os.path.exists(filename)
        with open(filename) as f:
            assert f.read() == "test"
    
    assert not os.path.exists(filename)
    
    return "All tests passed"

# TODO: Test exceptions
def test_exceptions():
    """
    Test exceptions example.
    """
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    
    # Test normal case
    assert divide(6, 2) == 3
    
    # Test exception
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(1, 0)
    assert str(excinfo.value) == "Cannot divide by zero"
    
    return "All tests passed"

# TODO: Test setup/teardown
def test_setup_teardown():
    """
    Test setup/teardown example.
    """
    class TestExample(unittest.TestCase):
        def setUp(self):
            self.data = [1, 2, 3]
        
        def tearDown(self):
            self.data = None
        
        def test_data(self):
            self.assertEqual(self.data, [1, 2, 3])
    
    # Run tests
    unittest.main(argv=[''], exit=False)
    
    return "All tests passed"

# TODO: Example usage
def example_usage():
    """
    Example usage of testing features.
    """
    # Basic tests
    print("Basic tests:")
    basic_tests()
    
    # Test class
    print("\nTest class:")
    test_class()
    
    # Test fixtures
    print("\nTest fixtures:")
    test_fixtures()
    
    # Test mocks
    print("\nTest mocks:")
    test_mocks()
    
    # Test parameterization
    print("\nTest parameterization:")
    test_parameterization()
    
    # Test skipping
    print("\nTest skipping:")
    test_skipping()
    
    # Test expected failure
    print("\nTest expected failure:")
    test_expected_failure()
    
    # Test timeout
    print("\nTest timeout:")
    test_timeout()
    
    # Test coverage
    print("\nTest coverage:")
    test_coverage()
    
    # Test async
    print("\nTest async:")
    test_async()
    
    # Test context manager
    print("\nTest context manager:")
    test_context_manager()
    
    # Test exceptions
    print("\nTest exceptions:")
    test_exceptions()
    
    # Test setup/teardown
    print("\nTest setup/teardown:")
    test_setup_teardown()

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
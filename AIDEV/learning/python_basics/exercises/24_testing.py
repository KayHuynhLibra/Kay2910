"""
Bài tập 24: Testing

Mục tiêu:
- Hiểu cách viết unit tests trong Python
- Thực hành với pytest
- Sử dụng mocking và fixtures
"""

import pytest
import unittest
from unittest.mock import Mock, patch, MagicMock
from typing import Any, Dict, List, Optional
import json
from datetime import datetime
import asyncio

# TODO: Basic unit tests
def test_basic_math():
    """
    Basic math operations test
    """
    assert 1 + 1 == 2
    assert 2 * 2 == 4
    assert 10 / 2 == 5
    assert 10 % 3 == 1

def test_string_operations():
    """
    String operations test
    """
    assert "hello" + " world" == "hello world"
    assert "hello".upper() == "HELLO"
    assert "HELLO".lower() == "hello"
    assert "hello world".split() == ["hello", "world"]

# TODO: Test with fixtures
@pytest.fixture
def sample_data():
    """
    Sample data fixture
    """
    return {
        "name": "John",
        "age": 30,
        "email": "john@example.com"
    }

def test_user_data(sample_data):
    """
    Test user data
    """
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30
    assert sample_data["email"] == "john@example.com"

# TODO: Test with mocking
class UserService:
    """
    User service for testing
    """
    def __init__(self, database):
        self.database = database
    
    def get_user(self, user_id: int) -> Dict[str, Any]:
        """
        Get user from database
        """
        return self.database.get_user(user_id)
    
    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create user in database
        """
        return self.database.create_user(user_data)

def test_user_service():
    """
    Test user service with mocking
    """
    # Create mock database
    mock_db = Mock()
    mock_db.get_user.return_value = {"id": 1, "name": "John"}
    mock_db.create_user.return_value = {"id": 2, "name": "Jane"}
    
    # Create service with mock database
    service = UserService(mock_db)
    
    # Test get_user
    user = service.get_user(1)
    assert user["name"] == "John"
    mock_db.get_user.assert_called_once_with(1)
    
    # Test create_user
    new_user = service.create_user({"name": "Jane"})
    assert new_user["name"] == "Jane"
    mock_db.create_user.assert_called_once_with({"name": "Jane"})

# TODO: Test with parametrize
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25)
])
def test_square(input: int, expected: int):
    """
    Test square function with parameters
    """
    assert input * input == expected

# TODO: Test with async
async def async_function():
    """
    Async function for testing
    """
    await asyncio.sleep(0.1)
    return "async result"

@pytest.mark.asyncio
async def test_async_function():
    """
    Test async function
    """
    result = await async_function()
    assert result == "async result"

# TODO: Test with context manager
class TestContext:
    """
    Context manager for testing
    """
    def __init__(self):
        self.value = 0
    
    def __enter__(self):
        self.value = 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.value = 0

def test_context_manager():
    """
    Test context manager
    """
    context = TestContext()
    assert context.value == 0
    
    with context:
        assert context.value == 1
    
    assert context.value == 0

# TODO: Test with exception
def test_exception():
    """
    Test exception handling
    """
    with pytest.raises(ValueError):
        raise ValueError("Test exception")

# TODO: Test with patch
def test_patch():
    """
    Test with patch
    """
    with patch('json.dumps') as mock_dumps:
        mock_dumps.return_value = '{"test": "value"}'
        result = json.dumps({"test": "value"})
        assert result == '{"test": "value"}'
        mock_dumps.assert_called_once_with({"test": "value"})

# TODO: Test with setup and teardown
class TestSetupTeardown:
    """
    Test class with setup and teardown
    """
    def setup_method(self):
        """
        Setup before each test
        """
        self.value = 0
    
    def teardown_method(self):
        """
        Teardown after each test
        """
        self.value = None
    
    def test_value(self):
        """
        Test value
        """
        assert self.value == 0
        self.value = 1
        assert self.value == 1

# TODO: Test with skip
@pytest.mark.skip(reason="This test is not implemented yet")
def test_skipped():
    """
    Skipped test
    """
    assert False

# TODO: Test with expected failure
@pytest.mark.xfail
def test_expected_to_fail():
    """
    Test that is expected to fail
    """
    assert False

# TODO: Test with timeout
@pytest.mark.timeout(1)
def test_timeout():
    """
    Test with timeout
    """
    import time
    time.sleep(2)

# TODO: Test with coverage
def test_coverage():
    """
    Test with coverage
    """
    def function_to_test():
        if True:
            return "true"
        return "false"
    
    assert function_to_test() == "true"

# TODO: Example usage
def example_usage():
    """
    Example usage of testing
    """
    # Run all tests
    pytest.main([__file__])

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tạo một bộ test cho một ứng dụng FastAPI
2. Tạo một bộ test cho một ứng dụng machine learning
3. Tạo một bộ test cho một hệ thống microservices
4. Tạo một bộ test cho một ứng dụng web với Nginx
5. Tạo một bộ test cho một hệ thống database
""" 
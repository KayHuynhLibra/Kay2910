"""
Bài tập 18: Testing

Mục tiêu:
- Hiểu cách viết unit tests
- Thực hành với pytest
- Sử dụng mocking và fixtures
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import json
from datetime import datetime
import asyncio
from typing import List, Dict, Any

# TODO: Basic test
def test_basic_math():
    """
    Test basic math operations
    """
    assert 1 + 1 == 2
    assert 2 * 3 == 6
    assert 10 / 2 == 5
    assert 2 ** 3 == 8

# TODO: Test with fixtures
@pytest.fixture
def sample_data():
    """
    Sample data fixture
    """
    return {
        "name": "Test User",
        "age": 25,
        "email": "test@example.com"
    }

def test_user_data(sample_data):
    """
    Test user data
    """
    assert sample_data["name"] == "Test User"
    assert sample_data["age"] == 25
    assert "@" in sample_data["email"]

# TODO: Test with mocking
class UserService:
    def __init__(self, db):
        self.db = db
    
    def get_user(self, user_id):
        return self.db.query(f"SELECT * FROM users WHERE id = {user_id}")

def test_user_service():
    """
    Test user service with mock database
    """
    # Create mock database
    mock_db = Mock()
    mock_db.query.return_value = {"id": 1, "name": "Test User"}
    
    # Create service with mock database
    service = UserService(mock_db)
    
    # Test get_user
    user = service.get_user(1)
    assert user["name"] == "Test User"
    mock_db.query.assert_called_once_with("SELECT * FROM users WHERE id = 1")

# TODO: Test with parametrize
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25)
])
def test_square(input, expected):
    """
    Test square function with multiple inputs
    """
    assert input ** 2 == expected

# TODO: Test with async
async def async_function():
    await asyncio.sleep(0.1)
    return "done"

@pytest.mark.asyncio
async def test_async_function():
    """
    Test async function
    """
    result = await async_function()
    assert result == "done"

# TODO: Test with context manager
class TestContext:
    def __init__(self):
        self.data = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.data.clear()

def test_context_manager():
    """
    Test context manager
    """
    with TestContext() as ctx:
        ctx.data.append(1)
        assert len(ctx.data) == 1
    assert len(ctx.data) == 0

# TODO: Test with exception
def test_exception():
    """
    Test exception handling
    """
    with pytest.raises(ValueError):
        raise ValueError("Test error")

# TODO: Test with patch
@patch('json.dumps')
def test_json_dumps(mock_dumps):
    """
    Test with patch
    """
    mock_dumps.return_value = '{"test": true}'
    result = json.dumps({"test": True})
    assert result == '{"test": true}'
    mock_dumps.assert_called_once_with({"test": True})

# TODO: Test with setup and teardown
@pytest.fixture(autouse=True)
def setup_and_teardown():
    """
    Setup and teardown for each test
    """
    # Setup
    print("\nSetting up test")
    yield
    # Teardown
    print("\nTearing down test")

# TODO: Test with skip and xfail
@pytest.mark.skip(reason="Not implemented yet")
def test_skipped():
    """
    Test that is skipped
    """
    assert False

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
            return True
        return False
    
    assert function_to_test() is True

# TODO: Test with async context manager
class AsyncTestContext:
    def __init__(self):
        self.data = []
    
    async def __aenter__(self):
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.sleep(0.1)
        self.data.clear()

@pytest.mark.asyncio
async def test_async_context_manager():
    """
    Test async context manager
    """
    async with AsyncTestContext() as ctx:
        ctx.data.append(1)
        assert len(ctx.data) == 1
    assert len(ctx.data) == 0

# TODO: Test with async mock
class AsyncService:
    async def get_data(self):
        await asyncio.sleep(0.1)
        return {"data": "test"}

@pytest.mark.asyncio
async def test_async_service():
    """
    Test async service with mock
    """
    service = AsyncService()
    with patch.object(service, 'get_data', return_value={"data": "mocked"}):
        result = await service.get_data()
        assert result["data"] == "mocked"

# TODO: Test with async fixture
@pytest.fixture
async def async_data():
    """
    Async data fixture
    """
    await asyncio.sleep(0.1)
    return {"async": "data"}

@pytest.mark.asyncio
async def test_async_fixture(async_data):
    """
    Test with async fixture
    """
    assert async_data["async"] == "data"

# TODO: Test with async parametrize
@pytest.mark.asyncio
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6)
])
async def test_async_parametrize(input, expected):
    """
    Test async function with multiple inputs
    """
    await asyncio.sleep(0.1)
    assert input * 2 == expected

# TODO: Test with async error handling
@pytest.mark.asyncio
async def test_async_error_handling():
    """
    Test async error handling
    """
    with pytest.raises(ValueError):
        await asyncio.sleep(0.1)
        raise ValueError("Async error")

# TODO: Test with async timeout
@pytest.mark.asyncio
@pytest.mark.timeout(1)
async def test_async_timeout():
    """
    Test async function with timeout
    """
    await asyncio.sleep(2)

# TODO: Test with async coverage
@pytest.mark.asyncio
async def test_async_coverage():
    """
    Test async function with coverage
    """
    async def async_function_to_test():
        if True:
            return True
        return False
    
    assert await async_function_to_test() is True

# TODO: Example usage
def test_example():
    """
    Example test
    """
    # Basic test
    assert 1 + 1 == 2
    
    # Test with fixture
    data = sample_data()
    assert data["name"] == "Test User"
    
    # Test with mock
    mock = Mock()
    mock.method.return_value = 42
    assert mock.method() == 42
    
    # Test with patch
    with patch('json.dumps') as mock_dumps:
        mock_dumps.return_value = '{"test": true}'
        assert json.dumps({"test": True}) == '{"test": true}'
    
    # Test with context manager
    with TestContext() as ctx:
        ctx.data.append(1)
        assert len(ctx.data) == 1
    
    # Test with exception
    with pytest.raises(ValueError):
        raise ValueError("Test error")

"""
Bài tập về nhà:
1. Tạo một bộ test cho một ứng dụng FastAPI
2. Tạo một bộ test cho một ứng dụng machine learning
3. Tạo một bộ test cho một hệ thống microservices
4. Tạo một bộ test cho một ứng dụng web với Nginx
5. Tạo một bộ test cho một hệ thống database
""" 
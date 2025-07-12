"""
Bài tập 13: Testing

Mục tiêu:
- Hiểu cách viết unit tests
- Thực hành với pytest
- Sử dụng mocking và fixtures
"""

import pytest
from unittest.mock import Mock, patch
import json
from datetime import datetime

# TODO: Unit test cơ bản
def test_basic_math():
    """
    Test các phép tính cơ bản
    """
    assert 1 + 1 == 2
    assert 2 * 3 == 6
    assert 10 / 2 == 5
    assert 2 ** 3 == 8

# TODO: Test với fixtures
@pytest.fixture
def sample_data():
    """
    Fixture cung cấp dữ liệu mẫu
    """
    return {
        "name": "Test User",
        "age": 25,
        "email": "test@example.com"
    }

def test_user_data(sample_data):
    """
    Test dữ liệu người dùng
    """
    assert sample_data["name"] == "Test User"
    assert sample_data["age"] == 25
    assert "@" in sample_data["email"]

# TODO: Test với mocking
class UserService:
    def __init__(self, db):
        self.db = db
    
    def get_user(self, user_id):
        return self.db.query(f"SELECT * FROM users WHERE id = {user_id}")

def test_user_service():
    """
    Test UserService với mock database
    """
    # Tạo mock database
    mock_db = Mock()
    mock_db.query.return_value = {"id": 1, "name": "Test User"}
    
    # Tạo service với mock database
    service = UserService(mock_db)
    
    # Test get_user
    user = service.get_user(1)
    assert user["name"] == "Test User"
    mock_db.query.assert_called_once_with("SELECT * FROM users WHERE id = 1")

# TODO: Test với parametrize
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25)
])
def test_square(input, expected):
    """
    Test hàm bình phương với nhiều input
    """
    assert input ** 2 == expected

# TODO: Test với async
import asyncio

async def async_function():
    await asyncio.sleep(0.1)
    return "done"

@pytest.mark.asyncio
async def test_async_function():
    """
    Test hàm bất đồng bộ
    """
    result = await async_function()
    assert result == "done"

# TODO: Test với context manager
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

# TODO: Test với exception
def test_exception():
    """
    Test xử lý exception
    """
    with pytest.raises(ValueError):
        raise ValueError("Test error")

# TODO: Test với patch
@patch('json.dumps')
def test_json_dumps(mock_dumps):
    """
    Test với patch
    """
    mock_dumps.return_value = '{"test": true}'
    result = json.dumps({"test": True})
    assert result == '{"test": true}'
    mock_dumps.assert_called_once_with({"test": True})

# TODO: Test với setup và teardown
@pytest.fixture(autouse=True)
def setup_and_teardown():
    """
    Setup và teardown cho mỗi test
    """
    # Setup
    print("\nSetting up test")
    yield
    # Teardown
    print("\nTearing down test")

# TODO: Test với skip và xfail
@pytest.mark.skip(reason="Not implemented yet")
def test_skipped():
    """
    Test bị skip
    """
    assert False

@pytest.mark.xfail
def test_expected_to_fail():
    """
    Test được đánh dấu là sẽ fail
    """
    assert False

# TODO: Test với timeout
@pytest.mark.timeout(1)
def test_timeout():
    """
    Test với timeout
    """
    import time
    time.sleep(2)

# TODO: Test với coverage
def test_coverage():
    """
    Test với coverage
    """
    def function_to_test():
        if True:
            return True
        return False
    
    assert function_to_test() is True

"""
Bài tập về nhà:
1. Tạo một bộ test cho một ứng dụng FastAPI
2. Tạo một bộ test cho một ứng dụng machine learning
3. Tạo một bộ test cho một hệ thống microservices
4. Tạo một bộ test cho một ứng dụng web với Nginx
5. Tạo một bộ test cho một hệ thống database
""" 
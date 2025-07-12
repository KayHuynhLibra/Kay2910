"""
Bài tập 8: Testing

Mục tiêu:
- Hiểu cách viết test trong Python
- Thực hành với unittest và pytest
- Sử dụng mock và fixture
"""

import unittest
from unittest.mock import Mock, patch
import pytest
from datetime import datetime

# TODO: Class cần test
class Calculator:
    """
    Class máy tính đơn giản
    """
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Không thể chia cho 0")
        return a / b

# TODO: Test với unittest
class TestCalculator(unittest.TestCase):
    """
    Test class Calculator sử dụng unittest
    """
    def setUp(self):
        """
        Chuẩn bị trước mỗi test
        """
        self.calc = Calculator()
    
    def test_add(self):
        """
        Test phép cộng
        """
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_subtract(self):
        """
        Test phép trừ
        """
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
    
    def test_multiply(self):
        """
        Test phép nhân
        """
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
    
    def test_divide(self):
        """
        Test phép chia
        """
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

# TODO: Test với pytest
@pytest.fixture
def calculator():
    """
    Fixture tạo instance Calculator
    """
    return Calculator()

def test_add(calculator):
    """
    Test phép cộng với pytest
    """
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2

def test_subtract(calculator):
    """
    Test phép trừ với pytest
    """
    assert calculator.subtract(3, 2) == 1
    assert calculator.subtract(1, 1) == 0
    assert calculator.subtract(-1, -1) == 0

def test_multiply(calculator):
    """
    Test phép nhân với pytest
    """
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(-2, -3) == 6

def test_divide(calculator):
    """
    Test phép chia với pytest
    """
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(5, 2) == 2.5
    assert calculator.divide(-6, 2) == -3
    
    with pytest.raises(ValueError):
        calculator.divide(1, 0)

# TODO: Test với mock
class UserService:
    """
    Service xử lý người dùng
    """
    def __init__(self, db):
        self.db = db
    
    def get_user(self, user_id):
        return self.db.get_user(user_id)
    
    def create_user(self, user_data):
        return self.db.create_user(user_data)

def test_user_service():
    """
    Test UserService với mock
    """
    # Tạo mock database
    mock_db = Mock()
    
    # Cấu hình mock
    mock_db.get_user.return_value = {"id": 1, "name": "Test User"}
    mock_db.create_user.return_value = {"id": 2, "name": "New User"}
    
    # Tạo service với mock
    service = UserService(mock_db)
    
    # Test get_user
    user = service.get_user(1)
    assert user["name"] == "Test User"
    mock_db.get_user.assert_called_once_with(1)
    
    # Test create_user
    new_user = service.create_user({"name": "New User"})
    assert new_user["name"] == "New User"
    mock_db.create_user.assert_called_once_with({"name": "New User"})

# TODO: Test với patch
class EmailService:
    """
    Service gửi email
    """
    def send_email(self, to, subject, body):
        # Giả lập gửi email
        print(f"Sending email to {to}: {subject}")
        return True

class NotificationService:
    """
    Service gửi thông báo
    """
    def __init__(self, email_service):
        self.email_service = email_service
    
    def notify(self, user, message):
        return self.email_service.send_email(
            user["email"],
            "Notification",
            message
        )

def test_notification_service():
    """
    Test NotificationService với patch
    """
    with patch("__main__.EmailService") as mock_email_service:
        # Cấu hình mock
        mock_instance = mock_email_service.return_value
        mock_instance.send_email.return_value = True
        
        # Tạo service với mock
        notification_service = NotificationService(mock_instance)
        
        # Test notify
        user = {"email": "test@example.com"}
        result = notification_service.notify(user, "Test message")
        
        assert result is True
        mock_instance.send_email.assert_called_once_with(
            "test@example.com",
            "Notification",
            "Test message"
        )

"""
Bài tập về nhà:
1. Tạo test suite cho một hệ thống quản lý thư viện
2. Tạo test suite cho một hệ thống quản lý đơn hàng
3. Tạo test suite cho một hệ thống xác thực
4. Tạo test suite cho một hệ thống cache
5. Tạo test suite cho một hệ thống log
""" 
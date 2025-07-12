"""
Bài tập 5: Xử Lý Ngoại Lệ và Logging

Mục tiêu:
- Hiểu cách xử lý ngoại lệ trong Python
- Thực hành với try-except blocks
- Sử dụng logging để ghi log
"""

import logging
import sys
from datetime import datetime

# TODO: Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# TODO: Xử lý ngoại lệ cơ bản
def divide_numbers(a, b):
    """
    Chia hai số và xử lý ngoại lệ
    """
    try:
        result = a / b
        logger.info(f"Kết quả phép chia {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Lỗi: Không thể chia cho 0")
        return None
    except TypeError:
        logger.error("Lỗi: Đầu vào phải là số")
        return None

# Test hàm divide_numbers
print("Test phép chia:")
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers("10", 2))

# TODO: Xử lý nhiều ngoại lệ
def process_data(data):
    """
    Xử lý dữ liệu với nhiều loại ngoại lệ
    """
    try:
        if not data:
            raise ValueError("Dữ liệu trống")
        
        if not isinstance(data, (list, tuple)):
            raise TypeError("Dữ liệu phải là list hoặc tuple")
        
        result = sum(data) / len(data)
        logger.info(f"Xử lý dữ liệu thành công: {result}")
        return result
    
    except ValueError as e:
        logger.error(f"Lỗi giá trị: {str(e)}")
        return None
    except TypeError as e:
        logger.error(f"Lỗi kiểu dữ liệu: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Lỗi không xác định: {str(e)}")
        return None

# Test hàm process_data
print("\nTest xử lý dữ liệu:")
print(process_data([1, 2, 3, 4, 5]))
print(process_data([]))
print(process_data("12345"))

# TODO: Custom Exception
class ValidationError(Exception):
    """
    Ngoại lệ tùy chỉnh cho lỗi validation
    """
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(self.message)

# TODO: Sử dụng custom exception
def validate_user(username, age):
    """
    Kiểm tra thông tin người dùng
    """
    try:
        if not username:
            raise ValidationError("Tên người dùng không được để trống", "username")
        
        if not isinstance(age, int):
            raise ValidationError("Tuổi phải là số nguyên", "age")
        
        if age < 0 or age > 150:
            raise ValidationError("Tuổi không hợp lệ", "age")
        
        logger.info(f"Validation thành công cho user: {username}")
        return True
    
    except ValidationError as e:
        logger.error(f"Lỗi validation: {e.message} (field: {e.field})")
        return False

# Test hàm validate_user
print("\nTest validation:")
print(validate_user("", 25))
print(validate_user("An", "25"))
print(validate_user("Bình", 200))
print(validate_user("Cường", 25))

# TODO: Context Manager
class DatabaseConnection:
    """
    Class minh họa context manager
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None
    
    def __enter__(self):
        logger.info(f"Kết nối đến database {self.host}:{self.port}")
        self.connection = "Connected"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logger.error(f"Lỗi: {exc_val}")
        logger.info("Đóng kết nối database")
        self.connection = None

# Test context manager
print("\nTest database connection:")
try:
    with DatabaseConnection("localhost", 5432) as db:
        print(f"Trạng thái kết nối: {db.connection}")
        raise Exception("Lỗi kết nối")
except Exception as e:
    print(f"Bắt được lỗi: {str(e)}")

"""
Bài tập về nhà:
1. Tạo một hệ thống xử lý file với try-except và logging
2. Tạo một class ValidationError mới với nhiều thông tin hơn
3. Tạo một context manager để quản lý tài nguyên
4. Tạo một decorator để log thời gian thực thi của hàm
5. Tạo một hệ thống retry với exponential backoff
""" 
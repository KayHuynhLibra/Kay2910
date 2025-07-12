# Programming Reference Guide / Hướng Dẫn Tham Khảo Lập Trình

## Python Basics / Cơ Bản Python

### Variables and Data Types / Biến và Kiểu Dữ Liệu
```python
# Numbers / Số
integer = 42
float_num = 3.14
complex_num = 1 + 2j

# Strings / Chuỗi
string = "Hello"
multi_line = """Multiple
lines"""

# Lists / Danh sách
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

# Tuples / Bộ
tuple1 = (1, 2, 3)
tuple2 = ("x", "y", "z")

# Dictionaries / Từ điển
dict1 = {"name": "John", "age": 30}
dict2 = {1: "one", 2: "two"}

# Sets / Tập hợp
set1 = {1, 2, 3}
set2 = {"a", "b", "c"}
```

### Operators / Toán Tử
```python
# Arithmetic / Số học
a + b  # Addition / Cộng
a - b  # Subtraction / Trừ
a * b  # Multiplication / Nhân
a / b  # Division / Chia
a % b  # Modulus / Chia lấy dư
a ** b # Exponentiation / Lũy thừa

# Comparison / So sánh
a == b # Equal / Bằng
a != b # Not equal / Không bằng
a > b  # Greater than / Lớn hơn
a < b  # Less than / Nhỏ hơn
a >= b # Greater or equal / Lớn hơn hoặc bằng
a <= b # Less or equal / Nhỏ hơn hoặc bằng

# Logical / Logic
a and b # Logical AND / Và
a or b  # Logical OR / Hoặc
not a   # Logical NOT / Không
```

### Control Structures / Cấu Trúc Điều Khiển
```python
# If statement / Câu lệnh if
if condition:
    # code
elif another_condition:
    # code
else:
    # code

# For loop / Vòng lặp for
for item in sequence:
    # code

# While loop / Vòng lặp while
while condition:
    # code

# Break and continue / Break và continue
for item in sequence:
    if condition:
        break
    if another_condition:
        continue
```

## Functions / Hàm

### Basic Functions / Hàm Cơ Bản
```python
# Function definition / Định nghĩa hàm
def function_name(parameters):
    # function body / Thân hàm
    return result

# Function call / Gọi hàm
result = function_name(arguments)

# Lambda functions / Hàm lambda
lambda x: x * 2
```

### Function Parameters / Tham Số Hàm
```python
# Required parameters / Tham số bắt buộc
def func(a, b):
    return a + b

# Default parameters / Tham số mặc định
def func(a, b=0):
    return a + b

# Variable arguments / Tham số biến
def func(*args):
    return sum(args)

# Keyword arguments / Tham số từ khóa
def func(**kwargs):
    return kwargs
```

## Object-Oriented Programming / Lập Trình Hướng Đối Tượng

### Classes / Lớp
```python
# Class definition / Định nghĩa lớp
class MyClass:
    # Class variable / Biến lớp
    class_var = 0

    def __init__(self, param):
        # Instance variable / Biến đối tượng
        self.param = param

    def method(self):
        # Instance method / Phương thức đối tượng
        return self.param

    @classmethod
    def class_method(cls):
        # Class method / Phương thức lớp
        return cls.class_var

    @staticmethod
    def static_method():
        # Static method / Phương thức tĩnh
        return "static"
```

### Inheritance / Kế Thừa
```python
# Parent class / Lớp cha
class Parent:
    def method(self):
        return "parent"

# Child class / Lớp con
class Child(Parent):
    def method(self):
        return "child"

# Multiple inheritance / Kế thừa nhiều lớp
class Multiple(Parent1, Parent2):
    pass
```

## File Operations / Thao Tác File

### Reading Files / Đọc File
```python
# Read entire file / Đọc toàn bộ file
with open('file.txt', 'r') as f:
    content = f.read()

# Read line by line / Đọc từng dòng
with open('file.txt', 'r') as f:
    for line in f:
        process(line)

# Read specific lines / Đọc các dòng cụ thể
with open('file.txt', 'r') as f:
    lines = f.readlines()
```

### Writing Files / Ghi File
```python
# Write to file / Ghi vào file
with open('file.txt', 'w') as f:
    f.write('content')

# Append to file / Thêm vào file
with open('file.txt', 'a') as f:
    f.write('new content')

# Write multiple lines / Ghi nhiều dòng
with open('file.txt', 'w') as f:
    f.writelines(['line1\n', 'line2\n'])
```

## Error Handling / Xử Lý Lỗi

### Try-Except Blocks / Khối Try-Except
```python
# Basic try-except / Try-except cơ bản
try:
    # code
except Exception as e:
    # handle error / xử lý lỗi

# Multiple exceptions / Nhiều ngoại lệ
try:
    # code
except ValueError:
    # handle ValueError
except TypeError:
    # handle TypeError
except Exception as e:
    # handle other exceptions
```

### Custom Exceptions / Ngoại Lệ Tùy Chỉnh
```python
# Define custom exception / Định nghĩa ngoại lệ tùy chỉnh
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

# Raise custom exception / Ném ngoại lệ tùy chỉnh
raise CustomError("Error message")
```

## Modules and Packages / Module và Package

### Importing / Nhập Module
```python
# Import module / Nhập module
import module

# Import specific items / Nhập các thành phần cụ thể
from module import item

# Import with alias / Nhập với bí danh
import module as m
from module import item as i
```

### Creating Packages / Tạo Package
```
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

## Best Practices / Thực Hành Tốt Nhất

### Code Style / Phong Cách Code
```python
# PEP 8 guidelines / Hướng dẫn PEP 8
# - Use 4 spaces for indentation / Sử dụng 4 khoảng trắng cho thụt lề
# - Maximum line length: 79 characters / Độ dài dòng tối đa: 79 ký tự
# - Use descriptive names / Sử dụng tên mô tả
# - Add comments / Thêm chú thích
```

### Testing / Kiểm Thử
```python
# Unit testing / Kiểm thử đơn vị
import unittest

class TestMyFunction(unittest.TestCase):
    def test_function(self):
        self.assertEqual(function(), expected)

# Test fixtures / Bộ kiểm thử
def setUp(self):
    # setup code
def tearDown(self):
    # cleanup code
```

### Version Control / Quản Lý Phiên Bản
```
# Git commands / Lệnh Git
git init
git add .
git commit -m "message"
git push
git pull
```

## Security / Bảo Mật

### Input Validation / Xác Thực Đầu Vào
```python
# Validate input / Xác thực đầu vào
def validate_input(data):
    if not isinstance(data, str):
        raise TypeError("Input must be string")
    if len(data) > 100:
        raise ValueError("Input too long")
    return data

# Sanitize input / Làm sạch đầu vào
import html
def sanitize_input(data):
    return html.escape(data)
```

### Secure Coding Practices / Thực Hành Code An Toàn
```python
# Use parameterized queries / Sử dụng truy vấn tham số hóa
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# Hash passwords / Băm mật khẩu
import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Use secure random / Sử dụng ngẫu nhiên an toàn
import secrets
token = secrets.token_hex(16)
```

## Resources / Tài Nguyên
- Python Documentation
- PEP 8 Style Guide
- Python Security Best Practices
- Online Courses and Tutorials 
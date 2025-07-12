# Programming Fundamentals / Kiến Thức Cơ Bản Lập Trình

## Introduction / Giới Thiệu
- What is programming? / Lập trình là gì?
- Why Python? / Tại sao chọn Python?
- Python versions / Các phiên bản Python
- Development environment / Môi trường phát triển

## Python Basics / Python Cơ Bản
### Variables and Data Types / Biến và Kiểu Dữ Liệu
```python
# Numbers / Số
age = 25
height = 1.75

# Strings / Chuỗi
name = "John Doe"
message = 'Hello, World!'

# Lists / Danh sách
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

# Dictionaries / Từ điển
person = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}
```

### Operators / Toán Tử
- Arithmetic / Số học
- Comparison / So sánh
- Logical / Logic
- Assignment / Gán

### Control Structures / Cấu Trúc Điều Khiển
```python
# If statements / Câu lệnh if
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Loops / Vòng lặp
for i in range(5):
    print(i)

while count < 5:
    print(count)
    count += 1
```

## Functions / Hàm
### Basic Functions / Hàm Cơ Bản
```python
def greet(name):
    return f"Hello, {name}!"

def calculate_sum(a, b):
    return a + b
```

### Function Parameters / Tham Số Hàm
- Required parameters / Tham số bắt buộc
- Default parameters / Tham số mặc định
- Keyword arguments / Đối số từ khóa
- Variable arguments / Đối số biến

## Object-Oriented Programming / Lập Trình Hướng Đối Tượng
### Classes / Lớp
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name}"
```

### Inheritance / Kế Thừa
```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
```

## File Operations / Thao Tác File
### Reading Files / Đọc File
```python
with open('file.txt', 'r') as f:
    content = f.read()
```

### Writing Files / Ghi File
```python
with open('file.txt', 'w') as f:
    f.write('Hello, World!')
```

## Error Handling / Xử Lý Lỗi
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup")
```

## Modules and Packages / Module và Gói
- Importing modules / Nhập module
- Creating packages / Tạo gói
- Virtual environments / Môi trường ảo
- Package management / Quản lý gói

## Best Practices / Thực Hành Tốt Nhất
- Code style / Phong cách code
- Documentation / Tài liệu hóa
- Testing / Kiểm thử
- Version control / Quản lý phiên bản

## Security / Bảo Mật
- Input validation / Xác thực đầu vào
- Secure coding / Lập trình an toàn
- Common vulnerabilities / Lỗ hổng thường gặp
- Best practices / Thực hành tốt nhất

## Resources / Tài Nguyên
- Python Documentation / Tài liệu Python
- Online courses / Khóa học trực tuyến
- Books / Sách
- Communities / Cộng đồng

## Lab Exercises / Bài Tập Thực Hành
1. Basic syntax / Cú pháp cơ bản
2. Functions and classes / Hàm và lớp
3. File operations / Thao tác file
4. Error handling / Xử lý lỗi

## Assessment / Đánh Giá
- Quiz / Kiểm tra
- Lab assignments / Bài tập thực hành
- Project / Dự án
- Final exam / Thi cuối khóa

## Next Steps / Các Bước Tiếp Theo
- Advanced Python / Python nâng cao
- Web development / Phát triển web
- Data science / Khoa học dữ liệu
- Security programming / Lập trình bảo mật 
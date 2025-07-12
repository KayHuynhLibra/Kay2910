# Lab 3: Programming Fundamentals / Lab 3: Kiến Thức Cơ Bản Lập Trình

## Overview / Tổng Quan
This lab introduces fundamental programming concepts using Python. Students will learn about variables, control structures, functions, and basic algorithms.

Lab này giới thiệu các khái niệm lập trình cơ bản sử dụng Python. Học viên sẽ học về biến, cấu trúc điều khiển, hàm và thuật toán cơ bản.

## Objectives / Mục Tiêu
- Understand basic programming concepts
- Learn Python syntax and data types
- Master control structures and functions
- Practice problem-solving with algorithms

- Hiểu các khái niệm lập trình cơ bản
- Học cú pháp và kiểu dữ liệu Python
- Thành thạo cấu trúc điều khiển và hàm
- Thực hành giải quyết vấn đề với thuật toán

## Prerequisites / Yêu Cầu Đầu Vào
- Python 3.x installed
- Text editor (VS Code recommended)
- Basic understanding of programming
- Terminal access

- Đã cài đặt Python 3.x
- Trình soạn thảo văn bản (khuyến nghị VS Code)
- Hiểu biết cơ bản về lập trình
- Truy cập terminal

## Lab Setup / Thiết Lập Lab
1. Create a working directory:
```bash
mkdir ~/python_lab
cd ~/python_lab
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

1. Tạo thư mục làm việc:
```bash
mkdir ~/python_lab
cd ~/python_lab
```

2. Tạo môi trường ảo:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## Exercises / Bài Tập

### Exercise 1: Variables and Data Types / Bài Tập 1: Biến và Kiểu Dữ Liệu
1. Create variables:
```python
# Numbers
age = 25
height = 1.75

# Strings
name = "John Doe"
message = 'Hello, World!'

# Lists
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

# Dictionaries
person = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}
```

2. Type conversion:
```python
# String to number
num_str = "123"
num = int(num_str)

# Number to string
num = 123
num_str = str(num)

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
```

1. Tạo biến:
```python
# Số
age = 25
height = 1.75

# Chuỗi
name = "John Doe"
message = 'Hello, World!'

# Danh sách
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']

# Từ điển
person = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}
```

2. Chuyển đổi kiểu:
```python
# Chuỗi sang số
num_str = "123"
num = int(num_str)

# Số sang chuỗi
num = 123
num_str = str(num)

# Danh sách sang tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
```

### Exercise 2: Control Structures / Bài Tập 2: Cấu Trúc Điều Khiển
1. If statements:
```python
age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

2. Loops:
```python
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

1. Câu lệnh if:
```python
age = 18

if age >= 18:
    print("Người lớn")
elif age >= 13:
    print("Thanh thiếu niên")
else:
    print("Trẻ em")
```

2. Vòng lặp:
```python
# Vòng lặp for
for i in range(5):
    print(i)

# Vòng lặp while
count = 0
while count < 5:
    print(count)
    count += 1
```

### Exercise 3: Functions / Bài Tập 3: Hàm
1. Basic functions:
```python
def greet(name):
    return f"Hello, {name}!"

def calculate_sum(a, b):
    return a + b
```

2. Function with default parameters:
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

3. Lambda functions:
```python
square = lambda x: x**2
add = lambda x, y: x + y
```

1. Hàm cơ bản:
```python
def greet(name):
    return f"Xin chào, {name}!"

def calculate_sum(a, b):
    return a + b
```

2. Hàm với tham số mặc định:
```python
def greet(name, greeting="Xin chào"):
    return f"{greeting}, {name}!"
```

3. Hàm lambda:
```python
square = lambda x: x**2
add = lambda x, y: x + y
```

### Exercise 4: File Operations / Bài Tập 4: Thao Tác File
1. Read file:
```python
with open('file.txt', 'r') as f:
    content = f.read()
```

2. Write file:
```python
with open('file.txt', 'w') as f:
    f.write('Hello, World!')
```

3. Append to file:
```python
with open('file.txt', 'a') as f:
    f.write('\nNew line')
```

1. Đọc file:
```python
with open('file.txt', 'r') as f:
    content = f.read()
```

2. Ghi file:
```python
with open('file.txt', 'w') as f:
    f.write('Hello, World!')
```

3. Thêm vào file:
```python
with open('file.txt', 'a') as f:
    f.write('\nDòng mới')
```

## Challenge / Thử Thách
Create a program that:
1. Reads a text file
2. Counts word frequency
3. Generates a report
4. Saves results to a new file

Tạo một chương trình:
1. Đọc file văn bản
2. Đếm tần suất từ
3. Tạo báo cáo
4. Lưu kết quả vào file mới

## Submission / Nộp Bài
Submit the following:
1. Python scripts for exercises
2. Challenge solution
3. Test cases and results
4. Lab report with findings

Nộp các nội dung sau:
1. Script Python cho các bài tập
2. Giải pháp thử thách
3. Các trường hợp kiểm thử và kết quả
4. Báo cáo lab với các phát hiện

## Resources / Tài Nguyên
- Python Documentation
- Python for Beginners
- Python Programming Guide
- Python Cookbook

## Grading Criteria / Tiêu Chí Đánh Giá
- Exercise completion: 60%
- Challenge solution: 30%
- Documentation: 10%

- Hoàn thành bài tập: 60%
- Giải pháp thử thách: 30%
- Tài liệu: 10% 
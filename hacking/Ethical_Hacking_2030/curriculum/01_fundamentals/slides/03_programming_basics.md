# Programming Basics / Cơ Bản Lập Trình

## Introduction / Giới Thiệu

### What is Programming? / Lập Trình là gì?
- Writing instructions for computers / Viết hướng dẫn cho máy tính
- Problem solving / Giải quyết vấn đề
- Algorithm development / Phát triển thuật toán
- Code implementation / Triển khai mã

### Programming Languages / Ngôn Ngữ Lập Trình
- High-level languages / Ngôn ngữ bậc cao
- Low-level languages / Ngôn ngữ bậc thấp
- Compiled languages / Ngôn ngữ biên dịch
- Interpreted languages / Ngôn ngữ thông dịch

### Common Languages / Ngôn Ngữ Phổ Biến
```
Python - General purpose / Đa mục đích
JavaScript - Web development / Phát triển web
C/C++ - System programming / Lập trình hệ thống
Java - Enterprise applications / Ứng dụng doanh nghiệp
```

## Basic Concepts / Khái Niệm Cơ Bản

### Variables and Data Types / Biến và Kiểu Dữ Liệu
```
Numbers / Số:
- Integer / Số nguyên
- Float / Số thực
- Double / Số thực độ chính xác kép

Strings / Chuỗi:
- Text / Văn bản
- Characters / Ký tự
- String operations / Thao tác chuỗi

Booleans / Logic:
- True / Đúng
- False / Sai
- Logical operations / Thao tác logic

Arrays / Mảng:
- Lists / Danh sách
- Indexing / Đánh chỉ số
- Array operations / Thao tác mảng
```

### Control Structures / Cấu Trúc Điều Khiển
```
Conditionals / Điều kiện:
if (condition) {
    // code
} else {
    // code
}

Loops / Vòng lặp:
for (initialization; condition; increment) {
    // code
}

while (condition) {
    // code
}
```

### Functions / Hàm
```
Function Definition / Định nghĩa hàm:
def function_name(parameters):
    // code
    return value

Function Call / Gọi hàm:
result = function_name(arguments)
```

## Object-Oriented Programming / Lập Trình Hướng Đối Tượng

### Classes and Objects / Lớp và Đối Tượng
```
Class Definition / Định nghĩa lớp:
class ClassName:
    def __init__(self):
        // initialization code
    
    def method_name(self):
        // method code

Object Creation / Tạo đối tượng:
object_name = ClassName()
```

### Inheritance / Kế Thừa
```
class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        // additional initialization
```

### Encapsulation / Đóng Gói
```
Private attributes / Thuộc tính riêng tư
Public methods / Phương thức công khai
Protected members / Thành viên được bảo vệ
```

## Error Handling / Xử Lý Lỗi

### Try-Catch Blocks / Khối Try-Catch
```
try:
    // code that might raise an error
except ErrorType:
    // handle the error
finally:
    // code that always executes
```

### Common Errors / Lỗi Thường Gặp
```
Syntax errors / Lỗi cú pháp
Runtime errors / Lỗi thực thi
Logical errors / Lỗi logic
Type errors / Lỗi kiểu dữ liệu
```

## File Operations / Thao Tác File

### Reading Files / Đọc File
```
with open('file.txt', 'r') as file:
    content = file.read()
```

### Writing Files / Ghi File
```
with open('file.txt', 'w') as file:
    file.write('content')
```

### File Modes / Chế Độ File
```
'r' - Read / Đọc
'w' - Write / Ghi
'a' - Append / Thêm
'b' - Binary / Nhị phân
```

## Debugging / Gỡ Lỗi

### Debugging Tools / Công Cụ Gỡ Lỗi
```
Print statements / Lệnh in
Debugger / Trình gỡ lỗi
Logging / Ghi log
Unit testing / Kiểm thử đơn vị
```

### Debugging Techniques / Kỹ Thuật Gỡ Lỗi
```
Breakpoints / Điểm dừng
Step through / Thực hiện từng bước
Variable inspection / Kiểm tra biến
Stack trace / Dấu vết ngăn xếp
```

## Best Practices / Thực Hành Tốt Nhất

### Code Organization / Tổ Chức Mã
```
Modular design / Thiết kế module
Clean code / Mã sạch
Documentation / Tài liệu
Version control / Kiểm soát phiên bản
```

### Naming Conventions / Quy Ước Đặt Tên
```
Variables / Biến
Functions / Hàm
Classes / Lớp
Constants / Hằng số
```

## Development Tools / Công Cụ Phát Triển

### IDEs / Môi Trường Phát Triển
```
Visual Studio Code
PyCharm
Eclipse
IntelliJ IDEA
```

### Version Control / Kiểm Soát Phiên Bản
```
Git commands / Lệnh Git:
git init
git add
git commit
git push
git pull
```

## Lab Exercises / Bài Tập Thực Hành

### Basic Programming / Lập Trình Cơ Bản
1. Variable operations / Thao tác biến
2. Control structures / Cấu trúc điều khiển
3. Functions / Hàm
4. File handling / Xử lý file

### Object-Oriented Programming / Lập Trình Hướng Đối Tượng
1. Class creation / Tạo lớp
2. Inheritance / Kế thừa
3. Encapsulation / Đóng gói
4. Polymorphism / Đa hình

### Debugging Practice / Thực Hành Gỡ Lỗi
1. Error handling / Xử lý lỗi
2. Debugging tools / Công cụ gỡ lỗi
3. Testing / Kiểm thử
4. Code review / Đánh giá mã

## Assessment / Đánh Giá

### Quizzes / Kiểm Tra
- Multiple choice / Trắc nghiệm
- Code analysis / Phân tích mã
- Problem solving / Giải quyết vấn đề
- Debugging exercises / Bài tập gỡ lỗi

### Projects / Dự Án
- Small applications / Ứng dụng nhỏ
- Code refactoring / Tái cấu trúc mã
- Testing implementation / Triển khai kiểm thử
- Documentation / Tài liệu

## Resources / Tài Nguyên

### Online Documentation / Tài Liệu Trực Tuyến
- Language Documentation
- Tutorial Websites
- Online Courses
- Code Examples

### Books / Sách
- "Clean Code"
- "Python Programming"
- "JavaScript: The Good Parts"
- "Head First Design Patterns"

### Communities / Cộng Đồng
- Stack Overflow
- GitHub
- Reddit /r/programming
- Dev.to

### Training / Đào Tạo
- Codecademy
- freeCodeCamp
- Coursera
- Udemy 
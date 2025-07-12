"""
Hàm và Module trong Python

Mục tiêu:
- Hiểu về cách định nghĩa và gọi hàm
- Biết cách sử dụng tham số và giá trị trả về
- Hiểu về phạm vi biến (scope)
- Biết cách sử dụng module
"""

# 1. Định nghĩa hàm cơ bản
def greet(name):
    """Hàm chào hỏi"""
    return f"Xin chào, {name}!"

# 2. Hàm với nhiều tham số
def calculate_rectangle_area(length, width):
    """Tính diện tích hình chữ nhật"""
    return length * width

# 3. Hàm với tham số mặc định
def greet_with_title(name, title="Mr."):
    """Chào hỏi với danh xưng"""
    return f"Xin chào, {title} {name}!"

# 4. Hàm với tham số tùy chọn (*args)
def sum_numbers(*args):
    """Tính tổng các số"""
    return sum(args)

# 5. Hàm với tham số từ khóa tùy chọn (**kwargs)
def print_person_info(**kwargs):
    """In thông tin người dùng"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 6. Hàm với kiểu trả về
def get_square_root(number: float) -> float:
    """Tính căn bậc hai của số"""
    return number ** 0.5

# 7. Hàm lambda
square = lambda x: x**2

# 8. Phạm vi biến (scope)
def demonstrate_scope():
    x = 10  # Biến cục bộ
    
    def inner_function():
        y = 20  # Biến cục bộ của inner_function
        print(f"x trong inner_function: {x}")
        print(f"y trong inner_function: {y}")
    
    inner_function()
    print(f"x trong demonstrate_scope: {x}")
    # print(y)  # Lỗi: y không tồn tại trong phạm vi này

# 9. Decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Trước khi gọi hàm")
        result = func(*args, **kwargs)
        print("Sau khi gọi hàm")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello, {name}!"

# 10. Generator
def fibonacci(n):
    """Tạo dãy Fibonacci"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 11. Bài tập thực hành
def practice_functions():
    """
    Bài tập:
    1. Viết hàm tính giai thừa
    2. Viết hàm kiểm tra số nguyên tố
    3. Viết hàm đảo ngược chuỗi
    4. Viết hàm tìm số lớn nhất trong list
    5. Viết decorator để đo thời gian thực thi hàm
    """
    # Viết code của bạn ở đây
    pass

if __name__ == "__main__":
    # Chạy các ví dụ
    print(greet("John"))
    print(calculate_rectangle_area(5, 3))
    print(greet_with_title("John", "Dr."))
    print(sum_numbers(1, 2, 3, 4, 5))
    print_person_info(name="John", age=25, city="New York")
    print(get_square_root(16))
    print(square(5))
    
    print("\nPhạm vi biến:")
    demonstrate_scope()
    
    print("\nDecorator:")
    print(say_hello("John"))
    
    print("\nGenerator:")
    for num in fibonacci(5):
        print(num)
    
    print("\nBài tập thực hành:")
    practice_functions() 
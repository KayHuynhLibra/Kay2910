"""
Functions and Modules in Python
Hàm và Module trong Python

This module demonstrates function definitions, parameters, and module usage.
Module này minh họa định nghĩa hàm, tham số và cách sử dụng module.
"""

# Basic function / Hàm cơ bản
def greet(name):
    """
    Greet a person by name
    Chào một người theo tên
    
    Args:
        name (str): Name of the person
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}! / Xin chào, {name}!"

# Function with multiple parameters / Hàm với nhiều tham số
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle
    Tính diện tích hình chữ nhật
    
    Args:
        length (float): Length of the rectangle
        width (float): Width of the rectangle
    Returns:
        float: Area of the rectangle
    """
    return length * width

# Function with default parameters / Hàm với tham số mặc định
def create_user(name, age=18, city="Unknown"):
    """
    Create a user with optional parameters
    Tạo người dùng với các tham số tùy chọn
    
    Args:
        name (str): User's name
        age (int, optional): User's age. Defaults to 18
        city (str, optional): User's city. Defaults to "Unknown"
    Returns:
        dict: User information
    """
    return {
        "name": name,
        "age": age,
        "city": city
    }

# Function with variable arguments / Hàm với số lượng tham số thay đổi
def sum_numbers(*args):
    """
    Sum all provided numbers
    Tính tổng tất cả các số được cung cấp
    
    Args:
        *args: Variable number of numbers
    Returns:
        float: Sum of all numbers
    """
    return sum(args)

# Function with keyword arguments / Hàm với tham số từ khóa
def print_person_info(**kwargs):
    """
    Print person information
    In thông tin người dùng
    
    Args:
        **kwargs: Keyword arguments containing person information
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda function / Hàm lambda
square = lambda x: x ** 2

def demonstrate_functions():
    """
    Demonstrate various function examples
    Minh họa các ví dụ về hàm
    """
    # Basic function call / Gọi hàm cơ bản
    print("\nBasic function / Hàm cơ bản:")
    print(greet("John"))
    
    # Multiple parameters / Nhiều tham số
    print("\nMultiple parameters / Nhiều tham số:")
    area = calculate_rectangle_area(5, 3)
    print(f"Rectangle area: {area}")
    
    # Default parameters / Tham số mặc định
    print("\nDefault parameters / Tham số mặc định:")
    user1 = create_user("Alice")
    user2 = create_user("Bob", 25, "New York")
    print(f"User 1: {user1}")
    print(f"User 2: {user2}")
    
    # Variable arguments / Tham số thay đổi
    print("\nVariable arguments / Tham số thay đổi:")
    total = sum_numbers(1, 2, 3, 4, 5)
    print(f"Sum: {total}")
    
    # Keyword arguments / Tham số từ khóa
    print("\nKeyword arguments / Tham số từ khóa:")
    print_person_info(name="John", age=30, city="London")
    
    # Lambda function / Hàm lambda
    print("\nLambda function / Hàm lambda:")
    print(f"Square of 5: {square(5)}")

if __name__ == "__main__":
    demonstrate_functions() 
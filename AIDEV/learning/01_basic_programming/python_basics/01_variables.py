"""
Variables and Data Types in Python
Biến và Kiểu Dữ Liệu trong Python

This module demonstrates basic variable usage and data types in Python.
Module này minh họa cách sử dụng biến và các kiểu dữ liệu cơ bản trong Python.
"""

# Integer (Số nguyên)
age = 25
# English: Integer is a whole number without decimal points
# Tiếng Việt: Số nguyên là số không có phần thập phân

# Float (Số thực)
height = 1.75
# English: Float represents decimal numbers
# Tiếng Việt: Số thực biểu diễn các số có phần thập phân

# String (Chuỗi)
name = "John Doe"
# English: String is a sequence of characters enclosed in quotes
# Tiếng Việt: Chuỗi là một dãy các ký tự được đặt trong dấu ngoặc kép

# Boolean (Luận lý)
is_student = True
# English: Boolean represents True or False values
# Tiếng Việt: Boolean biểu diễn giá trị Đúng hoặc Sai

# List (Danh sách)
fruits = ["apple", "banana", "orange"]
# English: List is an ordered collection of items
# Tiếng Việt: List là một tập hợp có thứ tự các phần tử

# Dictionary (Từ điển)
person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
# English: Dictionary stores key-value pairs
# Tiếng Việt: Dictionary lưu trữ các cặp khóa-giá trị

# Tuple (Bộ)
coordinates = (10, 20)
# English: Tuple is an immutable ordered collection
# Tiếng Việt: Tuple là một tập hợp có thứ tự không thể thay đổi

# Set (Tập hợp)
unique_numbers = {1, 2, 3, 4, 5}
# English: Set is an unordered collection of unique elements
# Tiếng Việt: Set là một tập hợp không có thứ tự các phần tử duy nhất

def print_variable_info(var_name, var_value):
    """
    Print information about a variable
    In thông tin về một biến
    
    Args:
        var_name (str): Name of the variable
        var_value: Value of the variable
    """
    print(f"Variable name: {var_name}")
    print(f"Value: {var_value}")
    print(f"Type: {type(var_value)}")
    print("-" * 30)

# Example usage / Ví dụ sử dụng
if __name__ == "__main__":
    # Print information about each variable
    # In thông tin về mỗi biến
    print_variable_info("age", age)
    print_variable_info("height", height)
    print_variable_info("name", name)
    print_variable_info("is_student", is_student)
    print_variable_info("fruits", fruits)
    print_variable_info("person", person)
    print_variable_info("coordinates", coordinates)
    print_variable_info("unique_numbers", unique_numbers) 
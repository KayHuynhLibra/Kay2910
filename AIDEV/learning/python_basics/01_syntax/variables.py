"""
Biến và Kiểu Dữ Liệu trong Python

Mục tiêu:
- Hiểu về biến và cách khai báo
- Nắm được các kiểu dữ liệu cơ bản
- Biết cách chuyển đổi kiểu dữ liệu
"""

# 1. Khai báo biến
name = "John"  # String
age = 25       # Integer
height = 1.75  # Float
is_student = True  # Boolean

# 2. In kiểu dữ liệu
print(f"Kiểu của name: {type(name)}")      # <class 'str'>
print(f"Kiểu của age: {type(age)}")        # <class 'int'>
print(f"Kiểu của height: {type(height)}")  # <class 'float'>
print(f"Kiểu của is_student: {type(is_student)}")  # <class 'bool'>

# 3. Chuyển đổi kiểu dữ liệu
age_str = str(age)          # Chuyển int sang str
height_int = int(height)     # Chuyển float sang int
age_float = float(age)      # Chuyển int sang float
is_student_str = str(is_student)  # Chuyển bool sang str

# 4. Kiểm tra kiểu dữ liệu
print(f"age_str là string? {isinstance(age_str, str)}")
print(f"height_int là integer? {isinstance(height_int, int)}")
print(f"age_float là float? {isinstance(age_float, float)}")

# 5. Các kiểu dữ liệu phức tạp
# List
fruits = ["apple", "banana", "orange"]
print(f"Kiểu của fruits: {type(fruits)}")  # <class 'list'>

# Tuple
coordinates = (10, 20)
print(f"Kiểu của coordinates: {type(coordinates)}")  # <class 'tuple'>

# Dictionary
person = {"name": "John", "age": 25}
print(f"Kiểu của person: {type(person)}")  # <class 'dict'>

# Set
unique_numbers = {1, 2, 3, 3, 4}
print(f"Kiểu của unique_numbers: {type(unique_numbers)}")  # <class 'set'>

# 6. None
empty_value = None
print(f"Kiểu của empty_value: {type(empty_value)}")  # <class 'NoneType'>

# 7. Bài tập thực hành
def practice_variables():
    """
    Bài tập:
    1. Tạo biến chứa tên, tuổi, chiều cao của bạn
    2. In ra kiểu dữ liệu của mỗi biến
    3. Chuyển đổi tuổi sang string và chiều cao sang integer
    4. Tạo một dictionary chứa thông tin của bạn
    5. Tạo một list chứa các môn học yêu thích
    """
    # Viết code của bạn ở đây
    pass

if __name__ == "__main__":
    practice_variables() 
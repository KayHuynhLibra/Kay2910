"""
Điều Kiện và Vòng Lặp trong Python

Mục tiêu:
- Hiểu về câu lệnh điều kiện if-elif-else
- Biết cách sử dụng vòng lặp for
- Biết cách sử dụng vòng lặp while
- Biết cách sử dụng break, continue và pass
"""

# 1. Câu lệnh điều kiện
def check_number(number):
    if number > 0:
        print(f"{number} là số dương")
    elif number < 0:
        print(f"{number} là số âm")
    else:
        print(f"{number} là số 0")

# 2. Vòng lặp for
def print_numbers():
    # In các số từ 1 đến 5
    for i in range(1, 6):
        print(i)

    # Duyệt qua list
    fruits = ["apple", "banana", "orange"]
    for fruit in fruits:
        print(fruit)

    # Duyệt qua dictionary
    person = {"name": "John", "age": 25}
    for key, value in person.items():
        print(f"{key}: {value}")

# 3. Vòng lặp while
def count_down():
    count = 5
    while count > 0:
        print(count)
        count -= 1

# 4. Break, Continue và Pass
def demonstrate_control():
    # Break
    for i in range(10):
        if i == 5:
            break
        print(i)

    # Continue
    for i in range(5):
        if i == 2:
            continue
        print(i)

    # Pass
    for i in range(3):
        pass  # Không làm gì cả

# 5. Nested Loops
def print_multiplication_table():
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} x {j} = {i * j}")

# 6. List Comprehension
def demonstrate_list_comprehension():
    # Tạo list các số chẵn
    even_numbers = [x for x in range(10) if x % 2 == 0]
    print(f"Số chẵn: {even_numbers}")

    # Tạo list bình phương
    squares = [x**2 for x in range(5)]
    print(f"Bình phương: {squares}")

# 7. Bài tập thực hành
def practice_control_flow():
    """
    Bài tập:
    1. Viết hàm kiểm tra số nguyên tố
    2. In bảng cửu chương từ 1 đến 5
    3. Tìm số lớn nhất trong list
    4. Đếm số lần xuất hiện của mỗi phần tử trong list
    5. Tạo list các số Fibonacci nhỏ hơn 100
    """
    # Viết code của bạn ở đây
    pass

if __name__ == "__main__":
    # Chạy các ví dụ
    check_number(5)
    check_number(-3)
    check_number(0)
    
    print("\nIn số:")
    print_numbers()
    
    print("\nĐếm ngược:")
    count_down()
    
    print("\nBreak, Continue, Pass:")
    demonstrate_control()
    
    print("\nBảng nhân:")
    print_multiplication_table()
    
    print("\nList Comprehension:")
    demonstrate_list_comprehension()
    
    print("\nBài tập thực hành:")
    practice_control_flow() 
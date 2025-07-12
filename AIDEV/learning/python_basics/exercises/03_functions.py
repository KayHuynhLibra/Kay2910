"""
Bài tập 3: Hàm và Module

Mục tiêu:
- Hiểu cách định nghĩa và sử dụng hàm
- Thực hành với tham số và giá trị trả về
- Làm quen với module và package
"""

# TODO: Hàm cơ bản
def greet(name, greeting="Xin chào"):
    """
    Hàm chào hỏi với tham số mặc định
    """
    return f"{greeting}, {name}!"

# Test hàm greet
print("Test hàm chào hỏi:")
print(greet("An"))
print(greet("Bình", "Chào"))

# TODO: Hàm với nhiều tham số
def calculate_stats(numbers):
    """
    Tính toán các thống kê cơ bản của một danh sách số
    """
    if not numbers:
        return None
    
    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

# Test hàm calculate_stats
numbers = [1, 2, 3, 4, 5]
print("\nThống kê của danh sách số:", numbers)
print(calculate_stats(numbers))

# TODO: Hàm với tham số tùy chọn
def format_text(text, uppercase=False, reverse=False):
    """
    Định dạng văn bản theo các tùy chọn
    """
    if uppercase:
        text = text.upper()
    if reverse:
        text = text[::-1]
    return text

# Test hàm format_text
text = "Hello World"
print("\nĐịnh dạng văn bản:")
print(f"Gốc: {text}")
print(f"Chữ hoa: {format_text(text, uppercase=True)}")
print(f"Đảo ngược: {format_text(text, reverse=True)}")
print(f"Chữ hoa và đảo ngược: {format_text(text, uppercase=True, reverse=True)}")

# TODO: Hàm đệ quy
def factorial(n):
    """
    Tính giai thừa sử dụng đệ quy
    """
    if n < 0:
        raise ValueError("Không thể tính giai thừa cho số âm")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test hàm factorial
print("\nTính giai thừa:")
for i in range(6):
    print(f"{i}! = {factorial(i)}")

# TODO: Hàm với lambda
square = lambda x: x ** 2
cube = lambda x: x ** 3

# Test hàm lambda
print("\nTest hàm lambda:")
print(f"Bình phương của 5: {square(5)}")
print(f"Lập phương của 3: {cube(3)}")

# TODO: Hàm với generator
def fibonacci(n):
    """
    Generator tạo dãy Fibonacci
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Test hàm fibonacci
print("\nDãy Fibonacci:")
print(list(fibonacci(10)))

"""
Bài tập về nhà:
1. Viết hàm tính tổng các số trong một dãy số sử dụng đệ quy
2. Viết hàm tìm ước chung lớn nhất của hai số sử dụng thuật toán Euclidean
3. Viết hàm kiểm tra một chuỗi có phải là palindrome không
4. Viết hàm tạo một generator tạo ra các số nguyên tố
5. Viết một module chứa các hàm tiện ích để xử lý chuỗi
""" 
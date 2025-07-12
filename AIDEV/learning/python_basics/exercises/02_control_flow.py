"""
Bài tập 2: Điều Kiện và Vòng Lặp

Mục tiêu:
- Hiểu và sử dụng các câu lệnh điều kiện
- Thực hành với các loại vòng lặp
- Kết hợp điều kiện và vòng lặp
"""

# TODO: Câu lệnh điều kiện
def check_age(age):
    """
    Kiểm tra tuổi và trả về trạng thái tương ứng
    """
    if age < 0:
        return "Tuổi không hợp lệ"
    elif age < 18:
        return "Vị thành niên"
    elif age < 60:
        return "Người trưởng thành"
    else:
        return "Người cao tuổi"

# Test hàm check_age
print("Kiểm tra tuổi:")
print(f"Tuổi -1: {check_age(-1)}")
print(f"Tuổi 15: {check_age(15)}")
print(f"Tuổi 25: {check_age(25)}")
print(f"Tuổi 65: {check_age(65)}")

# TODO: Vòng lặp for
def print_multiplication_table(n):
    """
    In bảng cửu chương cho số n
    """
    print(f"\nBảng cửu chương {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Test hàm print_multiplication_table
print_multiplication_table(5)

# TODO: Vòng lặp while
def countdown(n):
    """
    Đếm ngược từ n về 0
    """
    print(f"\nĐếm ngược từ {n}:")
    while n >= 0:
        print(n)
        n -= 1

# Test hàm countdown
countdown(5)

# TODO: Kết hợp điều kiện và vòng lặp
def find_primes(limit):
    """
    Tìm các số nguyên tố từ 2 đến limit
    """
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Test hàm find_primes
print("\nCác số nguyên tố từ 2 đến 20:")
print(find_primes(20))

# TODO: Bài tập nâng cao
def fizzbuzz(n):
    """
    In các số từ 1 đến n theo quy tắc FizzBuzz:
    - Nếu số chia hết cho 3, in "Fizz"
    - Nếu số chia hết cho 5, in "Buzz"
    - Nếu số chia hết cho cả 3 và 5, in "FizzBuzz"
    - Nếu không, in số đó
    """
    print(f"\nFizzBuzz từ 1 đến {n}:")
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Test hàm fizzbuzz
fizzbuzz(15)

"""
Bài tập về nhà:
1. Viết hàm kiểm tra một số có phải là số hoàn hảo không
   (số hoàn hảo là số có tổng các ước số bằng chính nó)
2. Viết hàm tìm ước chung lớn nhất của hai số
3. Viết hàm tính giai thừa của một số
4. Viết hàm in tam giác Pascal với chiều cao n
5. Viết hàm tìm số Fibonacci thứ n
""" 
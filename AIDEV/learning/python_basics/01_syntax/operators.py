"""
Toán Tử trong Python

Mục tiêu:
- Hiểu về các loại toán tử trong Python
- Biết cách sử dụng toán tử số học
- Biết cách sử dụng toán tử so sánh
- Biết cách sử dụng toán tử logic
"""

# 1. Toán tử số học
a = 10
b = 3

print(f"a + b = {a + b}")    # Cộng
print(f"a - b = {a - b}")    # Trừ
print(f"a * b = {a * b}")    # Nhân
print(f"a / b = {a / b}")    # Chia
print(f"a // b = {a // b}")  # Chia lấy phần nguyên
print(f"a % b = {a % b}")    # Chia lấy phần dư
print(f"a ** b = {a ** b}")  # Lũy thừa

# 2. Toán tử gán
x = 5
x += 3  # Tương đương x = x + 3
print(f"x sau khi += 3: {x}")

x -= 2  # Tương đương x = x - 2
print(f"x sau khi -= 2: {x}")

x *= 4  # Tương đương x = x * 4
print(f"x sau khi *= 4: {x}")

x /= 2  # Tương đương x = x / 2
print(f"x sau khi /= 2: {x}")

# 3. Toán tử so sánh
print(f"a > b: {a > b}")     # Lớn hơn
print(f"a < b: {a < b}")     # Nhỏ hơn
print(f"a == b: {a == b}")   # Bằng
print(f"a != b: {a != b}")   # Khác
print(f"a >= b: {a >= b}")   # Lớn hơn hoặc bằng
print(f"a <= b: {a <= b}")   # Nhỏ hơn hoặc bằng

# 4. Toán tử logic
p = True
q = False

print(f"p and q: {p and q}")  # AND
print(f"p or q: {p or q}")    # OR
print(f"not p: {not p}")      # NOT

# 5. Toán tử bit
c = 60  # 60 = 0011 1100
d = 13  # 13 = 0000 1101

print(f"c & d = {c & d}")   # AND
print(f"c | d = {c | d}")   # OR
print(f"c ^ d = {c ^ d}")   # XOR
print(f"~c = {~c}")         # NOT
print(f"c << 2 = {c << 2}") # Dịch trái
print(f"c >> 2 = {c >> 2}") # Dịch phải

# 6. Toán tử thành viên
fruits = ["apple", "banana", "orange"]
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# 7. Toán tử định danh
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(f"x is z: {x is z}")       # True
print(f"x is y: {x is y}")       # False
print(f"x == y: {x == y}")       # True

# 8. Bài tập thực hành
def practice_operators():
    """
    Bài tập:
    1. Tính tổng, hiệu, tích, thương của hai số
    2. So sánh hai số và in kết quả
    3. Sử dụng toán tử logic để kiểm tra điều kiện
    4. Thực hiện các phép toán bit
    5. Kiểm tra phần tử trong list
    """
    # Viết code của bạn ở đây
    pass

if __name__ == "__main__":
    practice_operators() 
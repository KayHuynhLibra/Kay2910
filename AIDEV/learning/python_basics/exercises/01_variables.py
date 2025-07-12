"""
Bài tập 1: Biến và Kiểu Dữ Liệu

Mục tiêu:
- Hiểu cách khai báo và sử dụng biến
- Nắm vững các kiểu dữ liệu cơ bản
- Thực hành chuyển đổi kiểu dữ liệu
"""

# TODO: Khai báo các biến với các kiểu dữ liệu khác nhau
# 1. Tạo biến name kiểu string
name = "John"

# 2. Tạo biến age kiểu integer
age = 25

# 3. Tạo biến height kiểu float
height = 1.75

# 4. Tạo biến is_student kiểu boolean
is_student = True

# TODO: In ra kiểu dữ liệu của các biến
print(f"Kiểu dữ liệu của name: {type(name)}")
print(f"Kiểu dữ liệu của age: {type(age)}")
print(f"Kiểu dữ liệu của height: {type(height)}")
print(f"Kiểu dữ liệu của is_student: {type(is_student)}")

# TODO: Chuyển đổi kiểu dữ liệu
# 1. Chuyển age thành string
age_str = str(age)
print(f"age_str: {age_str}, kiểu dữ liệu: {type(age_str)}")

# 2. Chuyển height thành integer
height_int = int(height)
print(f"height_int: {height_int}, kiểu dữ liệu: {type(height_int)}")

# 3. Chuyển is_student thành string
is_student_str = str(is_student)
print(f"is_student_str: {is_student_str}, kiểu dữ liệu: {type(is_student_str)}")

# TODO: Thực hành với các phép toán
# 1. Cộng hai số
num1 = 10
num2 = 5
sum_result = num1 + num2
print(f"Tổng của {num1} và {num2} là: {sum_result}")

# 2. Nối hai chuỗi
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Họ tên đầy đủ: {full_name}")

# TODO: Bài tập nâng cao
# 1. Tạo một dictionary chứa thông tin cá nhân
personal_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}

# 2. In ra thông tin từ dictionary
print("\nThông tin cá nhân:")
for key, value in personal_info.items():
    print(f"{key}: {value}")

# 3. Thêm thông tin mới vào dictionary
personal_info["city"] = "New York"
personal_info["occupation"] = "Developer"

# 4. In ra thông tin đã cập nhật
print("\nThông tin cá nhân sau khi cập nhật:")
for key, value in personal_info.items():
    print(f"{key}: {value}")

"""
Bài tập về nhà:
1. Tạo một list chứa các số từ 1 đến 10
2. Tính tổng các số trong list
3. Tìm số lớn nhất và nhỏ nhất trong list
4. Tạo một tuple chứa thông tin về một sản phẩm (tên, giá, số lượng)
5. Tạo một set chứa các màu sắc và thực hiện các phép toán tập hợp
""" 
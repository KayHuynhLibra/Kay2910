"""
Xử Lý File trong Python

Mục tiêu:
- Hiểu về cách đọc và ghi file
- Biết cách xử lý file text và binary
- Biết cách sử dụng context manager
- Biết cách xử lý lỗi khi làm việc với file
"""

import os
import json
import pickle

# 1. Đọc và ghi file text
def write_text_file():
    """Ghi nội dung vào file text"""
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("Dòng 1\n")
        f.write("Dòng 2\n")
        f.write("Dòng 3\n")

def read_text_file():
    """Đọc nội dung từ file text"""
    try:
        with open("example.txt", "r", encoding="utf-8") as f:
            content = f.read()
            print("Nội dung file:")
            print(content)
    except FileNotFoundError:
        print("Không tìm thấy file")
    except Exception as e:
        print(f"Lỗi: {e}")

# 2. Đọc và ghi file theo dòng
def write_lines():
    """Ghi nhiều dòng vào file"""
    lines = ["Dòng 1", "Dòng 2", "Dòng 3"]
    with open("lines.txt", "w", encoding="utf-8") as f:
        f.writelines(line + "\n" for line in lines)

def read_lines():
    """Đọc file theo từng dòng"""
    try:
        with open("lines.txt", "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("Không tìm thấy file")

# 3. Đọc và ghi file JSON
def write_json_file():
    """Ghi dữ liệu JSON vào file"""
    data = {
        "name": "John",
        "age": 25,
        "city": "New York"
    }
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def read_json_file():
    """Đọc dữ liệu JSON từ file"""
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            print("Dữ liệu JSON:")
            print(data)
    except FileNotFoundError:
        print("Không tìm thấy file")
    except json.JSONDecodeError:
        print("Lỗi định dạng JSON")

# 4. Đọc và ghi file binary
def write_binary_file():
    """Ghi dữ liệu binary vào file"""
    data = [1, 2, 3, 4, 5]
    with open("data.bin", "wb") as f:
        pickle.dump(data, f)

def read_binary_file():
    """Đọc dữ liệu binary từ file"""
    try:
        with open("data.bin", "rb") as f:
            data = pickle.load(f)
            print("Dữ liệu binary:")
            print(data)
    except FileNotFoundError:
        print("Không tìm thấy file")
    except pickle.UnpicklingError:
        print("Lỗi đọc dữ liệu binary")

# 5. Xử lý file với context manager
def file_operations():
    """Thực hiện các thao tác với file"""
    # Tạo thư mục
    if not os.path.exists("temp"):
        os.makedirs("temp")
    
    # Ghi file
    with open("temp/test.txt", "w") as f:
        f.write("Test content")
    
    # Đọc file
    with open("temp/test.txt", "r") as f:
        content = f.read()
        print(f"Nội dung file: {content}")
    
    # Xóa file
    os.remove("temp/test.txt")
    os.rmdir("temp")

# 6. Bài tập thực hành
def practice_file_handling():
    """
    Bài tập:
    1. Tạo file chứa thông tin sinh viên
    2. Đọc và hiển thị thông tin từ file
    3. Thêm thông tin mới vào file
    4. Xóa thông tin cũ từ file
    5. Tạo backup cho file
    """
    # Viết code của bạn ở đây
    pass

if __name__ == "__main__":
    # Chạy các ví dụ
    print("1. Đọc và ghi file text:")
    write_text_file()
    read_text_file()
    
    print("\n2. Đọc và ghi file theo dòng:")
    write_lines()
    read_lines()
    
    print("\n3. Đọc và ghi file JSON:")
    write_json_file()
    read_json_file()
    
    print("\n4. Đọc và ghi file binary:")
    write_binary_file()
    read_binary_file()
    
    print("\n5. Xử lý file với context manager:")
    file_operations()
    
    print("\n6. Bài tập thực hành:")
    practice_file_handling()
    
    # Dọn dẹp file tạm
    for file in ["example.txt", "lines.txt", "data.json", "data.bin"]:
        if os.path.exists(file):
            os.remove(file) 
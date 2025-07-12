"""
Bài tập 6: Xử Lý File và JSON

Mục tiêu:
- Hiểu cách đọc/ghi file trong Python
- Thực hành với JSON
- Xử lý file với context manager
"""

import json
import os
from datetime import datetime
from pathlib import Path

# TODO: Đọc/ghi file text
def read_text_file(filename):
    """
    Đọc nội dung file text
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return None
    except Exception as e:
        print(f"Lỗi khi đọc file: {str(e)}")
        return None

def write_text_file(filename, content):
    """
    Ghi nội dung vào file text
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Lỗi khi ghi file: {str(e)}")
        return False

# Test đọc/ghi file text
print("Test đọc/ghi file text:")
content = "Hello, World!\nThis is a test file."
write_text_file("test.txt", content)
print(read_text_file("test.txt"))

# TODO: Xử lý JSON
def save_to_json(data, filename):
    """
    Lưu dữ liệu vào file JSON
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Lỗi khi lưu JSON: {str(e)}")
        return False

def load_from_json(filename):
    """
    Đọc dữ liệu từ file JSON
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return None
    except json.JSONDecodeError:
        print(f"Lỗi định dạng JSON trong file: {filename}")
        return None
    except Exception as e:
        print(f"Lỗi khi đọc JSON: {str(e)}")
        return None

# Test xử lý JSON
print("\nTest xử lý JSON:")
data = {
    "name": "An",
    "age": 25,
    "skills": ["Python", "FastAPI", "Docker"],
    "created_at": datetime.now().isoformat()
}
save_to_json(data, "user.json")
print(load_from_json("user.json"))

# TODO: Xử lý file với Path
def process_files(directory):
    """
    Xử lý tất cả file trong thư mục
    """
    try:
        path = Path(directory)
        if not path.exists():
            print(f"Thư mục không tồn tại: {directory}")
            return
        
        for file_path in path.glob("**/*"):
            if file_path.is_file():
                print(f"File: {file_path}")
                print(f"Kích thước: {file_path.stat().st_size} bytes")
                print(f"Thời gian sửa đổi: {datetime.fromtimestamp(file_path.stat().st_mtime)}")
                print("-" * 50)
    
    except Exception as e:
        print(f"Lỗi khi xử lý thư mục: {str(e)}")

# Test xử lý file với Path
print("\nTest xử lý file với Path:")
process_files(".")

# TODO: Xử lý file binary
def copy_binary_file(source, destination):
    """
    Sao chép file binary
    """
    try:
        with open(source, 'rb') as src, open(destination, 'wb') as dst:
            while True:
                chunk = src.read(8192)  # Đọc 8KB mỗi lần
                if not chunk:
                    break
                dst.write(chunk)
        return True
    except Exception as e:
        print(f"Lỗi khi sao chép file: {str(e)}")
        return False

# Test sao chép file binary
print("\nTest sao chép file binary:")
copy_binary_file("test.txt", "test_copy.txt")
print("Đã sao chép file")

# TODO: Xử lý file với context manager tùy chỉnh
class FileHandler:
    """
    Context manager tùy chỉnh để xử lý file
    """
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Lỗi khi xử lý file: {exc_val}")
            return True

# Test FileHandler
print("\nTest FileHandler:")
with FileHandler("test.txt", 'r') as f:
    print(f.read())

"""
Bài tập về nhà:
1. Tạo một hệ thống backup file tự động
2. Tạo một chương trình đọc/ghi file CSV
3. Tạo một hệ thống quản lý log file
4. Tạo một chương trình nén/giải nén file
5. Tạo một hệ thống đồng bộ hóa file giữa các thư mục
""" 
"""
File Handling in Python
Xử Lý File trong Python

This module demonstrates various file handling operations in Python.
Module này minh họa các thao tác xử lý file khác nhau trong Python.
"""

def demonstrate_text_file_operations():
    """
    Demonstrate basic text file operations
    Minh họa các thao tác cơ bản với file văn bản
    """
    # Writing to a file / Ghi vào file
    print("\nWriting to a file / Ghi vào file:")
    with open("example.txt", "w", encoding="utf-8") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")
        file.write("Xin chào, Thế giới!\n")
    
    # Reading from a file / Đọc từ file
    print("\nReading from a file / Đọc từ file:")
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("File content / Nội dung file:")
        print(content)
    
    # Reading line by line / Đọc từng dòng
    print("\nReading line by line / Đọc từng dòng:")
    with open("example.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(f"Line: {line.strip()}")

def demonstrate_binary_file_operations():
    """
    Demonstrate binary file operations
    Minh họa các thao tác với file nhị phân
    """
    # Writing binary data / Ghi dữ liệu nhị phân
    print("\nWriting binary data / Ghi dữ liệu nhị phân:")
    with open("binary.bin", "wb") as file:
        file.write(bytes([65, 66, 67]))  # ABC in ASCII
    
    # Reading binary data / Đọc dữ liệu nhị phân
    print("\nReading binary data / Đọc dữ liệu nhị phân:")
    with open("binary.bin", "rb") as file:
        data = file.read()
        print(f"Binary data: {data}")
        print(f"ASCII: {data.decode('ascii')}")

def demonstrate_file_operations():
    """
    Demonstrate various file operations
    Minh họa các thao tác file khác nhau
    """
    import os
    
    # File information / Thông tin file
    print("\nFile information / Thông tin file:")
    print(f"Current directory: {os.getcwd()}")
    
    # List files / Liệt kê file
    print("\nList files / Liệt kê file:")
    for file in os.listdir():
        if file.endswith(".txt") or file.endswith(".bin"):
            print(f"File: {file}")
            print(f"Size: {os.path.getsize(file)} bytes")
    
    # File operations / Thao tác file
    print("\nFile operations / Thao tác file:")
    # Rename file / Đổi tên file
    os.rename("example.txt", "renamed.txt")
    print("File renamed / Đã đổi tên file")
    
    # Remove file / Xóa file
    os.remove("renamed.txt")
    print("File removed / Đã xóa file")
    
    os.remove("binary.bin")
    print("Binary file removed / Đã xóa file nhị phân")

def demonstrate_csv_operations():
    """
    Demonstrate CSV file operations
    Minh họa các thao tác với file CSV
    """
    import csv
    
    # Writing CSV / Ghi file CSV
    print("\nWriting CSV / Ghi file CSV:")
    with open("data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["John", 25, "New York"])
        writer.writerow(["Alice", 30, "London"])
    
    # Reading CSV / Đọc file CSV
    print("\nReading CSV / Đọc file CSV:")
    with open("data.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    
    # Clean up / Dọn dẹp
    os.remove("data.csv")

if __name__ == "__main__":
    print("=== Text File Operations / Thao Tác File Văn Bản ===")
    demonstrate_text_file_operations()
    
    print("\n=== Binary File Operations / Thao Tác File Nhị Phân ===")
    demonstrate_binary_file_operations()
    
    print("\n=== File Operations / Thao Tác File ===")
    demonstrate_file_operations()
    
    print("\n=== CSV Operations / Thao Tác CSV ===")
    demonstrate_csv_operations() 
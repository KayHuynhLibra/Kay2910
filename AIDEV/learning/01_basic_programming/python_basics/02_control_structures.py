"""
Control Structures in Python
Cấu Trúc Điều Khiển trong Python

This module demonstrates various control structures in Python.
Module này minh họa các cấu trúc điều khiển khác nhau trong Python.
"""

def demonstrate_if_else():
    """
    Demonstrate if-else statements
    Minh họa câu lệnh if-else
    """
    age = 18
    
    # Simple if statement / Câu lệnh if đơn giản
    if age >= 18:
        print("Adult / Người lớn")
    else:
        print("Minor / Vị thành niên")
    
    # if-elif-else chain / Chuỗi if-elif-else
    score = 85
    if score >= 90:
        print("Grade A / Điểm A")
    elif score >= 80:
        print("Grade B / Điểm B")
    elif score >= 70:
        print("Grade C / Điểm C")
    else:
        print("Grade F / Điểm F")

def demonstrate_loops():
    """
    Demonstrate different types of loops
    Minh họa các loại vòng lặp khác nhau
    """
    # For loop with range / Vòng lặp for với range
    print("\nFor loop with range / Vòng lặp for với range:")
    for i in range(5):
        print(f"Count: {i}")
    
    # For loop with list / Vòng lặp for với list
    print("\nFor loop with list / Vòng lặp for với list:")
    fruits = ["apple", "banana", "orange"]
    for fruit in fruits:
        print(f"Fruit: {fruit}")
    
    # While loop / Vòng lặp while
    print("\nWhile loop / Vòng lặp while:")
    count = 0
    while count < 3:
        print(f"Count: {count}")
        count += 1

def demonstrate_break_continue():
    """
    Demonstrate break and continue statements
    Minh họa câu lệnh break và continue
    """
    # Break example / Ví dụ về break
    print("\nBreak example / Ví dụ về break:")
    for i in range(10):
        if i == 5:
            break
        print(f"Number: {i}")
    
    # Continue example / Ví dụ về continue
    print("\nContinue example / Ví dụ về continue:")
    for i in range(5):
        if i == 2:
            continue
        print(f"Number: {i}")

def demonstrate_try_except():
    """
    Demonstrate exception handling
    Minh họa xử lý ngoại lệ
    """
    # Try-except example / Ví dụ try-except
    print("\nTry-except example / Ví dụ try-except:")
    try:
        number = int("abc")
    except ValueError:
        print("Invalid number / Số không hợp lệ")
    
    # Try-except-else-finally example / Ví dụ try-except-else-finally
    print("\nTry-except-else-finally example / Ví dụ try-except-else-finally:")
    try:
        number = int("123")
    except ValueError:
        print("Invalid number / Số không hợp lệ")
    else:
        print("Valid number / Số hợp lệ")
    finally:
        print("This always executes / Điều này luôn được thực thi")

if __name__ == "__main__":
    print("=== If-Else Examples / Ví dụ If-Else ===")
    demonstrate_if_else()
    
    print("\n=== Loop Examples / Ví dụ Vòng Lặp ===")
    demonstrate_loops()
    
    print("\n=== Break and Continue Examples / Ví dụ Break và Continue ===")
    demonstrate_break_continue()
    
    print("\n=== Exception Handling Examples / Ví dụ Xử Lý Ngoại Lệ ===")
    demonstrate_try_except() 
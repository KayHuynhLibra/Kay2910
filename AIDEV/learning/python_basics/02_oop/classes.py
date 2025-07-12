"""
Class và Object trong Python

Mục tiêu:
- Hiểu về cách định nghĩa class
- Biết cách tạo và sử dụng object
- Hiểu về constructor và destructor
- Biết cách sử dụng các phương thức đặc biệt
"""

# 1. Class cơ bản
class Person:
    """Class đại diện cho một người"""
    
    def __init__(self, name, age):
        """Constructor"""
        self.name = name
        self.age = age
    
    def greet(self):
        """Phương thức chào hỏi"""
        return f"Xin chào, tôi là {self.name}, {self.age} tuổi"
    
    def __str__(self):
        """Phương thức đặc biệt để in object"""
        return f"Person(name={self.name}, age={self.age})"

# 2. Class với thuộc tính private
class BankAccount:
    """Class đại diện cho tài khoản ngân hàng"""
    
    def __init__(self, account_number, balance=0):
        """Constructor"""
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        """Nạp tiền vào tài khoản"""
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Rút tiền từ tài khoản"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        """Lấy số dư tài khoản"""
        return self.__balance
    
    def __str__(self):
        """Phương thức đặc biệt để in object"""
        return f"BankAccount(account_number={self.__account_number}, balance={self.__balance})"

# 3. Class với thuộc tính class
class Student:
    """Class đại diện cho sinh viên"""
    
    # Class attribute
    school = "University of Technology"
    
    def __init__(self, name, student_id):
        """Constructor"""
        self.name = name  # Instance attribute
        self.student_id = student_id  # Instance attribute
    
    @classmethod
    def change_school(cls, new_school):
        """Phương thức class để thay đổi tên trường"""
        cls.school = new_school
    
    @staticmethod
    def is_valid_student_id(student_id):
        """Phương thức static để kiểm tra mã sinh viên"""
        return len(student_id) == 8
    
    def __str__(self):
        """Phương thức đặc biệt để in object"""
        return f"Student(name={self.name}, student_id={self.student_id}, school={self.school})"

# 4. Class với property
class Rectangle:
    """Class đại diện cho hình chữ nhật"""
    
    def __init__(self, width, height):
        """Constructor"""
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """Property để lấy chiều rộng"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Property để set chiều rộng"""
        if value > 0:
            self.__width = value
        else:
            raise ValueError("Chiều rộng phải lớn hơn 0")
    
    @property
    def height(self):
        """Property để lấy chiều cao"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Property để set chiều cao"""
        if value > 0:
            self.__height = value
        else:
            raise ValueError("Chiều cao phải lớn hơn 0")
    
    @property
    def area(self):
        """Property để tính diện tích"""
        return self.__width * self.__height
    
    def __str__(self):
        """Phương thức đặc biệt để in object"""
        return f"Rectangle(width={self.__width}, height={self.__height}, area={self.area})"

# 5. Bài tập thực hành
def practice_classes():
    """
    Bài tập:
    1. Tạo class Car với các thuộc tính và phương thức cơ bản
    2. Tạo class Employee với các thuộc tính private và public
    3. Tạo class Book với các property
    4. Tạo class Calculator với các phương thức static
    5. Tạo class Animal với các phương thức đặc biệt
    """
    # Viết code của bạn ở đây
    pass

if __name__ == "__main__":
    # Chạy các ví dụ
    print("1. Class Person:")
    person = Person("John", 25)
    print(person.greet())
    print(person)
    
    print("\n2. Class BankAccount:")
    account = BankAccount("123456789", 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f"Số dư: {account.get_balance()}")
    print(account)
    
    print("\n3. Class Student:")
    student = Student("Alice", "12345678")
    print(student)
    Student.change_school("New University")
    print(f"Mã sinh viên hợp lệ: {Student.is_valid_student_id('12345678')}")
    
    print("\n4. Class Rectangle:")
    rect = Rectangle(5, 3)
    print(rect)
    rect.width = 6
    rect.height = 4
    print(f"Diện tích: {rect.area}")
    
    print("\n5. Bài tập thực hành:")
    practice_classes() 
"""
Đóng Gói trong Python

Mục tiêu:
- Hiểu về cách đóng gói dữ liệu
- Biết cách sử dụng access modifiers
- Hiểu về getters và setters
- Biết cách sử dụng property
"""

# 1. Đóng gói cơ bản
class BankAccount:
    """Class đại diện cho tài khoản ngân hàng"""
    
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute
    
    def get_balance(self):
        """Getter cho balance"""
        return self.__balance
    
    def set_balance(self, amount):
        """Setter cho balance"""
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Số dư không thể âm")
    
    def get_account_number(self):
        """Getter cho account_number"""
        return self.__account_number

# 2. Sử dụng property
class Person:
    """Class đại diện cho một người"""
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        """Property cho name"""
        return self.__name
    
    @name.setter
    def name(self, value):
        """Setter cho name"""
        if not value:
            raise ValueError("Tên không thể rỗng")
        self.__name = value
    
    @property
    def age(self):
        """Property cho age"""
        return self.__age
    
    @age.setter
    def age(self, value):
        """Setter cho age"""
        if value < 0:
            raise ValueError("Tuổi không thể âm")
        self.__age = value

# 3. Đóng gói với protected attributes
class Animal:
    """Class cơ sở cho các loài động vật"""
    
    def __init__(self, name, species):
        self._name = name  # Protected attribute
        self._species = species  # Protected attribute
    
    def _make_sound(self):
        """Protected method"""
        return "Some sound"
    
    def get_info(self):
        """Public method"""
        return f"{self._name} is a {self._species}"

# 4. Đóng gói với class methods
class Student:
    """Class đại diện cho sinh viên"""
    
    __school = "University of Technology"  # Private class attribute
    
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
    
    @classmethod
    def get_school(cls):
        """Class method để lấy tên trường"""
        return cls.__school
    
    @classmethod
    def set_school(cls, new_school):
        """Class method để thay đổi tên trường"""
        cls.__school = new_school

# 5. Đóng gói với static methods
class MathOperations:
    """Class chứa các phép toán toán học"""
    
    __PI = 3.14159  # Private class attribute
    
    @staticmethod
    def get_pi():
        """Static method để lấy giá trị PI"""
        return MathOperations.__PI
    
    @staticmethod
    def calculate_circle_area(radius):
        """Static method để tính diện tích hình tròn"""
        return MathOperations.__PI * radius ** 2

# 6. Bài tập thực hành
def practice_encapsulation():
    """
    Bài tập:
    1. Tạo class Product với các thuộc tính private và public
    2. Tạo class Employee với các property
    3. Tạo class Bank với các class methods
    4. Tạo class Calculator với các static methods
    5. Tạo class Library với các protected methods
    """
    # Viết code của bạn ở đây
    pass

if __name__ == "__main__":
    # Chạy các ví dụ
    print("1. Đóng gói cơ bản:")
    account = BankAccount("123456789", 1000)
    print(f"Số dư: {account.get_balance()}")
    account.set_balance(2000)
    print(f"Số dư mới: {account.get_balance()}")
    
    print("\n2. Sử dụng property:")
    person = Person("John", 25)
    print(f"Tên: {person.name}")
    print(f"Tuổi: {person.age}")
    person.name = "Jane"
    person.age = 30
    print(f"Tên mới: {person.name}")
    print(f"Tuổi mới: {person.age}")
    
    print("\n3. Đóng gói với protected attributes:")
    animal = Animal("Buddy", "Dog")
    print(animal.get_info())
    
    print("\n4. Đóng gói với class methods:")
    print(f"Trường học: {Student.get_school()}")
    Student.set_school("New University")
    print(f"Trường học mới: {Student.get_school()}")
    
    print("\n5. Đóng gói với static methods:")
    print(f"PI: {MathOperations.get_pi()}")
    print(f"Diện tích hình tròn: {MathOperations.calculate_circle_area(5)}")
    
    print("\n6. Bài tập thực hành:")
    practice_encapsulation() 
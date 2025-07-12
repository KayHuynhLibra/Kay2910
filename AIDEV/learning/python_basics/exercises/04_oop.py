"""
Bài tập 4: Lập Trình Hướng Đối Tượng

Mục tiêu:
- Hiểu các khái niệm cơ bản của OOP
- Thực hành với class và object
- Sử dụng inheritance và polymorphism
"""

# TODO: Class cơ bản
class Person:
    """
    Class đại diện cho một người
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Xin chào, tôi là {self.name}, {self.age} tuổi."

# Test class Person
print("Test class Person:")
person = Person("An", 25)
print(person.introduce())

# TODO: Inheritance
class Student(Person):
    """
    Class Student kế thừa từ Person
    """
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def introduce(self):
        return f"{super().introduce()} Tôi là sinh viên với mã số {self.student_id}."

# Test class Student
print("\nTest class Student:")
student = Student("Bình", 20, "SV001")
print(student.introduce())

# TODO: Encapsulation
class BankAccount:
    """
    Class đại diện cho tài khoản ngân hàng
    """
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

# Test class BankAccount
print("\nTest class BankAccount:")
account = BankAccount("ACC001", 1000)
print(f"Số dư ban đầu: {account.balance}")
account.deposit(500)
print(f"Số dư sau khi gửi: {account.balance}")
account.withdraw(200)
print(f"Số dư sau khi rút: {account.balance}")

# TODO: Polymorphism
class Animal:
    """
    Class cơ sở cho các loài động vật
    """
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Gâu gâu!"

class Cat(Animal):
    def make_sound(self):
        return "Meo meo!"

# Test polymorphism
print("\nTest polymorphism:")
animals = [Dog(), Cat()]
for animal in animals:
    print(f"Âm thanh: {animal.make_sound()}")

# TODO: Static method và class method
class MathUtils:
    """
    Class chứa các phương thức tiện ích toán học
    """
    PI = 3.14159
    
    @staticmethod
    def square(x):
        return x * x
    
    @classmethod
    def circle_area(cls, radius):
        return cls.PI * cls.square(radius)

# Test static method và class method
print("\nTest static method và class method:")
print(f"Bình phương của 5: {MathUtils.square(5)}")
print(f"Diện tích hình tròn bán kính 3: {MathUtils.circle_area(3)}")

"""
Bài tập về nhà:
1. Tạo một hệ thống quản lý thư viện với các class Book, Member, và Library
2. Tạo một hệ thống quản lý nhân viên với các class Employee, Manager, và Department
3. Tạo một hệ thống quản lý đơn hàng với các class Product, Order, và Customer
4. Tạo một hệ thống quản lý trường học với các class Teacher, Student, và Course
5. Tạo một hệ thống quản lý ngân hàng với các class Account, Transaction, và Bank
""" 
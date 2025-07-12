"""
Kế Thừa trong Python

Mục tiêu:
- Hiểu về cách sử dụng kế thừa
- Biết cách override phương thức
- Hiểu về đa kế thừa
- Biết cách sử dụng super()
"""

# 1. Kế thừa đơn
class Animal:
    """Class cơ sở cho các loài động vật"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        """Phương thức tạo âm thanh"""
        return "Some sound"
    
    def __str__(self):
        return f"Animal(name={self.name}, species={self.species})"

class Dog(Animal):
    """Class con kế thừa từ Animal"""
    
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        """Override phương thức make_sound"""
        return "Woof!"
    
    def __str__(self):
        return f"Dog(name={self.name}, breed={self.breed})"

# 2. Kế thừa nhiều cấp
class WorkingDog(Dog):
    """Class con kế thừa từ Dog"""
    
    def __init__(self, name, breed, job):
        super().__init__(name, breed)
        self.job = job
    
    def work(self):
        """Phương thức làm việc"""
        return f"{self.name} is working as a {self.job}"
    
    def __str__(self):
        return f"WorkingDog(name={self.name}, breed={self.breed}, job={self.job})"

# 3. Đa kế thừa
class Flying:
    """Mixin class cho khả năng bay"""
    
    def fly(self):
        return "Flying high!"

class Swimming:
    """Mixin class cho khả năng bơi"""
    
    def swim(self):
        return "Swimming in water!"

class Duck(Animal, Flying, Swimming):
    """Class con kế thừa từ nhiều class"""
    
    def __init__(self, name):
        super().__init__(name, species="Duck")
    
    def make_sound(self):
        return "Quack!"
    
    def __str__(self):
        return f"Duck(name={self.name})"

# 4. Abstract Base Class
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract class cho các hình học"""
    
    @abstractmethod
    def area(self):
        """Tính diện tích"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Tính chu vi"""
        pass

class Circle(Shape):
    """Class con kế thừa từ Shape"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Tính diện tích hình tròn"""
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        """Tính chu vi hình tròn"""
        return 2 * 3.14 * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius})"

# 5. Bài tập thực hành
def practice_inheritance():
    """
    Bài tập:
    1. Tạo class Vehicle và các class con Car, Motorcycle
    2. Tạo class Employee và các class con Manager, Developer
    3. Tạo class Shape và các class con Rectangle, Triangle
    4. Tạo class Animal và các class con Bird, Fish
    5. Tạo class Product và các class con Book, Electronics
    """
    # Viết code của bạn ở đây
    pass

if __name__ == "__main__":
    # Chạy các ví dụ
    print("1. Kế thừa đơn:")
    dog = Dog("Buddy", "Golden Retriever")
    print(dog)
    print(dog.make_sound())
    
    print("\n2. Kế thừa nhiều cấp:")
    working_dog = WorkingDog("Max", "German Shepherd", "Police Dog")
    print(working_dog)
    print(working_dog.work())
    
    print("\n3. Đa kế thừa:")
    duck = Duck("Donald")
    print(duck)
    print(duck.make_sound())
    print(duck.fly())
    print(duck.swim())
    
    print("\n4. Abstract Base Class:")
    circle = Circle(5)
    print(circle)
    print(f"Diện tích: {circle.area()}")
    print(f"Chu vi: {circle.perimeter()}")
    
    print("\n5. Bài tập thực hành:")
    practice_inheritance() 
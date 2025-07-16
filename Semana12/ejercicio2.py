import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * (self.radius **2)
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side
    
    def calculate_area(self):
        return self.side ** 2
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def calculate_area(self):
        return self.width * self.height

circle = Circle(radius=5)

print(f"Circle with radius 5:")
print(f"Perimeter: {circle.calculate_perimeter()}")
print(f"Area: {circle.calculate_area()}")

square = Square(side=4)

print(f"\nSquare with side 4:")
print(f"Perimeter: {square.calculate_perimeter()}")
print(f"Area: {square.calculate_area()}")

rectangle = Rectangle(width=6, height=3)

print(f"\nRectangle with width 6 and height 3:")
print(f"Perimeter: {rectangle.calculate_perimeter()}")
print(f"Area: {rectangle.calculate_area()}")
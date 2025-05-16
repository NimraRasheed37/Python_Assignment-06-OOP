# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

# Creating an abstract class
class Shape(ABC):
    
    # abstract method
    @abstractmethod
    def area(self):
        pass

# child class and implement the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create an object of Rectangle
rect = Rectangle(5, 4)
print("Area of Rectangle:", rect.area())  




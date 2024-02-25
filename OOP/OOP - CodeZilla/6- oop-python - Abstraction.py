from abc import ABC, abstractmethod


# Using abstractmethod ( area() - perimeter() ) => all child classes must follow the pattern and implement function called area() && perimeter() however how their logic is !

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return (self.__length + self.__width) * 2


square = Square(10)
print(f"Square Area = {square.area()} and perimeter = {square.perimeter()}")

print('***************************************')

rect = Rectangle(5,3)
print(f"Rectangle Area = {rect.area()} and perimeter = {rect.perimeter()}")

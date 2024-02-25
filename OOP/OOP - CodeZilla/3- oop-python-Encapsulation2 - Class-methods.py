from datetime import date

class Student:
    
    # Class Attributes
    no_of_students = 0

    # Class Methods [Access only to class attributes]
    # Usage: Initialize many objects with a different way / parameter
    #   Act as an additional constructors
    # cls => Class Convention
    @classmethod
    def initFromBirthYear(cls, name, birthYear):
          return cls(name, date.today().year - birthYear)


    # Instance Attributes
    def __init__(self, name, age= 0):
            self.__name = name
            self.__age = age
            Student.no_of_students += 1
    
    # Instance Methods
    def describe(self):
          print(f"My name is {self.__name} and my age is {self.__age}")


student_1 = Student("Islam", 20)
student_2 = Student.initFromBirthYear("Ahmed", 1995)

print(student_1.describe())
print(student_2.describe())

print("---------------------------------------------------------------------")

class Pizza:
    def __init__(self, ingredients) -> None:
            self.ingredients = ingredients
    
    @classmethod
    def vegeterian(cls):
          return cls(['mushrooms', 'olives', 'onion'])
    
    @classmethod
    def margherita(cls):
          return cls(['mozarella', 'saude'])
    

    # Instance Method
    # Polymorphism -- Override: __str__ Function 
    def __str__(self):
          return f"Pizza Ingredients are {self.ingredients}"
          
    

pizza_1 = Pizza(['tomatoes', 'olives'])     
pizza_2 = Pizza.vegeterian()
pizza_3 = Pizza.margherita()

print(pizza_1, pizza_2, pizza_3)   
# <__main__.Pizza object at 0x000001F4AE7D1490> <__main__.Pizza object at 0x000001F4AE7D14C0> <__main__.Pizza object at 0x000001F4AE7D14F0>


# dunder (Double Under-Score) function sucg as __init__
print(pizza_1.__str__) 
print(pizza_2.__str__)
print(pizza_3.__str__)


        

    


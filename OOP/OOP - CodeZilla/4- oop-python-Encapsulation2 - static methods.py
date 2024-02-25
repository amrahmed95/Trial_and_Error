# Static Methods
# ------------------
# Utility Functions (Helper Method) => a function inside a class for a quick specific task 
# Type of method by which we can't change in the class or object states
    # => Don't take any parameter as "Self" or "cls"
class Math:

    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def add5(num):
        return num + 5
    
    @staticmethod
    def add10(num):
        return num + 10
    
    @staticmethod
    def PI():
        return 3.14
    
x = Math.add(5,10)
y = Math.add5(x)
z = Math.add10(y)
print(x,y,z)



print("---------------------------------------------------------------------")

class Pizza:
    def __init__(self, radius, ingredients):
            self.radius = radius
            self.ingredients = ingredients
    
    # Instance Method
    # Polymorphism -- Override: __str__ Function 
    def __str__(self):
          return f"Pizza Ingredients are {self.ingredients}"

    # Usage for static method
    # -----------------------------------------------      
    def area(self):
         return Pizza.circla_area(self.radius)  
    
    @staticmethod
    def circla_area(r):
         return r ** 2 ** Math.PI()
    # -----------------------------------------------
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
          
    
p = Pizza(6, ['Mozzarella', 'tomatoes'])
print(p.area())
print(p.circla_area(4))
print(p.circla_area(10))


print("---------------------------------------------------------------------")

class Dates:
    def __init__(self, date):
          self.__date = date

    def getDate(self):
         return self.__date
    
    @staticmethod
    def toDashDate(date):
         return date.replace('/', '-')
    

date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if (date.getDate() == dateWithDash):
     print("Equal")
else:
    print("Not Equal")


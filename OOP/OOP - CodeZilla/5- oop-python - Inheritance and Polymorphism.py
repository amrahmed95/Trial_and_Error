from datetime import date

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return "My name is {} and My age is {}".format(self.name, self.age)
    
    @classmethod
    def initFromBirthDate(cls, name, birthYear, extra):
        return cls(name, date.today().year - birthYear, extra)

class Man(Person):    
    # Class Attributes
    gender = 'Male'
    no_of_men = 0


    def __init__(self, name, age, voice):
        #self.name = name
        #self.age = age
        super().__init__(name, age)
        self.voice = voice
        Man.no_of_men += 1

    # Override function
    def display(self):
        string = super().display()
        return string + f", voice is {self.voice}, gender is {self.gender}"    
    
    

class Woman(Person):    
    # Class Attributes
    gender = 'Female'
    no_of_women = 0

    def __init__(self, name, age, hair):
        #self.name = name
        #self.age = age
        super().__init__(name, age)
        self.hair = hair
        Woman.no_of_women += 1

    # Override function
    def display(self):
        string = super().display()
        return string + f", hair is {self.hair}, gender is {self.gender}"



man = Man("Islam", 30, "hard")
print(man.display())
print(Man.no_of_men)


print('------------------------------------------------')
      
woman = Woman("Mona", 23,"Curly")
print(woman.display())
print(woman.no_of_women)

print('------------------------------------------------')

# Inheritance for class method

man = Man.initFromBirthDate("Amr",1995,"hard")
print(man.display())

print('------------------------------------------------')

woman = Woman.initFromBirthDate("Somaya",1980,"cirly")
print(woman.display())

print('------------------------------------------------')

print(isinstance(woman, Woman)) #True
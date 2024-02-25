class Student:
    # Class Attributes (shared among all objects of the class - must be initialized with a value)
        # Can be accessed directly from class and from the objects of the class
    no_of_students = 0

    # Object / Instance Attributes
    # These are public attributes
    # __ to make attribute private (Only can be valued by setter method)
    def __init__(self, name, age = 0, *courses):
        self.__name = name          # Private attribute
        self.__age = age            # Private attribute
        self.courses = courses      # Public attribute
        Student.no_of_students += 1

    def getName(self):
        return self.__name
    
    def setName(self, new_name):
        self.__name = new_name
    
    def getAge(self):
        return self.__age
    
    def setAge(self, new_age):
        self.__age = new_age
        

    # Instance Methods ('self' keyword to have access to the instance attributes)
    def describe(self):
        print(f"My Name is {self.__name} and my age is {self.__age}")
        #print("My name is {} and my age is {}".format(self.name, self.age))

    def is_old(self, num):
        if (self.__age <= num):
            print("student is not old")
        else:
            print("Student is old")
        

student_1 = Student("Islam", 40, ['Science'])

print("Get Name: ", student_1.getName())

student_1.setName("Amr")
print("Name after setName method: ", student_1.getName())

student_1.name = "Ahmed"
print('False set to ahmed: ', student_1.getName())  # Print 'Amr' not 'Ahmed' As Name Attribute is private

student_1.setAge(50)
print(student_1.describe())


#print(student_1.__name) # AttributeError: 'Student' object has no attribute '__name'. Did you mean: 'name'?


class Student:
    # Class Attributes (shared among all objects of the class - must be initialized with a value)
        # Can be accessed directly from class and from the objects of the class
    no_of_students = 0

    # Object / Instance Attributes
    # __init__ => Constructor of Object
    def __init__(self, name, age = 0, *courses):
        self.name = name
        self.age = age
        self.courses = courses
        Student.no_of_students += 1

    # Instance Methods ('self' keyword to have access to the instance attributes)
    def describe(self):
        print(f"My Name is {self.name} and my age is {self.age}")
        #print("My name is {} and my age is {}".format(self.name, self.age))

    def is_old(self, num):
        if (self.age <= num):
            print("student is not old")
        else:
            print("Student is old")
        

student_1 = Student("Islam")
student_2 = Student("Islam", 30, ['CS','Math'])


print(id(student_1), id(student_2)) # Different Momory Location
print(student_1, student_2)

print(student_1.name, student_1.age)

student_1.name = "Ahmed"
student_1.age = 50

print(student_1.name, student_1.age)

print(Student.no_of_students)
print(student_1.no_of_students)

print(student_1.describe())

print(student_1.is_old(40))

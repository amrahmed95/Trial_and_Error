# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# List all students' grades
ahmed_grade = 17.5
mustafa_grade = 16
ali_grade = 20
omnia_grade = 18.3
marwa_grade = 15.5

# Using lists to represent data
students_grades = [17.5, 16, 20, 18.3, 15.5]
print(students_grades)

# Subsetting a list 
print(students_grades[0])
print(students_grades[-1])

# Manipulate lists
students_grades[2] = 19.5
print(students_grades)
print(students_grades[3] - 2)


# Slicing a list
print(students_grades[0:3])
print(students_grades[0:])
print(students_grades[1:4])

# List functions
students_grades.append(19.2)
students_grades.remove(students_grades[1])
print(students_grades)

# Using dictionaries to represent data
student_dict = {'ahmed': 17.5, 'mustafa':16, 'ali':20, 'omnia':18.3, 'marwa':15.5}
print(student_dict)

# Subsetting a dictionary 
print(student_dict['ali'])

# Manipulate a dictionary
student_dict['ali'] = 19
print(student_dict)


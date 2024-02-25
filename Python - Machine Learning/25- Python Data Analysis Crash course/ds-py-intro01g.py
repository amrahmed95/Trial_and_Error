# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 02:05:06 2020

@author: musta
"""

# Define an Object
class Students():

    def __int__(self, name, age):
        self.name = name
        self.age = age
        
    def DescibeYourSelf(self):
        print('I am ', self.name, ' and I am ', self.age, ' years old!')
        

# Initiate an Object
my_student = Students()

# Object Attributes
my_student.name = 'Mustafa'
my_student.age = 33

# Object Method
my_student.DescibeYourSelf()
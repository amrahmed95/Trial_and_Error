# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:57:45 2020

@author: musta
"""

x = 4
y = 12

# Numerical Comparison Operators
print('x > y: ', x > y)
print('x < y: ', x < y)
print('x == y: ', x == y)
print('x >= y: ', x >= y)
print('x != y: ', x != y)
print('x <= y: ', x <= y)


# Logical Operators
print('x > y and x == y:', x > y and x == y)
print('x < y and x != y:', x < y and x != y)
print('x < y or x == y:', x < y or x == y)
print('not x < y: ', not x < y)


# Program to check if a number is Positive or Negative
z = float(input("Enter a number: "))

if z > 0:
    print('Positive')
elif z == 0:
    print('Zero')
else:
    print('Negative')
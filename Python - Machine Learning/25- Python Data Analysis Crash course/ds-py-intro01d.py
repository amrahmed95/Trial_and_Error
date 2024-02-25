# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:02:35 2020

@author: musta
"""

# Strings Manipulation
word = 'Python'
print(word[0])
print(word[0:3])

for char in word:
    print(char, end = ' ')

# For Loops
for x in range(0,10):
    print(x)

for x in range(0,10,2):
    print(x)

# Iterating a List
num = [1,2,3,4,5]

for i in num:
    print(i, end = ' ')

# While Loops
x = 1
while x < 5:
    print(x, end = ' ')
    x += 1 # x = x + 1
    

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 06:44:39 2020

@author: musta
"""

## Built-in Functions
num = [12.0, 4.8, 3.5, 17.2, 9.1, 55.0, 12.2]
print(min(num))
print(max(num))
print(abs(num[1]))
print(len(num))
print(round(num[3]))
my_str = "Hello"
print(my_str.upper())
print(my_str.lower())

## Modules (math, os)
import math
print(math.pi)
print(math.sqrt(16))
print(math.sin(90))
print(math.isnan(20))
import os
print(os.getcwd())

## Your Own Functions
def say_hello():
    print("Hello, Everybody!")
    
say_hello()

def say_special_hello(name):
    print("Hello, ", name)
    
say_special_hello('Mustafa')

def add_func(num1, num2):
    print("num1 + num2 = ", num1 + num2)
    
add_func(6, 3)

## Recursive Functions
def fact(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))
print(fact(5))
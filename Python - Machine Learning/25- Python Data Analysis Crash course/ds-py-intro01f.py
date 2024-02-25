# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 01:59:27 2020

@author: musta
"""
# Dealing with files

# Open a File
f = open('myfile.txt', 'w')
print(type(f))

# Read a File
f = open('myfile.txt', 'r')

# Write to a File
f.write('This is my first txt file \n')
f.write('And this is my second line')

# Read a File
f.read()

# Close a File
f.close()
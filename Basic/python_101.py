# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:18:41 2022

@author: TCBALGUL
"""

a="Hello world"
#del a
#String methods 
#len
len(a);

#toUpper and toLower
a.lower()
a.upper()
a.islower()
a.isupper()

#replace
a.replace('e', 'o')

#strip to trim spaces
a.strip()

#dir to see the methods and attr
dir(a)
a.capitalize() #first word 
a.title() #every word

#substrings
a[0:5]

#Type transformations
firstNumber = input()
int(firstNumber)
float(firstNumber)
str(firstNumber)

#print
print("Hello", "World", sep="_")
#?print
"_Python_".strip("_")


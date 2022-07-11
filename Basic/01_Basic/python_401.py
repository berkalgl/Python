#object oriented programming

class DataScientist():
    section = ''
    sql = 'Yes'
    experienceInYear = 0
    languages = []
    
DataScientist.section
DataScientist.sql = 'No'

#instantiation
berk = DataScientist()
berk.sql
berk.section
berk.languages.append("Python")

        
#Inheritance
class Employees():
    def __init__(self, firstName, lastName, address):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        
        
#instantiation properties and methods
class DataScientist(Employees):
    languages = ["R", "Python"]
    def __init__(self, languages, section):
        self.languages = languages
        self.section = section
    def AddLanguage(self, language):
        self.languages.append(language)
        
berk = DataScientist()

#Functional Programming in Python
#--------------------------------
#Pure functions
#Sample 1 independency
A=5
def impureSum(b):
    return b + A

def pureSum(a,b):
    return a + b

impureSum(6)
pureSum(4,3)

#Sample 2 deadly
#in oop
class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self.lines)
    
lc = LineCounter('deneme.txt')

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())
#in functional programming
def read(filename):
    with open(filename, 'r') as f:
        return[line for line in f]
    
def count(lines):
    return len(lines)

exampleLines = read('deneme.txt')
linesCount = count(exampleLines)
linesCount

#--------------------
#anonymous functions
def oldSum(a,b):
    return a+b

oldSum(4, 5)

newSum = lambda a,b: a+b
newSum(4, 5)

unorderedList = [('b',3), ('a',8), ('d',12), ('c',1) ]
sorted(unorderedList, key = lambda x: x[1])
#--------------------
#vectorel operations
#OOP
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i]*b[i])

#FP
import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b

#---------------------
#map & filter & reduce
listExample = [1,2,3,4,5,6,7,8,9,10]
list(map(lambda x: x+10, listExample))

list(filter(lambda x: x%2 == 0, listExample))

from functools import reduce
reduce(lambda a,b: a+b, listExample)

#---------------------
#calling a module
import calculationmodule

calculationmodule.calcNewSalary(1000)

import calculationmodule as cm

cm.calcNewSalary(1000)

from calculationmodule import calcNewSalary

calcNewSalary(1000)

calculationmodule.salaries

#errors/ exceptions
a=10
b=0

a/b #ZeroDivisionError

try:
    print(a/b)
except ZeroDivisionError:
    print("Zero Devision Error Occured")
except TypeError:
    print("Type Error Occured")
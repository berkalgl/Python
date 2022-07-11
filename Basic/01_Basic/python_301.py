#Introduction to functions and readability of functions' documentation.
?print

#define
def GetSquare(x):
    print(str(x) + "'s square is " + str(x**2))

getSquare(3)

def Multiply(a,b):
    print(a*b)
    
multiply(3, 2)

#global, local
x = []

def AddElement(y):
    x.append(y)
    
#control structure
#True false
#if else elif
a==b
limit = 5000
income = int(input("Income:"))

if income < limit:
    print("Income is lower than limit")
elif income > limit:
    print("Income is bigger than limit")
else:
    print("Income is equal to limit")

#Loops
#For
students = ["b","a","c"]

for i in students:
    print(i)
    
salaries = [1000,2000,3000,4000,5000,6000]

for salary in salaries:
    print(salary)
    
#Break and continue
for salary in salaries:
    if salary == 3000:
        break
    print(salary)
    
for salary in salaries:
    if salary == 3000:
        continue
    print(salary)
    
#while
count = 1

while count < 10:
    count += 1
    
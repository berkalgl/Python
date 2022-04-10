#docstring
def summer(arg1, arg2):
    """
    This function sum given two args
    Parameters
    __________
    arg1: int, float
    arg2: int, float
        
    Returns
    _________
    
    """
    print(arg1 + arg2)
    
help(summer)


#Functions' Statement and Body Part

def multiplication(a,b):
    c = a*b
    print(c)

listExample = []

def addToList(a,b):
    c = a * b
    listExample.append(c)
    
addToList(1, 2)

multiplication(3, 23) * 3 #nonetype and int 

#conditions
def number_check(number):
    if number > 10:
        print(str(number) + "greater than 10")
    elif number < 10:
        print(str(number) + "less than 10")
    else:
        print("equal to 10")
        
#loops
students = ["John", "Mark", "Venessa", "Mariam"]
for student in students:
    print(student)
    
#question
def alternating(string):
    newString = ""
    newChar = ''
    for idx,value in enumerate(string):
        newChar = string[idx].lower()
        if idx % 2 == 0:
            newChar = string[idx].upper()
        newString += newChar
    print(newString)
        
change_even_indexes("merhaba darling")

#homework
#1 alternating enumerate 
#2 calculate the sum of even or odd numbers in list 
#numbers =[1,2,3,4,5,6]
#choice = "odd"
#total = 0
#n = 0

def sum(numbers, choiceType=0):
    total = 0
    n = 0
    if choiceType == 0:
        total = sum(numbers)
        n = len(numbers)
    elif choiceType == 1 or choiceType == 2: #even
        for number in numbers:
            if not number % 2 and choiceType == 1:
                total += number
                n += 1
            elif number % 2 and choiceType == 2:
                total += number
                n += 1
    else:
        print('not supported')
    
    print(numbers)
    print(total/n)
    

sum([1,2,3,4,5,6,7,8,6,13,15],2)

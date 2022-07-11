# in fp we seperate methods and attributes 
# have an emphasis on simplicity where data and functions are concerned
# because in most functional programming paradigms, we do not have this idea of classes and objects
# clear + understandable
# easy to extend
# easy to maintain
# memory efficient
# dry

# pure functions
# has two rules
# 1 - given the same input, it will always return the same output
# 2 - should not produce any side effects to outside world

def multiply_by2(li):
    return [i * 2 for i in li]

print(multiply_by2([2,4,6]))

# useful functions 
# map(), filter(), zip(), reduce()

# MAP
mylist = [1,2,3]
def multiply_by2_2(item):
    return item * 2

print(list(map(multiply_by2_2, mylist)))# does not modify the mylist like this
multiplied_list = list(map(multiply_by2_2, mylist))
print(multiplied_list)

# FILTER
def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, mylist)))
print(list(filter(lambda x : x % 2 != 0, mylist)))

# ZIP
your_list = [10,20,30]
their_list = [5,4,3]
print(list(zip(mylist,your_list,their_list))) # returns tuple

# REDUCE
from functools import reduce
print(reduce(lambda acc,item : acc + item , mylist, 0))

# Exercise
#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

print(list(map(lambda x : x.capitalize(), my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(lambda x: x > 50, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
print(reduce(lambda acc, i : acc + i, my_numbers + scores, 0))

#lambda expressions
new_list = list(map(lambda x : x*x, [5,6,7]))

# List Sorting
a = [(0,2), (4,3), (10,-1),(9,9)]
a.sort(key=lambda x: x[1])
print(a)

# List, Set, Dictionary comprehensions
my_list = [char for char in 'hello']
my_list2 = [num * 2 for num in range(100)]

my_set = {char for char in 'hello'}

simple_dict = {'a': 1, 'b': 2}

my_dict = {key: value*2 for key,value in simple_dict.items()}

#exercise
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([value for value in some_list if some_list.count(value) > 1])
print(duplicates)
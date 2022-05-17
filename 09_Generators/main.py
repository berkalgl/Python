# Generators are available in Python and allow us to generate 
# a sequence of values over time

# a generator is a special type of thing in Python that allows us to 
# use a special keyword called yield and it can pause and resume functions


# range is a generator

# range(100)
# list(range(100))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result

#print(make_list(100))

# range does not create a list in the memory
# print(list(range(10)))
# a more efficient way is to use a generator and actually generate
# these one at a time without taking space and memory

# generators are actually iterable, you can iterate over them
# a list is an iterable, but it's not a generator

def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(10)
next(g)
next(g)
#print(next(g))

# for item in generator_function(10):
#     print(item)

# Example of its use
from time import time
def performance(fn):
    def check_performance():
        t1 = time()
        fn()
        t2 = time()
        print(f'took {t2-t1}s')
    return check_performance

@performance
def long_time():
    print(1)
    for i in range(100000000):
        i * 5

@performance
def long_time2():
    print(2)
    for i in list(range(100000000)):
        i * 5

# first one is much faster
#long_time()
#long_time2()

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            next(iterator)
        except StopIteration:
            break

special_for([1,2,3])

#our range function
class MyRange():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self
    
    def __next__(self):
        if MyRange.current < self.last:
            num = MyRange.current
            MyRange.current += 1
            return num
        raise StopIteration

ran = MyRange(0,100)
for i in ran:
    print(i)

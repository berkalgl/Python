# functions in python are first class citizens
# that can be passed around like var, declared as argument in functions

def hello(func):
    func()

def greet():
    print('Hi There !')

a = hello(greet)
print(a)

# Higher order function HOC
# can be two things
# it could either be a function that accepts another function or returns a function
def greet2():
    def func():
        return 5
    return func

# Decorator Pattern
# supercharges our function if we had our hello function and add extra functionallity to function
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*******')
        func(*args, **kwargs)
        print('*******')
    return wrap_func  

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)
    
@my_decorator
def bye(goodbye, a, b, c, d):
    print(goodbye,a,b,c,d)

hello('Hi there', ':)')
bye('Good Bye', 'See', 'You', 'Later' , 'There')

# decorators does like below
# hello2 = my_decorator(hello)
# hello2()

#Why do we need decorators ?
from time import time

def performance(fn):
    def check_performance(*args, **kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print(f'took {t2-t1}s')
        return result
    return check_performance

@performance
def long_time():
    for i in range(100000):
        i * 5

long_time()

#exercise
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'id' : 1,
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

auth_list = [1,2,3,4]

def authenticated(fn):
    # code here
    def check_auth(*args, **kwargs):
        if args[0]['id'] in auth_list:
            return fn(*args,**kwargs)

        print('not auth')
    return check_auth

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
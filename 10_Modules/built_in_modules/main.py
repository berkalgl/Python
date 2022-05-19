# all the modules python provides
# https://docs.python.org/3/py-modindex.html

import random 

#print(random)

#help(random)

#print(dir(random))

print(random.random())
print(random.randint(1,10))
print(random.choice([1,2,3,4,5]))

my_list = [1,2,3,4]
random.shuffle(my_list)
print(my_list)

import sys

# we can access the parameters when scripts are called from terminals
# calls like
# python3 main .py berk algul
first = sys.argv[1]
last = sys.argv[2]

print(f'hi {first}, {last}')
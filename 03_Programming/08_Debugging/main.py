# debugging
# linting
# ide/ editor
# read errors
# pdb (python built-in debugger) https://docs.python.org/3/library/pdb.html
# useful commands can be accessed via help
# variables can be changed

import pdb

def add(num1, num2):
    pdb.set_trace()
    #print(num1, num2)
    return num1 + num2

add(4, 'aaa')
import utility as uti
import shopping.shopping_cart as sc

# different ways of importing module
#from shopping.shopping_cart import buy
#from shopping import shopping_cart
#from utility import *

print(uti)

print(uti.multiply(3,4))

print(sc.buy(1))

# importing a module creates a __pycache__ file on every runtime
# cpython intrepreter caches module
#pyc is a compiled file
# instead of loading utility.py, it is going to load up this compiled version of utility.
# because nothing has changed in utility.py.

# package is a folder that contains modules.
# shopping is a package

# one of the rules of a package of a python
# is that on the root of the package you have to have __init__.py
# because interpreter is going to read this and say this is a python package

#you can add a package to a package

# modules overrides built-in functions

# __main__

#if __name__ == '__main__':
print(__name__) #prints __main__
# interpreter finds the module, it adds this code to memory. now it has access

# the name main, is given specifially to the file that we run because when we ran one single file
# that one file is default named __main__
# this condition statement is a good way for us to only run code of the main file
# if we add if statement, the code do not run unless the file is the one is running.

# print(type(utility.st1)) #prints out utility.Student so is created in utility class
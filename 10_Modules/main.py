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

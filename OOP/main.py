class PlayerCharacter():
    #Class Object Attribute
    # Static
    membership = True

    def __init__(self, name='unknown', age=0):
        #regular class attributes
        if(self.membership and age > 18):
            self.age = age
            self.name = name

    def run(self, hello):
        print(f'{self.name} Running... {hello}')

    #can be used even the class has not been initialized
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2
        #you can init the class 
        #return cls('Teddy', num1 + num2)

    #same with classmethod except you cannot access cls
    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2

player1 = PlayerCharacter("Cindy",21)
player1.run("hello")
print(PlayerCharacter.adding_things(1,2))

#introspection in programming means the ability to determine the type of an object at runtime
player2 = PlayerCharacter('Wizard', 23)
print(dir(player2)) #we can see the methods and attributes that player character access

#dunder methos allow us to use python specific functions on objects created through our class
# we can modify and override
#https://docs.python.org/3/reference/datamodel.html#special-method-names
class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {'name': 'Yoyo', 'has_pets': False}

    def __str__(self):
        print(object.__str__(self))
        return f'{self.color}'

    def __len__(self):
        return 5

    # def __del__(self):
    #     print('deleted')

    def __call__(self):
        return ('yess')

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
action_figure.__str__()
print(str(action_figure))
print(len(action_figure))
print(action_figure()) # __call__ method in object
print(action_figure['name'])


#Exercise
class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()
len(super_list1)
super_list1.append(5)
super_list1[0]
issubclass(SuperList, list)


# MRO - Method resolution order
# is a rule that python follows to determine when you run a method
# depfth first search
# http://www.srikanthtechnologies.com/blog/python/mro.aspx
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):
    pass

print(D.num)
print(D.mro())


#           A
#         /   \
#        B     C
#         \   /
#           D

# we avoid multiple intheritance 
class X:pass
class Y:pass
class Z:pass
class A(X, Y):pass
class B(Y, Z):pass
class M(B, A, Z):pass

print(M.mro())
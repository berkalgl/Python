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
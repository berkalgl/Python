#instantiation
class Player:
    def __init__(self, name, type):
        print('Player',self)
        self.name = name
        self.type = type
    
    def introduce(self):
        print("Hi I am",self.name,",I'm a" ,self.type)
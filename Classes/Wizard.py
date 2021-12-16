from Player import Player
class Wizard(Player):
    def __init__(self, name, type):
        print('Wizard',self)
        super().__init__(name, type)
    
    def play(self):
        print("WEEEE I'm a", self.type)
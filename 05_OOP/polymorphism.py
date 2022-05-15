# means manyforms
# it is the ability of redefine methods for these derived classes
# attack function
# super

class User:
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

class Warrior(User):
    def __init__(self, email):
        super().__init__(email)    

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with Arrows : {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

def player_attack(char):
    char.attack()

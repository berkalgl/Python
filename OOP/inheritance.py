# new objects to take on the properties of existing objects

#users

class User:
    def sign_in(self):
        print('logged in')
    
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

    def check_arrows(self):
        print(f'{self.num_arrows} remaning...')

    def run(self):
        print('ran really fast')

# multiple inheritance
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        super().__init__(name, power)
        Archer.__init__(self,name, arrows)

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.sign_in()

#check if wizard1 is instance of Wizard
isinstance(wizard1, Wizard)
isinstance(wizard1, object)

#multiple
hb1 = HybridBorg('borgie',100, 500)
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())

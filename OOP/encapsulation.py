# Encapsulating data, attrbts into a bigger class
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("Run")

    def speak(self):
        print(f'My name is {self.name}, and I am {self.age} years old')
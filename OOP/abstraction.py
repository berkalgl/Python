# hiding of information or abstracting away information and giving access to
# only what's necessary

#private ?
#dander built-in functions
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print("Run")

    def speak(self):
        print(f'My name is {self._name}, and I am {self._age} years old')
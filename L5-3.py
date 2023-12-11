class Animal(): 
    def __init__(self, name, age):
        self.age = age
        self.name = name

class Zebra (Animal): 
    family = 'Equus'

class Dolphin (Animal): 
    family = 'Delphinidae'

D_1 = Dolphin('Bottle', 2)

print(D_1.family)
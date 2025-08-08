class Vertebrate:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} Moves in a generic way.")
    
class Mammal(Vertebrate):
    def move(self): #method overriding
        print(f"{self.name} walks on land.")


class Bird(Vertebrate):
    def move(self): #method overriding
        print(f"{self.name} flies in the sky.")


animals = [Vertebrate("Generic Vertebrate"),Mammal("Dog"), Bird("Eagle")]

for animal in animals:
    animal.move()  # Polymorphism in action
    
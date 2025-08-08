class Vertebrate:
    def __init__(self, name):
        self.name = name
        self.spine = True
    
    def move(self):
        print(f"{self.name} is moving.")

class Mammal(Vertebrate):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color
    
    def nurse(self):
        print(f"{self.name} is nursing its too young.")  

class Bird(Vertebrate):
    def __init__(self, name, wing_span):
        super().__init__(name)
        self.wing_span = wing_span
    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wing_span} meters.")              


dog = Mammal("Bear", "Brown")
dog.move()
dog.nurse() 
print("Spine Exists?", dog.spine)

eagle = Bird("Eagle", 2.5)
eagle.move()
eagle.fly()
print("Spine Exists?", eagle.spine)
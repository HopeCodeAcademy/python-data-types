from abc import ABC, abstractmethod

class Three_Dimensional_Shapes(ABC):
    @abstractmethod
    def calc_volume(self):
        pass

class  Cube(Three_Dimensional_Shapes):
    def __init__(self, side_length):
        self.side_length = side_length

    def calc_volume(self):
        return self.side_length ** 3

side_length = 6
cube = Cube(side_length)

print("Cube's Side",side_length)
print("Cube's Volume:", cube.calc_volume())

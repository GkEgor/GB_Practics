from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def fabric_consumption(self):
        pass

class Coat(Clothes):
    def fabric_consumption(self):
        print(f'Расход ткани на пальто {self.size} размера составит {round(self.size / 6.5 + 0.5, 2)} м')

class Jacket(Clothes):
    @property
    def fabric_consumption(self):
        print(f'Расход ткани на пиджак под рост {self.size} м составит {2 * self.size + 0.3} м')

coat = Coat(56)
coat.fabric_consumption()
jacket = Jacket(1.83)
jacket.fabric_consumption




from abc import ABC, abstractmethod

class Cloth(ABC):

    @abstractmethod
    def calculate(self):
        pass

class Coat(Cloth):
    def __init__(self, param):
        self.param = param

    @property
    def calculate(self):
        return self.param / 6.5 + 0.5


class Suit(Cloth):
    def __init__(self, param):
        self.param = param

    @property
    def calculate(self):
        return 2 * self.param + 0.3



coat = Coat(54)

suit = Suit(180)

print(coat.calculate)
print(suit.calculate)

total = coat.calculate + suit.calculate

print(total)


from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calc(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def calc(self):
        return self.v / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calc(self):
        return self.h * 2 + 0.3


my_coat = Coat(float(input('Введите размер пальто: ')))
my_suit = Suit(float(input('Введите рост для костюма: ')))
print('Общие расходы равны:', my_coat.calc + my_suit.calc)

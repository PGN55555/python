class ComplexCh:
    def __init__(self, ch):
        str_2 = str(ch)
        str_2 = str_2.replace('i', '')
        str_2 = str_2.replace('j', '')
        str_2 = str_2.replace('(', '')
        str_2 = str_2.replace(')', '')
        self.ch = list(map(int, str_2.split('+')))

    def __add__(self, other):
        return complex(self.ch[0] + other.ch[0], self.ch[1] + other.ch[1])

    def __mul__(self, other):
        return complex(self.ch[0] * other.ch[0] - self.ch[1] * other.ch[1], self.ch[0] * other.ch[1] + self.ch[1] * other.ch[0])


num_1 = ComplexCh(complex(1, 2))
num_2 = ComplexCh(complex(4, 10))
print(num_1 + num_2)
print(num_1 * num_2)

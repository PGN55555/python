class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        ans = self.count - other.count
        if ans > 0:
            return ans
        else:
            return 'Результат вычитания отрицательный'

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, num):
        stroka = ''
        for i in range(1, self.count + 1):
            stroka += '*'
            if i % num == 0:
                stroka += '\n'
        return stroka

cell_1 = Cell(int(input('Введите количество ячеек первой клетки: ')))
cell_2 = Cell(int(input('Введите количество ячеек второй клетки: ')))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(4))
print(cell_2.make_order(3))

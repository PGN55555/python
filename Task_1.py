class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        mas = ''
        for line in self.matrix:
            for symbol in line:
                mas += f'{symbol} '
            mas += '\n'
        return mas

    def __add__(self, other):
        summ = []
        for i, el_i in enumerate(self.matrix):
            summ.append([self.matrix[i][j] + other.matrix[i][j] for j in range(len(el_i))])
        return summ


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)

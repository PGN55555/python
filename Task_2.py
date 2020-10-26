class Road:
    mass = 25
    thickness = 5
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return str(self._length * self._width * self.mass * self.thickness / 1000) + ' т'

a = Road(float(input('Введите длину в метрах: ')), float(input('Введите ширину в метрах: ')))
print('Масса равна', a.calc())

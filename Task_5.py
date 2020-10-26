class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}.')


class Pen(Stationery):
    def draw():
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):
    def draw():
        print('Запуск отрисовки карандашом.')


class Handle(Stationery):
    def draw():
        print('Запуск отрисовки маркером.')


Stationery(input('Чем рисовать? ')).draw()
Pen.draw()
Pencil.draw()
Handle.draw()

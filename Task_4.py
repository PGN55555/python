class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(name, color, f'скорость - {speed} полиция - {is_police}')

    def go(self):
        print(self.name, 'Машина поехала')

    def stop(self):
        print(self.name, 'Машина остановилась')

    def turn(self, direction):
        print(self.name, 'Машина повернула', direction)

    def show_speed(self):
        print(self.name, 'Текущая скорость равна', self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.name, 'Текущая скорость равна', self.speed)
        if self.speed > 60:
            print(self.name, 'Превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(self.name, 'Текущая скорость равна', self.speed)
        if self.speed > 40:
            print(self.name, 'Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


TownCar(70, 'grey', 'Nissan').show_speed()
SportCar(100, 'red', 'Tesla').go()
SportCar(100, 'red', 'Tesla').show_speed()
WorkCar(40, 'black', 'BMW').stop()
PoliceCar(200, 'white', 'Lada', True).turn('right')

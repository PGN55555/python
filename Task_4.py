class Storehouse:
    log_reception = {'printer': 0, 'scanner': 0, 'xerox': 0}
    log_transfer = {}

    def reception(self, what, count):
        self.log_reception[what] += count
        print('Приём:', self.log_reception)

    def transfer(self, what, where, count):
        if self.log_transfer.get(where) == None:
            self.log_transfer.update({where: {what: count}})
        else:
            if self.log_transfer[where].get(what) == None:
                self.log_transfer[where].update({what: count})
            else:
                self.log_transfer[where][what] += count
        print('Передача:', self.log_transfer)


class Equipment:
    def __init__(self, trademark, model, dimensions):
        self.trademark = trademark
        self.model = model
        self.dimensions = dimensions


class Printer(Equipment):
    def __init__(self, trademark, model, dimensions, is_color, speed, printer_type):
        self.trademark = trademark
        self.model = model
        self.dimensions = dimensions
        self.is_color = is_color
        self.speed = speed
        self.printer_type = printer_type


class Scanner(Equipment):
    def __init__(self, trademark, model, dimensions, resolution):
        self.trademark = trademark
        self.model = model
        self.dimensions = dimensions
        self.resolution = resolution


class Xerox(Equipment):
    def __init__(self, trademark, model, dimensions, quality_of_print):
        self.trademark = trademark
        self.model = model
        self.dimensions = dimensions
        self.quality_of_print = quality_of_print


def check(ch_2, ch_1=2147483647):
    flag = True
    while flag:
        ans = input()
        if ans.isdigit():
            if int(ans) > ch_1 or int(ans) < ch_2:
                print('Недопустимое значение')
            else:
                flag = False
        else:
            print('Недопустимое значение')
    return int(ans)


p = Printer('Canon', 'SuperPrinter', '300*200*10', True, 10, 'laser')
s = Scanner('Kodak', 'SuperScanner', '310*180*20', '4000*3000')
x = Scanner('Xerox', 'SuperXerox', '400*220*25', 'amazing')

print('Введите вариант:')
print('1 - Принтер')
print('2 - Сканер')
print('3 - Ксерокс')
ans = check(1, 3)

print('Введите вариант:')
print('1 - Принять')
print('2 - Передать')

if ans == 1:
    if check(1, 2) == 1:
        print('Сколько?')
        Storehouse.reception(f'{p.trademark} {p.model}', check(1))
    else:
        Storehouse.transfer(f'{p.trademark} {p.model}', input('Куда и сколько? (через ENTER)\n'), check(1))
elif ans == 2:
    if check(1, 2) == 1:
        print('Сколько?')
        Storehouse.reception(f'{p.trademark} {p.model}', check(1))
    else:
        Storehouse.transfer(f'{p.trademark} {p.model}', input('Куда и сколько? (через ENTER)\n'), check(1))
else:
    if check(1, 2) == 1:
        print('Сколько?')
        Storehouse.reception(f'{p.trademark} {p.model}', check(1))
    else:
        Storehouse.transfer(f'{p.trademark} {p.model}', input('Куда и сколько? (через ENTER)\n'), check(1))

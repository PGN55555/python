class Error(Exception):
    def __init__(self, text):
        self.text = text


delimoe = float(input('Введите делимое: '))
delitel = float(input('Введите делитель: '))

try:
    if delitel == 0:
        raise Error('Попытка деления на ноль!')
except Error as err:
    print(err)
else:
    print(delimoe / delitel)

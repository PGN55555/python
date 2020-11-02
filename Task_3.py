class Error(Exception):
    def __init__(self, text):
        self.text = text


mas = []
num = ''
print('Для выхода введите q')

while num != 'q':
    num = input('Введите число: ').replace(' ', '')
    if num != 'q':
        try:
            if not num.replace('.', '', 1).isdigit():
                raise Error('Вы ввели не число')
        except Error as err:
            print(err)
        else:
            if num.replace('.', '', 1) == num:
                mas.append(int(num))
            else:
                mas.append(float(num))

print('Готовый список:', mas)

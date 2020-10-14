def my_func(a, b, c):
    mas = [a, b, c]
    mas.remove(min(mas))
    return sum(mas)


a = float(input('Введите первый аргумент: '))
b = float(input('Введите второй аргумент: '))
c = float(input('Введите третий аргумент: '))

print('Сумма наибольших двух аргументов равна', my_func(a, b, c))

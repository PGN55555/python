def int_func(stroka):
    mas = list(stroka)
    mas[0] = mas[0].upper()
    return ''.join(mas)


stroka = input('Введите строку: ')
mas = stroka.split()
ans = ''

for i in mas:
    ans += int_func(i) + ' '

print('Результат:', ans)

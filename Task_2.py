n = int(input('Введите количество элементов: '))
spisok = []

for i in range(n):
    spisok.append(input('Введите элемент массива: '))

for i in range(1, n, 2):
    spisok[i - 1], spisok[i] = spisok[i], spisok[i - 1]

print('Новый список:', *spisok)
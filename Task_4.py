stroka = input('Ввведите строку: ').split()

for num, i in enumerate(stroka, 1):
    print(num, i[:10])

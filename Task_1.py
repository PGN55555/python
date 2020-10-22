a = open("text.txt", "w", encoding="utf-8")

ans = ' '
while ans != '':
    ans = input('Введите данные: ')
    a.write(ans + '\n')

a.close()

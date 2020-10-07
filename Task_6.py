a = float(input('Результат в первый день: '))
b = float(input('Необходимый результат: '))
i = 1

while a < b:
    a = a + a / 10
    i += 1

print(i)

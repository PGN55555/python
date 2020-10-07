num = int(input('Ввведите число: '))
maximum = 0
while num > 0:
    temp = num % 10
    if temp >= maximum:
        maximum = temp
    num //= 10
print('Самая большая цифра равна', maximum)

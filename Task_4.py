def my_func(x, y):
    #return x ** y
    x = 1 / x
    ans = x
    for i in range(abs(y) - 1):
        ans *= x
    return ans


x = float(input('Введите действительное положительное число x: '))
y = int(input('Введите целое отрицательное число y: '))

print(f'x в степени y равно {my_func(x, y)}')

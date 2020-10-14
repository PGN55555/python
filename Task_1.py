def division(a, b):
    if b != 0:
        ans = a / b
        return int(ans) if ans == int(ans) else ans
    else:
        return "на ноль делить нельзя"


a = float(input('Введите делимое: '))
b = float(input('Введите делитель: '))
print('Результат:', division(a, b))

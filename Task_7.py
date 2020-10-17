def fact(n):
    """
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)
    """
    factorial = 1
    if n != 0:
        for i in range(1, n + 1):
            factorial *= i
            yield factorial
    else:
        yield factorial


n = int(input('Введите n: '))
for i in fact(n):
    print(i, end=' ')

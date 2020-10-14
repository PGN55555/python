def summ(mas):
    ans = 0
    for i in mas:
        if i != 'q':
            ans += float(i)
    return ans


print('Для выхода введите q')

mas = []
all_sum = 0
while not 'q' in mas:
    mas = input('Введите числа: ').split()
    all_sum += summ(mas)
    print('Сумма чисел равна', all_sum)

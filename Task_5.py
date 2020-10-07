earn = float(input('Выручка фирмы: '))
cost = float(input('Издержки фирмы: '))

if earn > cost:
    print('Компания работает с прибылью')
    print(f'Рентабельность выручки равна {earn/cost:.2f}')
elif earn < cost:
    print('Компания работает в убыток')
else:
    print('Выручка и издержки равны')

workers = int(input('Численность сотрудников фирмы: '))
print(f'Прибыль фирмы на одного сотрудника равна {earn/workers:.2f}')

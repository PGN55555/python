month = int(input('Введите месяц: '))

l = ['зима', 'весна', 'лето', 'осень']
d = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}

if month >= 1 and month <= 2 or month == 12:
    month_name = l[0]
elif month >= 3 and month <= 5:
    month_name = l[1]
elif month >= 6 and month <= 8:
    month_name = l[2]
else:
    month_name = l[3]

print(f'Месяц через список: {month_name}')
print(f'Месяц через словарь: {d.get(month)}')
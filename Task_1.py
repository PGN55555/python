from sys import argv
# вводить в порядке: выработка в часах, ставка в час, премия
name, hour, rate_per_hour, bonus = argv
print('Зарплата равна', float(hour) * float(rate_per_hour) + float(bonus))

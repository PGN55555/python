import json

i = 0
av = 0
profit_dict = {}
profit_av = {}
ans = [profit_dict, profit_av]

with open('text.txt', encoding='utf-8') as file:
    for line in file:
        mas = line.split()
        profit = float(mas[2]) - float(mas[3])
        if profit >= 0:
            i += 1
            av += profit
        profit_dict[mas[0]] = profit

profit_av["average_profit"] = av / i

with open('text.json', 'w') as file:
    json.dump(ans, file)

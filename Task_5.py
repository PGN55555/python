a = open("text.txt", "w", encoding="utf-8")
a.write('12 3425 36 24 34.07 56601')
a.close()
a = open(r"text.txt", "r", encoding="utf-8")
content = a.readline()
mas = map(float, content.split())
s = 0

for i in mas:
    s += i

print('Сумма чисел равна', s)
a.close()

a = open(r"text.txt", "r", encoding="utf-8")
av = 0
i = 0

for line in a:
    mas = line.split()
    if float(mas[1]) < 20000:
        print(mas[0])
    av += float(mas[1])
    i += 1

print(f'Средняя величина дохода равна {av / i}')
a.close()

a = open(r"text.txt", "r", encoding="utf-8")
new = open("text2.txt", "w", encoding="utf-8")

for line in a:
    mas = line.split()
    word = mas[0].lower()
    if word == 'one':
        word = 'Один'
    elif word == 'two':
        word = 'Два'
    elif word == 'three':
        word = 'Три'
    else:
        word = 'Четыре'
    mas[0] = word
    mas.append('\n')
    new.writelines(mas)

a.close()
new.close()

a = open(r"text.txt", "r")
mas = list(a.read())
a.close()
stroka = ''
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = 0
key = ''
ans = {}

while ':' in mas:
    mas.remove(':')
while '.' in mas:
    mas.remove('.')
while '—' in mas:
    mas.remove('—')
while '(' in mas:
    mas.remove('(')
while ')' in mas:
    mas.remove(')')
while '\n' in mas:
    mas.insert(mas.index('\n'), ' ')
    mas.remove('\n')

stroka = ''.join(mas)
mas = stroka.split()

for i in mas:
    if i.istitle():
        if key != '':
            ans.update(dict(key=s))
            s = 0
        key = i
    else:
        temp = list(i)
        while not digits in temp:
            
        """for el in range(0, len(temp)):
            if not temp[el] in digits:
                temp.remove(temp[el])
                el -= 1"""
        s += int(''.join(temp))

print(ans)

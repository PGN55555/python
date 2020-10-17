from itertools import count, cycle

my_list = ['A', '1', 'B', '2', 'C', '3']
for i in count(3):
    if i > 20:
        print()
        break
    print(i, end=' ')

i = 0
for el in cycle(my_list):
    print(el)
    if i > 17:
        break
    i += 1

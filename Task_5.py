from functools import reduce

def pr(a, b):
    return a * b

my_list = [num for num in range(100, 1001, 2)]
print('Произведение всех элементов списка:', reduce(pr, my_list))

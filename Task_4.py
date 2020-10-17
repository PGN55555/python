from random import randint
old_list = [randint(1, 30) for i in range(15)]
new_list = [num for num in old_list if old_list.count(num) == 1]
print('Изначальный список:', *old_list)
print('Преобразованный список:', *new_list)

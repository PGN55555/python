from random import randint
old_list = [randint(1, 500) for i in range(15)]
new_list = [old_list[i] for i in range(1, len(old_list)) if old_list[i] > old_list[i - 1]]
print('Изначальный список:', *old_list)
print('Преобразованный список:', *new_list)

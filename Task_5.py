my_list = [9, 8, 6, 4, 4, 3]
num = int(input('Новый элемент рейтинга: '))
#i = 0

#if num in my_list:
my_list.insert(my_list.index(num) + my_list.count(num), num)
#else:
#    while num < my_list[i]:
#        i += 1
#    my_list.insert(i, num)

print('Новый рейтинг:', *my_list)

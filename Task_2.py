def info(name, surname, year, city, email, tel):
    print(f'Имя и фамилия: {name} {surname}, год рождения: {year}, город проживания: {city}, email: {email}, телефон: {tel}')


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
tel = input('Введите телефон: ')
info(name = name, surname = surname, year = year, city = city, tel = tel, email = email)

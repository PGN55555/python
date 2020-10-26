class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


a = Position(input('Введите имя сотрудника: '), input('Введите фамилию сотрудника: '), input('Введите должность сотрудника: '), float(input('Введите зарплату сотрудника: ')), float(input('Введите премию сотрудника: ')))
print('Полное имя сотрудника:', a.get_full_name())
print('Доход сотрудника:', a.get_total_income())

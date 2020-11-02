class Date:
    def __init__(self, stroka):
        self.stroka = stroka

    @classmethod
    def normal(cls, data):
        return cls(list(map(int, data.split('-'))))

    @staticmethod
    def validate(mas):
        ans = ''
        print(mas)
        if mas[0] < 1 or mas[0] > 31:
            ans += 'Неверное число\n'
        if mas[1] < 1 or mas[1] > 12:
            ans += 'Неверный месяц\n'
        return ans if ans != '' else 'Всё верно'

clss = Date.normal('32-13-2019')

print(Date.validate(clss.stroka))

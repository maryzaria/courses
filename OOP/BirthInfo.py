from functools import singledispatchmethod
from datetime import date, timedelta


class BirthInfo:
    @singledispatchmethod
    def __init__(self, data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def _(self, data):
        self.birth_date = data

    @__init__.register(str)
    def _(self, data):
        self.birth_date = date.fromisoformat(data)

    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, data):
        year, month, day = data
        self.birth_date = date(year, month, day)

    @property
    def age(self):
        today = date.today()
        bd = self.birth_date
        if date(2023, bd.month, bd.day) > today:
            return today.year - bd.year - 1
        else:
            return today.year - bd.year


today = date.today()
for day in range(10):
    birthday = (today + timedelta(days=day)).replace(year=2000)
    birthinfo = BirthInfo(birthday)
    # true_age = current_age(birthday, today)
    print(birthinfo.age)
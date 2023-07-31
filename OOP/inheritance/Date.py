from datetime import date


class Date:
    def __init__(self, year, month, day):
        self._date = date(year=year, month=month, day=day)

    def iso_format(self):
        return self._date.isoformat()


class USADate(Date):
    def format(self):
        return f'{self._date.strftime("%m-%d-%Y")}'


class ItalianDate(Date):
    def format(self):
        return f'{self._date.strftime("%d/%m/%Y")}'



usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())

italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())
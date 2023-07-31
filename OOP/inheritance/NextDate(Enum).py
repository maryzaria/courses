from enum import IntEnum, Enum
from datetime import date, datetime, timedelta


Weekday = Enum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)


class NextDate:
    def __init__(self, today, weekday, after_day=False):
        self.today = today
        self.weekday = weekday
        self.after_day = after_day

    def date(self):
        # if self.after_day:
        dt = datetime(year=self.today.year, month=self.today.month, day=self.today.day) + timedelta(days=self.days_until())
        return dt.date()

    def days_until(self):
        if self.after_day and self.today.weekday() == self.weekday.value:
            return 0
        if self.today.weekday() < self.weekday.value:
            return - self.today.weekday() + self.weekday.value
        return 7 - (self.today.weekday() - self.weekday.value)


# TEST_5:
from datetime import date

for weekday in Weekday:
    today = date(2023, 4, 27)                              # четверг
    next_date = NextDate(today, weekday, True)

    print(next_date.date())
    print(next_date.days_until())
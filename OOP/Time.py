from datetime import datetime


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours % 24
        if minutes >= 60:
            self.hours += minutes // 60
        self.minutes = minutes % 60

    def __str__(self):
        time = datetime(hour=self.hours, minute=self.minutes, year=1, month=1, day=1)
        return f'{time.strftime("%H:%M")}'

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours += other.hours
            self.minutes += other.minutes
            return self
        return NotImplemented

# TEST_7:
t = Time(40, 80)
print(t.__add__([]))
print(t.__iadd__('bee'))
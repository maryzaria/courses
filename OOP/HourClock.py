class HourClock:
    def __init__(self, hours):
        self.hours = hours  # возвращаемся к свойству hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if not (isinstance(hours, int) and 1 <= hours <= 12):
            raise ValueError('Некорректное время')
        self._hours = hours

    hours = property(get_hours, set_hours)

# TEST_3:
try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)
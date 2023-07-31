class Currency:
    __RATE = {
        'EUR': {'EUR': 1, 'USD': 1.1, 'RUB': 90},
        'USD': {'EUR': 1 / 1.1, 'USD': 1, 'RUB': 1 / 1.1 * 90},
        'RUB': {'EUR': 1 / 90, 'USD': 1 / 90 * 1.1, 'RUB': 1}
    }

    def __init__(self, num: (int, float), currency: str) -> None:
        self.count = num
        self.currency = currency

    def __str__(self):
        return f'{round(self.count, 2)} {self.currency}'

    def change_to(self, currency: str):
        self.count *= self.__RATE[self.currency][currency]
        self.currency = currency

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                other.change_to(self.currency)
            return Currency(self.count + other.count, self.currency)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                other.change_to(self.currency)
            return Currency(self.count * other.count, self.currency)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                other.change_to(self.currency)
            return Currency(self.count - other.count, self.currency)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                other.change_to(self.currency)
            return Currency(self.count / other.count, self.currency)
        return NotImplemented


# TEST_1:
money1 = Currency(10, 'EUR')
money2 = Currency(20, 'USD')
print(money1)
print(money2)

# TEST_2:
money = Currency(10, 'EUR')

money.change_to('RUB')
print(money)
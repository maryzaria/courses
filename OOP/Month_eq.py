from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __repr__(self):
        return f"{self.__class__.__name__}({self.year}, {self.month})"

    def __str__(self):
        return f'{self.year}-{self.month}'

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        if isinstance(other, tuple) and len(other) == 2:
            year, month = other
            return self.year == year and self.month == month
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Month):
            if self.year == other.year:
                return self.month > other.month
            return self.year > other.year
        if isinstance(other, tuple) and len(other) == 2:
            year, month = other
            if self.year == year:
                return self.month > month
            return self.year > year
        return NotImplemented


# TEST_2:
months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(sorted(months))

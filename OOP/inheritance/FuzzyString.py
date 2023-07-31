class UpperPrintString(str):
    def __str__(self):
        return f'{super().__str__().upper()}'


class LowerString(str):
    def __new__(cls, obj='', *args, **kwargs):
        return super().__new__(cls, str(obj).lower())


class FuzzyString(str):
    def __eq__(self, other):
        if isinstance(other, (str, FuzzyString)):
            return self.lower() == other.lower()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, (str, FuzzyString)):
            return self.lower() != other.lower()
        return NotImplemented

    def __contains__(self, item):
        # print(self.__str__())
        if isinstance(item, (str, FuzzyString)):
            return item.lower() in self.__str__().lower()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, (str, FuzzyString)):
            return self.lower() > other.lower()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (str, FuzzyString)):
            return self.lower() < other.lower()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, (str, FuzzyString)):
            return self.lower() >= other.lower()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, (str, FuzzyString)):
            return self.lower() <= other.lower()
        return NotImplemented

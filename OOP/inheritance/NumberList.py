from collections import UserList


class NumberList(UserList):
    def __init__(self, iterable=()):
        super().__init__(iterable)
        for item in iterable:
            self._try_to_add_item(item)

    def _try_to_add_item(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def _add_item(self, item):
        self._try_to_add_item(item)
        self.data += [item]

    def __add__(self, other):
        for item in other:
            self._add_item(item)
        return NumberList(self.data)

    __iadd__ = __add__

    def append(self, item):
        self._add_item(item)

    def extend(self, data):
        for item in data:
            self._add_item(item)

    def insert(self, index, data):
        self._try_to_add_item(data)
        super().insert(index, data)


# TEST_5:
numberlist = NumberList([1, 2])

try:
    numberlist += [3, '4']
except TypeError as e:
    print(e)

# TEST_6:
numberlist1 = NumberList([1, 2])

try:
    numberlist2 = numberlist1 + [3, '4']
except TypeError as e:
    print(e)

# TEST_7:
data = [1, 2, 3]
numberlist = NumberList(data)
print(numberlist)

data.extend([4, 5, 6])
print(data)
print(numberlist)

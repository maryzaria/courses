from collections.abc import *


class SortedList:
    def __init__(self, iterable=()):
        self._data = sorted(iterable[:])

    def add(self, obj):
        self._data.append(obj)
        self._data.sort()

    def discard(self, item):
        self._data = [i for i in self._data if i != item]

    def update(self, iterable):
        self._data.extend(list(iterable))
        self._data.sort()

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._data[item]
        return NotImplemented

    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            raise NotImplementedError

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        del self._data[key]

    def __len__(self):
        return len(self._data)

    def __reversed__(self):
        raise NotImplementedError

    def __repr__(self):
        return f'{self.__class__.__name__}({self._data})'

    def __add__(self, other):
        if isinstance(other, SortedList):
            return SortedList(self._data + other._data)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return SortedList(sorted(self._data * other))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, SortedList):
            self._data += other._data
            return self
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self._data = sorted(self._data * other)
            return self
        return NotImplemented


# TEST_11:
numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

id1_numbers1 = id(numbers1)
id1_numbers2 = id(numbers2)

numbers1 += numbers2
numbers2 *= 2

id2_numbers1 = id(numbers1)
id2_numbers2 = id(numbers2)

print(id1_numbers1 == id2_numbers1)
print(id1_numbers2 == id2_numbers2)
print(3 in numbers1)

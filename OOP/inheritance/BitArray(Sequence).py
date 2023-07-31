from collections.abc import *


class BitArray(Sequence):
    def __init__(self, iterable=()):
        self._data = iterable[:]

    def __str__(self):
        return f'{self._data}'

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._data[item]
        return NotImplemented

    def __invert__(self):
        return BitArray(list(0 if item == 1 else 1 for item in self._data))

    def __and__(self, other):
        if isinstance(other, BitArray) and len(self) == len(other):
            return BitArray(list(a and b for a, b in zip(self, other)))
        return NotImplemented

    def __or__(self, other):
        if isinstance(other, BitArray) and len(self) == len(other):
            return BitArray(list(a or b for a, b in zip(self, other)))
        return NotImplemented


# TEST_6:
bitarray = BitArray([1, 0, 1, 1])
print(bitarray.__or__(1))
print(bitarray.__and__(1.1))
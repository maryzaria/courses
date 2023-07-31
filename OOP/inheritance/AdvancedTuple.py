class AdvancedTuple(tuple):
    def __add__(self, other):
        if not hasattr(other, '__iter__'):
            return NotImplemented
        return AdvancedTuple(tuple(self) + tuple(other))

    def __radd__(self, other):
        if not hasattr(other, '__iter__'):
            return NotImplemented
        return AdvancedTuple(tuple(other) + tuple(self))

    __iadd__ = __add__


# TEST_3:
data = [[4, 5, 6], {4: None, 5: None, 6: None}, (4, 5, 6), '456', iter([4, 5, 6]), AdvancedTuple([4, 5, 6])]

advancedtuple = AdvancedTuple([1, 2, 3])

for item in data:
    print(advancedtuple + item, end=' ')
    print(item + advancedtuple)

# TEST_4:
data = ['456', [7, 8, 9], {10: None, 11: None, 12: None}, (13, 14, 15), iter([16, 17, 18]), AdvancedTuple([20, 21, 22])]

advancedtuple = AdvancedTuple([1, 2, 3])

for item in data:
    advancedtuple += item

print(advancedtuple)

# TEST_5:
advancedtuple = AdvancedTuple([1, 2, 3])
advancedtuple += []
print(advancedtuple)

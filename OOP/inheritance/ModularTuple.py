import copy


class ModularTuple(tuple):
    def __new__(cls, iterable=None, size=100):
        it = (num % size for num in copy.copy(iterable)) if iterable is not None else ()
        return super().__new__(cls, it)



# TEST_2:
modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)

print(modulartuple)

# TEST_3:
modulartuple = ModularTuple()
print(modulartuple)

# TEST_4:
modulartuple = ModularTuple([1, 2, 3, 4, 5], 1)

print(modulartuple)

# TEST_5:
data = [1, 2, 3, 4, 5]
modulartuple = ModularTuple(data, -5)

print(modulartuple)

data.extend([6, 7, 8, 9, 10])
print(data)
print(modulartuple)

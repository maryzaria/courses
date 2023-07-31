from copy import copy, deepcopy


class predicate:
    def __init__(self, func):
        self.func = func
        self._f = ''
        self.other_f = None
        self.invert = False

    def __call__(self, *args, **kwargs):
        if self._f == 'and':
            return self.get_result(self, *args, **kwargs) and self.get_result(self.other, *args, **kwargs)
        elif self._f == 'or':
            return self.get_result(self, *args, **kwargs) or self.get_result(self.other, *args, **kwargs)
        return self.func(*args, **kwargs)

    @staticmethod
    def get_result(obj, *args, **kwargs):
        if obj.invert:
            return not obj.func(*args, **kwargs)
        return obj.func(*args, **kwargs)

    def __and__(self, other):  # &
        self._f = 'and'
        self.other = other
        return self

    def __or__(self, other):  # |
        self._f = 'or'
        self.other = other
        return self

    def __invert__(self):
        res = copy(self)
        res.invert = True
        return res


# TEST_5:
@predicate
def is_arithmetic_mean(iterable):
    result = {iterable[i + 1] - iterable[i] for i in range(len(iterable) - 1)}
    return len(result) == 1


@predicate
def is_geometric_mean(iterable):
    result = {iterable[i + 1] // iterable[i] for i in range(len(iterable) - 1)}
    return len(result) == 1


print(is_arithmetic_mean([1, 2, 3, 4, 5]))
print(is_geometric_mean([1, 2, 4, 8, 16]))

print((is_arithmetic_mean & is_geometric_mean)([1, 2, 3, 4, 5]))
print((is_arithmetic_mean | is_geometric_mean)([1, 2, 3, 4, 5]))

print((is_arithmetic_mean & is_geometric_mean)([1, 2, 4, 8, 16]))
print((is_arithmetic_mean | is_geometric_mean)([1, 2, 4, 8, 16]))

print((~is_arithmetic_mean & ~is_geometric_mean)([1, 2, 4, 5]))
print((~is_arithmetic_mean | ~is_geometric_mean)([1, 2, 3, 4, 5]))

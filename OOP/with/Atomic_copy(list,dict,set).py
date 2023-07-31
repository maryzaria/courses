import copy


class Atomic:
    def __init__(self, data, deep=False):
        self._data = data
        self._deep = deep

    def __enter__(self):
        if not self._deep:
            self._new_data = copy.copy(self._data)
        else:
            self._new_data = copy.deepcopy(self._data)
        if isinstance(self._data, set):
            self._new_data = set(self._new_data)
        return self._new_data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if isinstance(self._data, list):
                self._data[:] = self._new_data
            else:
                self._data.clear()
                self._data.update(self._new_data)
        return True


# TEST_7:
data = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}

with Atomic(data) as atomic:
    atomic['e'] += 2   # изменение структуры

print(data)
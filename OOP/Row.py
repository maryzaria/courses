class Row:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            object.__setattr__(self, key, val)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            raise AttributeError('Установка нового атрибута невозможна')
        raise AttributeError('Изменение значения атрибута невозможно')

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

    def __repr__(self):
        return f"Row({', '.join(f'{key}={repr(val)}' for key, val in self.__dict__.items())})"

    @property
    def _keys(self):
        return tuple(self.__dict__.keys())

    @property
    def _values(self):
        return tuple(self.__dict__.values())

    def __eq__(self, other):
        if isinstance(other, Row):
            return self._keys == other._keys and self._values == other._values
        return NotImplemented

    def __hash__(self):
        return hash(self._keys) + hash(self._values)


# TEST_5:
row = Row(a=1, b=2, c=3)

try:
    del row.a
except AttributeError as e:
    print(e)



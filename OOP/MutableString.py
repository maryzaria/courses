class MutableString:
    def __init__(self, string=''):
        self.string = string
        self._lst = list(string)

    def lower(self):
        self.string = self.string.lower()
        return self.string

    def upper(self):
        self.string = self.string.upper()
        return self.string

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.string}')"

    def __iter__(self):
        yield from self.string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return MutableString(self.string[idx])
        if not isinstance(idx, int):
            raise TypeError('Индекс должен быть целым числом')
        return self._lst[idx]

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            self._lst[start:stop:step] = list(value)
        else:
            self._lst[key] = value
        self.string = ''.join(self._lst)

    def __delitem__(self, key):
        del self._lst[key]
        self.string = ''.join(self._lst)

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self.string + other.string)
        return NotImplemented


# TEST_9:
string = '''Many of you are familiar with the virtues of being a programmer. There are only three of them, 
and of course this is: laziness, impatience and pride. Larry Wall'''
mutablestring = MutableString(string)


print(mutablestring[::-10])

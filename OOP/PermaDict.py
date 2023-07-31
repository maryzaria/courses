class PermaDict:
    def __init__(self, data=()):
        self._d = dict(data) or {}

    def keys(self):
        return self._d.keys()

    def values(self):
        return self._d.values()

    def items(self):
        return self._d.items()

    def __iter__(self):
        yield from self._d

    def __len__(self):
        return len(self._d)

    def __getitem__(self, item):
        return self._d[item]

    def __setitem__(self, key, value):
        if key in self._d:
            raise KeyError('Изменение значения по ключу невозможно')
        self._d[key] = value

    def __delitem__(self, key):
        del self._d[key]



permadict = PermaDict()

permadict['name'] = 'Timur'
permadict['age'] = 30
del permadict['name']
print(permadict['age'])
print(len(permadict))
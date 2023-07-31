class AttrDict:
    def __init__(self, data=()):
        self._d = dict(data) or {}

    def __iter__(self):
        yield from self._d

    def __len__(self):
        return len(self._d)

    def __getitem__(self, item):
        return self._d[item]

    def __getattr__(self, item):
        return self._d[item]

    def __setitem__(self, key, value):
        self._d[key] = value


# TEST_2:
attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})

attrdict['city'] = 'Dubai'
attrdict['age'] = 31
print(attrdict.city)
print(attrdict.age)

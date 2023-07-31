class HistoryDict:
    def __init__(self, data=()):
        self._d = dict(data) or {}
        self._hist = dict((key, [val]) for key, val in data.items())

    def keys(self):
        return self._d.keys()

    def values(self):
        return self._d.values()

    def items(self):
        return self._d.items()

    def history(self, key):
        return self._hist.get(key, [])

    def __iter__(self):
        yield from self._d

    def __len__(self):
        return len(self._d)

    def __getitem__(self, item):
        return self._d[item]

    def __setitem__(self, key, value):
        self._d[key] = value
        self._hist.setdefault(key, []).append(value)

    def __delitem__(self, key):
        del self._d[key]
        del self._hist[key]

    def all_history(self):
        return self._hist


# TEST_8:
historydict = HistoryDict({'name': 'Irenica', 'country': 'Russia', 'level': 'junior', })

print(historydict.all_history())

historydict['country'] = 'Italy'
historydict['level'] = 'middle'
historydict['level'] = 'senior'

print(historydict.all_history())

del historydict['level']

print(historydict.all_history())

historydict['level'] = 'God'

print(historydict.all_history())


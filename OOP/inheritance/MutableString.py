from collections import UserString


class MutableString(UserString):
    def __init__(self, obj):
        super().__init__(obj)
        self._items = list(obj)

    def _join_data(self, items):
        self.data = ''.join(items)

    def lower(self):
        # self.data = ''.join(item.lower() for item in self._items)
        self._join_data(item.lower() for item in self._items)

    def upper(self):
        self._join_data(item.upper() for item in self._items)

    def sort(self, key=None, reverse=False):
        self._join_data(sorted(self.data, key=key, reverse=reverse))

    def __setitem__(self, index, value):
        self._items[index] = value
        self._join_data(self._items)

    def __delitem__(self, key):
        del self._items[key]
        self._join_data(self._items)


mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
mutablestring.sort()
print(mutablestring)
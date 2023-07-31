class Grouper:
    def __init__(self, iterable, key):
        self._group = {}
        self._key = key
        for item in iterable:
            self.add(item)
        # print(self._group)

    def add(self, item):
        self._group.setdefault(self.group_for(item), []).append(item)

    def group_for(self, item):
        return self._key(item)

    def __len__(self):
        return len(self._group)

    def __iter__(self):
        yield from self._group.items()

    def __contains__(self, key):
        return key in self._group

    def __getitem__(self, key):
        return self._group.get(key)


# TEST_6:
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]


grouper = Grouper(persons, key=lambda x: x.height)
print(sorted(grouper))

# TEST_7:
grouper = Grouper([], key=lambda x: x)
print(*grouper)

# TEST_8:
d = list(range(1, 100))
grouper = Grouper(d, bool)
print(*grouper)

d.append(100)
print(*grouper)

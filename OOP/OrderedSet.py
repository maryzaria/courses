class OrderedSet:
    def __init__(self, iterable=None):
        self.iterable = []
        if iterable is not None:
            for item in iterable:
                if item not in self.iterable:
                    self.iterable.append(item)

    def add(self, item):
        if item not in self.iterable:
            self.iterable.append(item)

    def discard(self, item):
        if item in self.iterable:
            self.iterable.remove(item)

    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        yield from self.iterable

    def __contains__(self, item):
        return item in self.iterable

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and all(s == o for s, o in zip(self, other))
        if isinstance(other, set):
            return len(self) == len(other) and all(item in other for item in self.iterable)
        return NotImplemented




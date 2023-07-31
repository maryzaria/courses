class CyclicList:
    def __init__(self, iterable=None):
        if iterable:
            self.iterable = iterable[:]
        else:
            self.iterable = []
        self._n = 0

    def __len__(self):
        return len(self.iterable)

    def append(self, item):
        self.iterable.append(item)

    def pop(self, index=-1):
        return self.iterable.pop(index)

    def __iter__(self):
        while True:
            yield self.iterable[self._n % len(self)]
            self._n += 1

    def __getitem__(self, index):
        return self.iterable[index % len(self)]


cyclic_list = CyclicList([1, 2, 3])

cyclic_list.append(4)
print(cyclic_list.pop())
print(len(cyclic_list))
print(cyclic_list.pop(0))
print(len(cyclic_list))
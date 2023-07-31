class LoopTracker:
    def __init__(self, iterable):
        # self.iterable = iter(iterable)
        self.it_list = list(iterable)
        self._cashe = []
        self.n = -1
        self.empty = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n >= len(self.it_list):
            self.empty += 1
            raise StopIteration
        res = self.it_list[self.n]
        self._cashe.append(res)
        return res

    @property
    def accesses(self):
        return len(self._cashe)

    @property
    def empty_accesses(self):
        return self.empty

    @property
    def first(self):
        if len(self.it_list) > 0:
            return self.it_list[0]
        raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if self.accesses > 0:
            return self._cashe[-1]
        raise AttributeError('Последнего элемента нет')

    def is_empty(self):
        return len(self._cashe) >= len(self.it_list)



# TEST_9:
loop_tracker = LoopTracker(range(1_000))

for _ in range(100_000):
    next(loop_tracker, None)

print(loop_tracker.accesses)
print(loop_tracker.empty_accesses)





class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = list(iterable)
        self.n = n
        self.count = -n - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += self.n + 1
        if self.count >= len(self.iterable):
            raise StopIteration
        return self.iterable[self.count]


skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

print(*skipiterator)
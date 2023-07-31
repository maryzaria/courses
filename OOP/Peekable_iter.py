class Peekable:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.it_list = list(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.it_list:
            self.it_list = self.it_list[1:]
        return next(self.iterable)

    def peek(self, default='None'):
        if self.it_list:
            return self.it_list[0]
        elif default == 'None':
            raise StopIteration
        return default


iterator = Peekable('beegeek')

print(next(iterator))
print(next(iterator))
print(*iterator)
from random import randint
from string import ascii_lowercase


class Xrange:
    def __init__(self, start, end, step=1):
        self.step = step
        self.start = start - self.step
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            self.start += self.step
            if self.start >= self.end:
                raise StopIteration
        if self.step < 0:
            self.start -= abs(self.step)
            if self.start <= self.end:
                raise StopIteration
        return self.start


class Alphabet:
    def __init__(self, language):
        self.loc = {"ru": 'абвгдежзийклмнопрстуфхцчшщъыьэюя',
                    'en': ascii_lowercase}
        self.lang = language
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.lang == 'ru' and self.index >= 32:
            self.index = 0
        elif self.lang == 'en' and self.index >= 26:
            self.index = 0
        return self.loc[self.lang][self.index]


class RandomNumbers:
    def __init__(self, left, right, n):
        self.index = -1
        self.n = n
        self.left = left
        self.right = right

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= self.n:
            raise StopIteration
        return randint(self.left, self.right)


class Cycle:
    def __init__(self, iterable):
        self.index = -1
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.iterable):
            self.index = 0
        return self.iterable[self.index]


class CardDeck:
    def __init__(self):
        self.mast = ('пик', 'треф', 'бубен', 'червей')
        self.num = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= 52:
            raise StopIteration
        return f'{self.num[self.index % 13]} {self.mast[(self.index // 13) % 4]}'


class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.keys = [*self.data]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.keys):
            raise StopIteration
        return self.keys[self.index], self.data[self.keys[self.index]]



class PowerOf:
    def __init__(self, number):
        self.num = number
        self.pow = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.pow += 1
        return self.num ** self.pow


class Fibonacci:
    def __init__(self):
        self.prev = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.prev, self.current = self.current, self.prev + self.current
        return self.prev


class Square:
    def __init__(self, n):
        self.n = n
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.n:
            raise StopIteration
        return self.start**2


class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == self.times:
            raise StopIteration
        return self.obj

# geek = BoundedRepeater('geek', 3)
#
# print(next(geek))
# print(next(geek))
# print(next(geek))
#
# try:
#     print(next(geek))
# except StopIteration:
#     print('Error')


class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    return filter(lambda x: x not in filter(predicate, iterable), iterable)


def transpose(matrix):
    return [list(i) for i in zip(*matrix)]


def get_min_max(data):
    if not data:
        return None
    iterator = iter(data)
    try:
        start = next(iterator)
        mindata, maxdata = start, start
        for dt in iterator:
            if dt > maxdata:
                maxdata = dt
            elif dt < mindata:
                mindata = dt
        return mindata, maxdata
    except:
        return None

def starmap(funk, iterable):
    return map(funk, *zip(*iterable))
    # return map(lambda x: func(*x), iterable)


def is_iterable(obj):
    return '__iter__' in dir(obj)


def is_iterator(obj):
    return '__next__' in dir(obj) and '__iter__' in dir(obj)


def random_numbers(left, right):
    return iter(lambda: randint(left, right), right+1)




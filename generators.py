from datetime import date, timedelta
from operator import mul
from string import ascii_uppercase
from itertools import groupby, accumulate, count, cycle, zip_longest, dropwhile, takewhile, filterfalse, islice, compress, chain, tee, repeat


def ranges(numbers):
    key_f = lambda x: numbers.index(x) - x
    res = []
    for key, data in groupby(numbers, key=key_f):
        lst = list(data)
        res.append((min(lst), max(lst)))
    return res


def group_anagrams(words):
    key_f = lambda x: sorted(x)
    group_words = groupby(sorted(words, key=key_f), key=key_f)
    return (tuple(w) for k, w in group_words)


def grouper(iterable, n):
    return zip_longest(*repeat(iter(iterable), n))
    # return zip_longest(*[iter(iterable)] * n)


def ncycles(iterable, times):
    yield from chain.from_iterable(tee(iterable, times))


def max_pair(iterable):
    return max(map(lambda x: sum(x), pairwise(iterable)))


def is_rising(iterable):
    return all(map(lambda x: x[0] < x[1], pairwise(iterable)))


def sum_of_digits(iterable):
    """сумма цифр всех чисел"""
    return sum(map(int, chain.from_iterable(map(str, iterable))))


def first_largest(iterable, num):
    for i, elem in enumerate(iterable):
        if elem >= num:
            return i
    return -1
    # return next(dropwhile(lambda x: x[1] <= num, enumerate(iterable)), [-1])[0]


def take_nth(iterable, n):
    for i in islice(iterable, n-1, n):
        return i
    # return next(islice(iterable, n - 1, None), None)


def take(iterable, n):
    yield from islice(iterable, n)


def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool
    # for i in iterable:
    #     if predicate(i):
    #         return True
    # return None
    return next(dropwhile(lambda x: not predicate(x), iterable), None)


def drop_this(iterable, obj):
    for i in dropwhile(lambda x: x == obj, iterable):
        yield i


def drop_while_negative(iterable):
    for i in dropwhile(lambda x: x < 0, iterable):
        yield i


def tabulate(func):
    for x in count(1):
        yield func(x)


def factorials(n):
    yield from accumulate(range(1, n+1), func=mul)


def alnum_sequence():
    for i in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
        yield from i


def roundrobin(*args):
    for item in zip_longest(*args, fillvalue=''):
        for i in item:
            if i == '':
                continue
            else:
                yield i


def parse_ranges(ranges):
    gen1 = (i for i in ranges.split(','))
    gen2 = (i.split('-') for i in gen1)
    return (i for a, b in gen2 for i in range(int(a), int(b)+1))


def filter_names(names: list[str], ignore_char: str, max_names: int):
    goodnames = (name for name in names if name.isalpha()
                 and name.lower()[0] != ignore_char.lower())
    return (name for i, name in enumerate(goodnames) if i < max_names)


# with open('data.csv', encoding='utf-8') as file:
#     data = csv.DictReader(file, delimiter=',')
#     filt_data = (int(line['raisedAmt']) for line in data if line['round'] == 'a')
#     print(sum(filt_data))


def number_of_days(year):
    if year % 4 != 0:
        return 365
    elif year % 100 == 0:
        if year % 400 == 0:
            return 366
        return 365


def years_days(year):
    start = date(day=1, month=1, year=year)
    return (start + timedelta(days=i) for i in range(number_of_days(year)))


def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as file:
        data = (line.strip('\n') for line in file)
        filt_data = (line for line in data if line != '')
        yield from (line if len(line) <= 25 else '...' for line in filt_data)


def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as file:
        data = (line.split('\n') for line in file.read().split('\n\n'))
        return (dict(l.split(' = ') for l in planet) for planet in data)


def unique(iterable):
    cash = {}
    for i in iterable:
        if i not in cash:
            cash[i] = True
            yield i


def stop_on(iterable, obj):
    for i in iterable:
        if i == obj:
            break
        yield i


def with_previous(iterable):
    prev = None
    for i in iterable:
        yield i, prev
        prev = i


def pairwise(iterable):
    it = iter(iterable)
    b = next(it, None)
    c = next(it, None)
    while b is not None:
        yield b, c
        b, c = c, next(it, None)
        

def around(iterable):
    it = iter(iterable)
    a = None
    b = next(it, None)
    c = next(it, None)
    while b is not None:
        yield a, b, c
        a, b, c = b, c, next(it, None)
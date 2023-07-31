def intersperse(iterable, delimiter):
    iterator = iter(iterable)
    yield next(iterator, '')
    for i in iterator:
        yield delimiter
        yield i

print(*intersperse([1, 2, 3], 0))
print(*intersperse('beegeek', '!'))
print(*intersperse('A', '...'))
data = intersperse(['John Warner Backus', 5, 'Niklaus Emil Wirth', True, 'Lawrence Gordon Tesler', None, {1, 2, 3}, {'hello': 'world'}], '—')
print(list(data))
# TEST_7:
print(*intersperse([], 100))

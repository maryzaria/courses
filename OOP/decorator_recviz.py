import functools


def recviz(funk):
    count = 0

    @functools.wraps(funk)
    def wrapper(*args, **kwargs):
        nonlocal count
        kwarg = [f'{key}={repr(value)}' for key, value in kwargs.items()]
        print(f'{"    " * count}-> {funk.__name__}({", ".join(list(map(repr, args)) + kwarg)})')
        count += 1
        res = funk(*args, **kwargs)
        count -= 1
        print(f'{"    " * count}<- {repr(res)}')
        return res

    return wrapper


@recviz
def add(a, b, c, d, e):
    return (a + b + c) * (d + e)

add('a', b='b', c='c', d=3, e=True)

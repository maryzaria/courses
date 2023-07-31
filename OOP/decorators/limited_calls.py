import functools


class MaxCallsException(Exception):
    pass


class limited_calls:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.n -= 1
            if self.n < 0:
                raise MaxCallsException('Превышено допустимое количество вызовов')
            return func(*args, **kwargs)
        return wrapper


@limited_calls(3)
def add(a, b):
    return a + b


# print(add(1, 2))
print(add(3, 4))
print(add(5, 6))
print(add(1,2))
try:
    print(add(1,2))
except MaxCallsException as e:
    print(e)
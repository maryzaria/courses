import functools


class type_check:
    def __init__(self, types):
        self.errors = types[:]

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not all(isinstance(arg, erg_type) for arg, erg_type in zip(args, self.errors)):
                raise TypeError
            return func(*args, **kwargs)
        return wrapper


@type_check([int, int])
def add(a, b):
    return a + b

try:
    print(add(1, '2'))
except Exception as error:
    print(type(error))
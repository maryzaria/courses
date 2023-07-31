import functools


class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        if not all(isinstance(arg, (int, float)) for arg in args) or \
                not all(isinstance(val, (int, float)) for val in kwargs.values()):
            raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)


@takes_numbers
def mul(a, b):
    return a * b


try:
    print(mul(1, '2'))
except TypeError as error:
    print(error)
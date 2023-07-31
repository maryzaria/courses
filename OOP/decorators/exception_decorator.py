import functools


class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs), None
        except Exception as e:
            return None, e


@exception_decorator
def f(x, y):
    return x * y


print(f('stepik', 10))
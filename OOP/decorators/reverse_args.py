import functools


def reverse_args1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args = reversed(args)
        return func(*args, **kwargs)
    return wrapper


class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        args = reversed(args)
        return self.func(*args, **kwargs)
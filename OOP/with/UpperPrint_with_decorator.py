class UpperPrint:
    def __enter__(self):
        global print
        self.old_print = print
        print = print_decorator(print)

    def __exit__(self, exc_type, exc_val, exc_tb):
        global print
        print = self.old_print


def print_decorator(funk):
    def wrapper(*args, **kwargs):
        args = tuple(map(lambda x: x.upper() if isinstance(x, str) else x, args))
        kwargs = {k: v.upper() if isinstance(v, str) else v for k, v in kwargs.items()}
        return funk(*args, **kwargs)
    return wrapper


with UpperPrint():
    print('Bee', 'Geek', 'Love', sep=' one ', end=' end')
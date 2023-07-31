from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    try:
        file = open(filename, mode=mode)
        yield file, None
    except Exception as error:
        return None, error
    else:
        file.close()



import functools
from functools import wraps, partial, update_wrapper


class MaxRetriesException(Exception):
    pass


to_Timur = partial(send_email, name='Тимур', email_address='timyrik20@beegeek.ru')
send_an_invitation = partial(send_email, text='Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....')
con_class = partial(range, 0, 101)


def apply(*apargs, **apkwargs):
    def decor(funk):
        return funk(*apargs, **apkwargs)
    return decor
@apply(2, 3)
def multiply(x, y):
    return x * y


print(multiply, type(multiply))


def decorator(wanna_be_decorator):
    def res_decorator(funk):
        def wrapper(*args, **kwargs):
            return wanna_be_decorator(funk, *args, **kwargs)
        return wrapper
    return res_decorator


def parametrized(init_deco):
    """ декоратор для декаратора, который позволяет уменьшить степень вложенности декоратора,
    но теперь он может принимать доп. параметры decargs, dekwargs"""

    def param_deco(*decargs, **dekwargs):
        def res_deco(funk):
            return init_deco(funk, *decargs, **dekwargs)
        return res_deco
    return param_deco

@parametrized
def introduce(funk, n, newline=True):
    @wraps(funk)
    def wrapper(*args, **kwargs):
        print(('\n' if newline else ' ').join([funk.__name__] * n))
        return funk(*args, **kwargs)
    return wrapper


def retry(times):
    def decorator(funk):
        @wraps(funk)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    res = funk(*args, **kwargs)
                    return res
                except:
                    pass
            raise MaxRetriesException
        return wrapper
    return decorator


# @retry(8)
# def beegeek():
#     beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
#     if beegeek.calls < 5:
#         raise ValueError
#     print('beegeek')
# beegeek()


def ignore_exception(*errors):
    def decorator(funk):
        @wraps(funk)
        def wrapper(*args, **kwargs):
            try:
                res = funk(*args, **kwargs)
                return res
            except Exception as err:
                if type(err) not in errors:
                    raise err
                else:
                    print(f'Исключение {type(err).__name__} обработано')
        return wrapper
    return decorator


def add_attrs(**data):
    def decorator(funk):
        for k, v in data.items():
            funk.__dict__[k] = v
        @wraps(funk)
        def wrapper(*args, **kwargs):

            res = funk(*args, **kwargs)
            return res
        return wrapper
    return decorator
# @add_attrs(attr2='geek')
# @add_attrs(attr1='bee')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek.attr1)
# print(beegeek.attr2)
# print(beegeek.__name__)

def takes(*datatypes):
    def decorator(funk):
        @wraps(funk)
        def wrapper(*args, **kwargs):
            res = funk(*args, **kwargs)
            if not all(map(lambda x: type(x) in datatypes, (*args, *kwargs.values()))):
                raise TypeError
            return res
        return wrapper
    return decorator
# @takes(list, bool, float, int)
# def repeat_string(string, times):
#     return string * times
#
# try:
#     print(repeat_string('bee', 4))
# except TypeError as e:
#     print(type(e))

def returns(datatype):
    def decorator(funk):
        @wraps(funk)
        def wrapper(*args, **kwargs):
            res = funk(*args, **kwargs)
            if not isinstance(res, datatype):
                raise TypeError
            return res
        return wrapper
    return decorator
# @returns(int)
# def add(a, b):
#     return a + b
#
# try:
#     print(add('199', '1'))
# except TypeError as e:
#     print(type(e))

def strip_range(start, end, char='.'):
    def decorator(funk):
        @wraps(funk)
        def wrapper(*args, **kwargs):
            res = funk(*args, **kwargs)
            new = list(res)
            for i, arg in enumerate(res):
                if i in range(start, end+1):
                    new[i] = char
            return ''.join(new)
        return wrapper
    return decorator


# @strip_range(13, 25)
# def beegeek():
#     return 'beegeek'


# print(beegeek())

def repeat(times):
    def decorator(funk):
        @wraps(funk)
        def wrapper(*args, **kwargs):
            for _ in range(times-1):
                funk(*args, **kwargs)
            return funk(*args, **kwargs)
        return wrapper
    return decorator

# @repeat(3)
# def say_beegeek():
#     '''documentation'''
#     print('beegeek')
#
# say_beegeek()

def make_html(string):
    def decorator(funk):
        @wraps(funk)
        def wrapper(*args, **kwargs):
            res = funk(*args, **kwargs)
            start = f'<{string}>'
            end = f'</{string}>'
            return start + res + end
        return wrapper
    return decorator


def trace(funk):
    @wraps(funk)
    def wrapper(*args, **kwargs):
        res = funk(*args, **kwargs)
        print(f'''TRACE: вызов {funk.__name__}() с аргументами: {tuple(args)}, {kwargs}
TRACE: возвращаемое значение {funk.__name__}(): {res}''')
        return res
    return wrapper
# @trace
# def say(name, line):
#     return f'{name}: {line}'
#
#
# say('Jane', 'Hello, World')

def returns_string(funk):
    @wraps(funk)
    def wrapper(*args, **kwargs):
        res = funk(*args, **kwargs)
        if not isinstance(res, str):
            raise TypeError
        return res
    return wrapper


def square(funk):
    @wraps(funk)
    def wrapper(*args, **kwargs):
        return funk(*args, **kwargs) ** 2
    return wrapper


def memoized(funk):
    memory = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        memory.setdefault(key, funk(*args, **kwargs))
        return memory[key]
    return wrapper


def flip(funk):
    def wrapper(*args, introduce=False, **kwargs):
        if introduce:
            print(funk.__name__)
        return funk(*args,  **kwargs)
    return wrapper


def sandwich(funk):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        res = funk(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return res
    return wrapper


def new_print(funk):
    def wrapper(*args, **kwargs):
        args = [arg.upper() if isinstance(arg, str) else arg for arg in args]
        kwargs = {k: v.upper() if isinstance(v, str) else v for k, v in kwargs.items()}
        return funk(*args, **kwargs)
    return wrapper


def do_twice(funk):
    def wrapper(*args, **kwargs):
        funk(*args, **kwargs)
        return funk(*args, **kwargs)
    return wrapper


def exception_decorator(funk):
    def wrapper(*args, **kwargs):
        try:
            res = funk(*args, **kwargs)
            return res, f'Функция выполнилась без ошибок'
        except:
            return None, 'При вызове функции произошла ошибка'
    return wrapper


def takes_positive(funk):
    def wrapper(*args, **kwargs):
        if not all(map(lambda x: isinstance(x, int), (*args, *kwargs.values()))):
            raise TypeError
        elif not all(map(lambda x: x > 0, (*args, *kwargs.values()))):
            raise ValueError
        return funk(*args, **kwargs)
    return wrapper

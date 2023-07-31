from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def _format_int(arg):
        print(f'Целое число: {arg}')

    @format.register(float)
    @staticmethod
    def _format_float(arg):
        print(f'Вещественное число: {arg}')

    @format.register
    @staticmethod
    def _format_list(arg: list):
        print(f'Элементы списка: {", ".join(map(str, arg))}')

    @format.register
    @staticmethod
    def _format_tuple(arg: tuple):
        print(f'Элементы кортежа: {", ".join(map(str, arg))}')

    @format.register
    @staticmethod
    def _format_dict(arg: dict):
        print(f'Пары словаря: {", ".join(map(str, arg.items()))}')


Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})
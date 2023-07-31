from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _neg_num(arg):
        return -1 * arg

    @neg.register(bool)
    @staticmethod
    def _neg_bool(arg):
        return not arg


print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))
# Sample Output 1:
# Sample Input 2:

try:
    Negator.neg('number')
except TypeError as e:
    print(e)
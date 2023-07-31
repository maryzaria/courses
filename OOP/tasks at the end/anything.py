class AnythingHelper:
    def __eq__(self, other):
        return True

    __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__


def anything():
    return AnythingHelper()


import math, re

print(anything() != [])
print(anything() < 'World')
print(anything() > 81)
print(anything() >= re)
print(anything() <= math)
print(anything() == ord)
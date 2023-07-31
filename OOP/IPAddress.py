from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, *args):
        raise TypeError

    @__init__.register(str)
    def _(self, ipaddress):
        self.n1, self.n2, self.n3, self.n4 = map(int, ipaddress.split('.'))

    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, ipaddress):
        self.n1, self.n2, self.n3, self.n4 = ipaddress

    def __str__(self):
        return f'{self.n1}.{self.n2}.{self.n3}.{self.n4}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.n1}.{self.n2}.{self.n3}.{self.n4}')"


ip = IPAddress((1, 1, 11, 11))

print(str(ip))
print(repr(ip))


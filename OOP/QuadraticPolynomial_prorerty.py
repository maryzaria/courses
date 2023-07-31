class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self._d = self.b **2 - 4 * self.a * self.c

    @classmethod
    def from_iterable(cls, iterable):
        a, b, c = iterable
        return cls(a, b, c)

    @classmethod
    def from_str(cls, string):
        a, b, c = tuple(map(float, string.split()))
        return cls(a, b, c)

    @property
    def x1(self):
        if self._d < 0:
            return None
        return (- self.b - self._d ** 0.5) / 2 / self.a

    @property
    def x2(self):
        if self._d < 0:
            return None
        elif self._d == 0:
            return self.x1
        return (- self.b + self._d ** 0.5) / 2 / self.a

    @property
    def view(self):
        return f'{self.a}x^2 {"+" if self.b >= 0 else "-"} {abs(self.b)}x {"+" if self.c >= 0 else "-"} {abs(self.c)}'

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, coefs):
        self.a, self.b, self.c = coefs
        self._d = self.b ** 2 - 4 * self.a * self.c



# TEST_4:
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

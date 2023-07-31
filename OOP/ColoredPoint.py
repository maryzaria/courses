class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, '{self.color}')"

    @property
    def _tuple_attrs(self):
        return self.x, self.y, self.color

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self._tuple_attrs == other._tuple_attrs
        return NotImplemented

    def __hash__(self):
        return hash(self._tuple_attrs)


point = ColoredPoint(1, 2, 'white')

try:
    point.color = 'black'
except AttributeError as e:
    print('Error')
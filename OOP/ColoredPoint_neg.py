class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.color})"

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __neg__(self):
        return ColoredPoint(-self.x, -self.y, self.color)

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)

    def __invert__(self):
        a, b, c = self.color
        return ColoredPoint(self.y, self.x, (255 - a, 255 - b, 255 - c))


# TEST_5:
point = ColoredPoint(0, 0, (0, 0, 0))

print(f'{+point}; {-point}; {~point}')
print(point.color)

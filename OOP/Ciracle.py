from math import pi


class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = 2 * self._radius
        self._area = pi * self._radius ** 2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area

    @classmethod
    def square(cls, side):
        return cls(side, side)

circle = Circle(1)

print(circle.get_radius())
print(circle.get_diameter())
print(round(circle.get_area()))
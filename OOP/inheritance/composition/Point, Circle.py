class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Circle:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center

    def __str__(self):
        return f'{str(self.center)}, r = {self.radius}'


point = Point(1, 1)
circle = Circle(5, point)

print(point)
print(circle)

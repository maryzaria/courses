from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(default=0, compare=False)

    def __post_init__(self):
        if self.x > 0 and self.y != 0:
            self.quadrant = (1, 4)[self.y < 0]
        elif self.x < 0 and self.y != 0:
            self.quadrant = (2, 3)[self.y < 0]

    def symmetric_x(self):
        return Point(self.x, -self.y)

    def symmetric_y(self):
        return Point(-self.x, self.y)


point = Point(1.0, 2.0)

print(point.symmetric_x())
print(point.symmetric_y())
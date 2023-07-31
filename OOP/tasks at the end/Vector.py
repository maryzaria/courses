from math import sqrt


class Vector:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return f'({", ".join(map(str, self.args))})'

    def __eq__(self, other):
        self.__prov(other)
        if isinstance(other, Vector):
            return self.args == other.args
        return NotImplemented

    def __prov(self, other):
        if not len(self.args) == len(other.args):
            raise ValueError('Векторы должны иметь равную длину')

    def __add__(self, other):
        self.__prov(other)
        return Vector(*(x + y for x, y in zip(self.args, other.args)))

    def __sub__(self, other):
        self.__prov(other)
        return Vector(*(x - y for x, y in zip(self.args, other.args)))

    def __mul__(self, other):
        self.__prov(other)
        return sum(x * y for x, y in zip(self.args, other.args))

    def norm(self):
        return sqrt(sum(x ** 2 for x in self.args))


# TEST_8:
coordinates = [((64, 42, 11), (20, 40, 64)), ((50, 96, 60), (32, 26, 38)), ((46, 95, 64), (23, 70, 78)),
               ((22, 29, 48), (21, 50, 31)), ((40, 50, 19), (95, 37, 78)), ((74, 21, 77), (74, 21, 77)),
               ((55, 33, 88), (55, 33, 88)), ((99, 50, 74), (77, 28, 87)), ((64, 65, 33), (24, 73, 76)),
               ((63, 12, 36), (80, 53, 22)), ((92, 15, 80), (48, 42, 17)), ((84, 65, 80), (72, 15, 46)),
               ((54, 48, 52), (68, 25, 26)), ((37, 93, 12), (16, 76, 42)), ((45, 91, 87), (46, 91, 58)),
               ((33, 74, 85), (13, 20, 36)), ((63, 12, 43), (63, 12, 43)), ((87, 67, 41), (41, 82, 52)),
               ((10, 63, 68), (54, 36, 65)), ((74, 51, 90), (30, 25, 90))]

for coord1, coord2 in coordinates:
    vector1 = Vector(*coord1)
    vector2 = Vector(*coord2)
    print(vector1 == vector2, vector1 != vector2)

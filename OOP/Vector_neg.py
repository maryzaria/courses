class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __bool__(self):
        if self.x == 0 and self.y == 0:
            return False
        return True

    def __int__(self):
        return int(self.__abs__())

    def __float__(self):
        return float(self.__abs__())

    def __complex__(self):
        return complex(self.x, self.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __pos__(self):
        return Vector(self.x, self.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# TEST_3:
vector = Vector(0, 0)
print(bool(vector))
print(int(vector))
print(float(vector))
print(complex(vector))

# TEST_4:
coordinates = [(492, 166), (429, 19), (366, 499), (90, 231), (64, 252), (188, 344), (86, 381), (429, 408), (406, 348),
               (15, 344), (181, 295), (255, 61), (342, 332), (8, 418), (195, 45), (74, 344), (213, 27), (243, 302),
               (74, 253), (487, 52), (314, 427), (391, 346), (128, 101), (116, 373), (186, 55), (328, 395), (65, 232),
               (427, 36), (228, 274), (255, 275), (369, 432), (300, 227), (106, 131), (282, 304), (18, 247), (377, 433),
               (79, 185), (445, 372), (73, 494), (436, 269), (107, 2), (356, 263), (91, 175), (427, 96), (366, 126),
               (17, 363), (188, 309), (408, 346), (427, 278), (304, 108), (139, 267), (91, 67), (260, 393), (144, 81),
               (16, 210), (282, 30), (118, 14), (413, 274), (230, 317), (365, 14), (129, 8), (341, 430), (463, 36),
               (276, 186), (150, 134), (299, 319), (106, 244), (323, 22), (153, 42), (298, 99), (348, 348), (153, 492),
               (374, 11), (168, 374), (303, 222), (170, 30), (17, 259), (402, 93), (291, 290), (296, 432), (401, 179),
               (179, 1), (128, 175), (370, 364), (468, 273), (106, 482), (492, 115), (404, 196), (381, 19), (287, 393),
               (398, 419), (174, 457), (287, 111), (351, 338), (268, 286), (28, 139), (334, 387), (242, 205),
               (103, 315), (455, 269)]

for x, y in coordinates:
    vector = Vector(x, y)
    print(f'Вектор с координатами {vector}:')
    print(f'bool = {bool(vector)};', f'int = {int(vector)};', f'float = {float(vector)};', f'complex = {complex(vector)}')
    print()
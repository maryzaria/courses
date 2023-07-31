class FieldTracker:
    def __init__(self):
        self._dct = dict((k, self.__dict__[k]) for k in self.fields)

    def base(self, name):
        return self._dct[name]

    def has_changed(self, name):
        return self._dct[name] != self.__dict__[name]

    def changed(self):
        return dict((k, self._dct[k]) for k in self.fields if self.has_changed(k))

    def save(self):
        self._dct = dict((k, self.__dict__[k]) for k in self.fields)


# TEST_6:
class Point(FieldTracker):
    fields = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()


p = Point(1, 2, 3)
print(p.base('x'))
p.x = 4
print(p.base('x'))
print(p.x)
p.z = 6
print(p.base('x'))
print(p.base('y'))
print(p.base('z'))
p.save()
print(p.base('x'))
print(p.base('y'))
print(p.base('z'))
p.y = 8
print(p.base('y'))
print(p.y)
p.save()
print(p.base('y'))
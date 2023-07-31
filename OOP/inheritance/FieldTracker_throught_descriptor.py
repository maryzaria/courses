class Descriptor:
    def __init__(self, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if not isinstance(obj.__dict__[self._attr], list):
            obj.__dict__[self._attr] = [obj.__dict__[self._attr]]
            return obj.__dict__[self._attr][-1]
        if not self._attr in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr][-1]

    def __set__(self, obj, value):
        if not self._attr in obj.__dict__:
            obj.__dict__[self._attr] = []
        obj.__dict__[self._attr].append(value)


class FieldTracker:
    def __init__(self):
        for attr in self.fields:
            setattr(FieldTracker, attr, Descriptor(attr))
        for attr in self.fields:
            getattr(self, attr)

    def base(self, name):
        return self.__dict__[name][-1] if not self.has_changed(name) else self.__dict__[name][0]

    def has_changed(self, name):
        return len(self.__dict__[name]) > 1

    def changed(self):
        return dict((k, v[0]) for k, v in self.__dict__.items() if self.has_changed(k))

    def save(self):
        self.__dict__ = dict((k, [v[-1]]) for k, v in self.__dict__.items())


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
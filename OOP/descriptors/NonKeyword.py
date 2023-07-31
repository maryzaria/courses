from keyword import kwlist


class NonKeyword:
    def __init__(self, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if value not in kwlist:
            obj.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')


class Student:
    name = NonKeyword('name')

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)
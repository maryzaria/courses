class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._attr = name
        self._default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = obj.__dict__.get(self._attr)
        if value is self._default:
            raise AttributeError('Атрибут не найден')
        if value is None:
            return self._default
        return value

    def __set__(self, obj, value):
        if isinstance(value, int) and value >= 0:
            obj.__dict__[self._attr] = value
        else:
            raise ValueError('Некорректное значение')


class Student:
    score = NonNegativeInteger('score', 0)

student = Student()

print(student.score)

# TEST_3:
class Student:
    score = NonNegativeInteger('score')

student = Student()

try:
    print(student.score)
except AttributeError as e:
    print(e)

# TEST_4:
class Student:
    score = NonNegativeInteger('score')

student = Student()

try:
    student.score = -90
except ValueError as e:
    print(e)

# TEST_5:
class Student:
    score = NonNegativeInteger('score')

student = Student()
student.score = 90

try:
    student.score = -90
except ValueError as e:
    print(e)

# TEST_6:
class Student:
    score = NonNegativeInteger('score')

student = Student()

not_supported = [1.2, {1: 'one'}, {1, 2, 3}, [4, 5, 6], (7, 8, 9), '14']

for item in not_supported:
    try:
        student.score = item
    except ValueError as e:
        print(e)
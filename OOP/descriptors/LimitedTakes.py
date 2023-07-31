class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self.times = times
        self._count = 0

    def __set_name__(self, cls, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            self._count += 1
            if self._count > self.times:
                raise MaxCallsException('Превышено количество доступных обращений')
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value


# TEST_3:
class Programmer:
    name = LimitedTakes(1)


programmer = Programmer()

try:
    print(programmer.name)
except AttributeError as e:
    print(e)

# TEST_4:
class Programmer:
    name = LimitedTakes(1000)


programmer = Programmer()
programmer.name = 'Gvido'

for _ in range(1000):
    programmer.name

try:
    print(programmer.name)
except MaxCallsException as e:
    print(e)

# TEST_5:
class Student:
    name = LimitedTakes(3)


class Programmer:
    name = LimitedTakes(1)


student = Student()
programmer = Programmer()

student.name = 'Gwen'
programmer.name = 'Mantrida'

for _ in range(3):
    print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)


print(programmer.name)

try:
    print(programmer.name)
except MaxCallsException as e:
    print(e)

# TEST_6:
class Student:
    first_name = LimitedTakes(3)
    last_name = LimitedTakes(1)


student = Student()

student.first_name = 'Gwen'
student.last_name = 'Stacy'


for _ in range(3):
    print(student.first_name)

try:
    print(student.first_name)
except MaxCallsException as e:
    print(e)

print(student.last_name)
try:
    print(student.last_name)
except MaxCallsException as e:
    print(e)

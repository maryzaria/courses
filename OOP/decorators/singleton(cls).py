import functools


def singleton(cls):
    old_new = cls.__new__
    cls._instanse = None

    @functools.wraps(old_new)
    def changes(cls, *args, **kwargs):
        if cls._instanse is None:
            cls._instanse = old_new(cls)
        return cls._instanse

    cls.__new__ = changes
    return cls


# TEST_3:
@singleton
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


instances = [Person('John Doe') for _ in range(1000)]
person = Person('Doe John')
print(person)
print(instances[389])
print(all(instance is person for instance in instances))

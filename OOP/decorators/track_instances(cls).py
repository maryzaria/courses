import functools


def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = new_init
    return cls


# TEST_2:
@track_instances
class Cat:
    def __init__(self, name, breed):
        """cat init"""
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f'Cat({self.name!r}, {self.breed!r})'


for _ in range(10):
    cat = Cat('Кемаль', 'Британский')

print(len(Cat.instances))
print(Cat.__init__.__name__)
print(Cat.__init__.__doc__)
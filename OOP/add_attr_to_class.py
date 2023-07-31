def add_attr_to_class(**kwargs):
    def decorator(cls):
        for key, val in kwargs.items():
            setattr(cls, key, val)
        return cls
    return decorator


class add_attr_to_class:
    def __init__(self, **kwargs):
        self.attrs = kwargs

    def __call__(self, cls):
        for attr_name, attr_value in self.attrs.items():
            setattr(cls, attr_name, attr_value)
        return cls



# TEST_3:
data = {'name': 'John', 'surname': 'Doe'}


@add_attr_to_class(**data)
class Person:
    def __init__(self, name=None, surname=None):
        self.name = name or self.name
        self.surname = surname or self.surname


person = Person()
print(person.name)
print(person.surname)
print(person.__dict__)
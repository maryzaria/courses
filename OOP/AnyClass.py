class AnyClass:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self._string = ', '.join(f"{key}={repr(value)}" for key, value in kwargs.items())

    def __str__(self):
        return f'{self.__class__.__name__}: {self._string}'

    def __repr__(self):
        return f"{self.__class__.__name__}({self._string})"


# TEST_6:
attrs = {
    'name': 'Guido van Rossum',
    'birth_date': '31.01.1956',
    'age': 67,
    'career': 'python guru'
}
obj = AnyClass(**attrs)
print(obj.__dict__)
print(obj.name)
print(obj.birth_date)
print(obj.age)
print(obj.career)


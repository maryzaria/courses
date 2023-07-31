class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        for key, val in kwargs.items():
            setattr(self, key, val)
        # self.__dict__.update(kwargs)

    def __getattribute__(self, attr):  # можно без этого метода
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):
        return self.default


god = DefaultObject(default=0, name='Tyr', mythology='scandinavian')

print(god.name)
print(god.mythology)
print(god.age)
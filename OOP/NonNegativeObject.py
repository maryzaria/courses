class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
        # self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        if type(value) in (int, float) and value < 0:
            value = abs(value)
        object.__setattr__(self, key, value)




point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')

print(point.x)
print(point.y)
print(point.z)
print(point.color)
def auto_repr(args, kwargs):
    def decorator(cls):
        def new_repr(self):
            res = []
            for attr, val in self.__dict__.items():
                # print(attr)
                if attr in args:
                    res.append(repr(val))
                elif attr in kwargs:
                    res.append(f'{attr}={repr(val)}')
            return f"{cls.__name__}({', '.join(res)})"

        cls.__repr__ = new_repr

        return cls
    return decorator


@auto_repr(args=['x', 'y'], kwargs=['color'])
class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

point = Point(1, 2, color='green')
print(point)
# print(Point.__dict__)
point.x = 10
point.y = 20
print(point)
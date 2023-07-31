from typing import Callable


def snake_case(attrs=False):
    def to_snake(string: str) -> str:
        s = [let if let.isalpha() and let.islower() else '_' + let.lower() for let in string]
        return ''.join(s).strip('_')

    def decorator(cls):
        res = {}
        for attr, value in cls.__dict__.items():
            if not attrs and attr[-1] != '_' and callable(cls.__dict__[attr]):
                res[attr] = value
            elif attrs and attr[-1] != '_':
                res[attr] = value
        for attr, value in res.items():
            delattr(cls, attr)
            setattr(cls, to_snake(attr), value)

        return cls

    return decorator


@snake_case()
class MyClass:
    FirstAttr = 1

    def FirstMethod(self):
        return 1


obj = MyClass()
print(MyClass.__dict__)
print(MyClass.FirstAttr)
print(obj.first_method())
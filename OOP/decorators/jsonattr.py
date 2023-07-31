import json


def jsonattr(filename):
    def decorator(cls):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for key, val in data.items():
            setattr(cls, key, val)
        return cls
    return decorator


with open('test.json', 'w') as file:
    file.write('{"x": 1, "y": 2}')


@jsonattr('test.json')
class MyClass:
    pass


print(MyClass.x)
print(MyClass.y)
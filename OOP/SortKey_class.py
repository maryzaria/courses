class SortKey:
    def __init__(self, *args):
        self._attrs = args

    def __call__(self, class_name):
        return tuple(getattr(class_name, attr) for attr in self._attrs)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(max(users, key=SortKey('name')))
print(max(users, key=SortKey('age')))
print(max(users, key=SortKey('name', 'age')))
print(max(users, key=SortKey('age', 'name')))
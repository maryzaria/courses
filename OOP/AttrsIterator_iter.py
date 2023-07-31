class AttrsIterator:
    def __init__(self, obj):
        self.obj = [(key, val) for key, val in obj.__dict__.items()]
        self.n = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n >= len(self.obj):
            raise StopIteration
        return self.obj[self.n]




class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)
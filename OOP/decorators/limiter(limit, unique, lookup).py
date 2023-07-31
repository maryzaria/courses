def limiter(limit, unique, lookup):
    def decorator(cls):
        examples = {}

        def new_cls(*args, **kwargs):
            inst = cls(*args, **kwargs)
            key = getattr(inst, unique)

            if key in examples:
                inst = examples[key]

            elif len(examples) >= limit:
                inst = list(examples.values())[0] if lookup == 'FIRST' else list(ex.values())[-1]

            examples.setdefault(key, inst)
            return inst
        return new_cls
    return decorator


@limiter(3, 'ID', 'LAST')
class MyClass:
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value

obj1 = MyClass(1, 5)          # создается экземпляр класса с идентификатором 1
obj2 = MyClass(2, 8)          # создается экземпляр класса с идентификатором 2
obj3 = MyClass(3, 10)         # создается экземпляр класса с идентификатором 3

obj4 = MyClass(4, 0)          # превышено ограничение limit, возвращается последний созданный экземпляр
obj5 = MyClass(2, 20)         # возвращается obj2, так как экземпляр с идентификатором 2 уже есть

print(obj4.value)
print(obj5.value)
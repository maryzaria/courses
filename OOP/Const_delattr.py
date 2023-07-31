class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, name, value):
        if name not in self.__dict__:
            object.__setattr__(self, name, value)
        else:
            raise AttributeError('Изменение значения атрибута невозможно')

    def __delattr__(self, name):
        raise AttributeError('Удаление атрибута невозможно')


videogame = Const(name='The Last of Us')

try:
    del videogame.name
except AttributeError as e:
    print(e)
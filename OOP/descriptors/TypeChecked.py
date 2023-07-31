class TypeChecked:
    def __init__(self, *args):
        self.args = args

    def __set_name__(self, cls, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if type(value) in self.args:
            obj.__dict__[self._attr] = value
        else:
            raise TypeError('Некорректное значение')


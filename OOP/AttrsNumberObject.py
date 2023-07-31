class AttrsNumberObject:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __getattr__(self, item):
        if item == 'attrs_num':
            return len(self.__dict__) + 1
        return object.__getattribute__(self, item)




music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)
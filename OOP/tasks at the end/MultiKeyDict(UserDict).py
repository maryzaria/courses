from collections import UserDict


class MultiKeyDict(UserDict):
    def alias(self, key, alias_name):
        if hasattr(self, alias_name) and self.__dict__[alias_name] != key or alias_name not in self.data:
            self.data[alias_name] = self.data[key]
        self.__dict__[alias_name] = key

    def __setitem__(self, key, value):
        if key in self.__dict__:
            self.data[self.__dict__[key]] = value
        self.data[key] = value

    def __missing__(self, key):
        return self.data[self.__dict__[key]]


# TEST_2:
multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
del multikeydict['x']
print(multikeydict['z'])
# TEST_4:
multikeydict = MultiKeyDict(lecture='python', lesson='object oriented programming')

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

del multikeydict['lesson']
print(multikeydict['lesson'])

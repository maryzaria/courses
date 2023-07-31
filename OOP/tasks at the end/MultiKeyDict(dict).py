class MultiKeyDict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keys_alias = {}

    def alias(self, key, alias_name):
        for v in self.keys_alias.values():
            if alias_name in v:
                v.remove(alias_name)
        self.keys_alias.setdefault(key, []).append(alias_name)

    def __getitem__(self, name):
        if self.get(name) is not None:
            return self.get(name)
        for key, val in self.keys_alias.items():
            if name in val:
                return self[key]

    def __setitem__(self, name, value):
        for key, names in self.keys_alias.items():
            if name in names:
                super().__delitem__(key)
                self.setdefault(key, value)

    def __delitem__(self, key):
        if key in self.keys_alias:
            self.setdefault(self.keys_alias[key][0], self[key])
        super().__delitem__(key)


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

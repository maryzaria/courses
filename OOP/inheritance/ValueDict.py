class ValueDict(dict):
    def key_of(self, value):
        for key, val in self.items():
            if val == value:
                return key

    def keys_of(self, value):
        for key, val in self.items():
            if val == value:
                yield key


valuedict = ValueDict({})

print(valuedict.key_of(12))
print(*valuedict.keys_of(33))
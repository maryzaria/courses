class AdvancedList(list):
    def join(self, delimiter=' '):
        return delimiter.join(str(item) for item in self)

    def map(self, func):
        self[:] = [func(item) for item in self]

    def filter(self, func):
        self[:] = [item for item in self if func(item)]


advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.map(lambda x: -x)

print(advancedlist)
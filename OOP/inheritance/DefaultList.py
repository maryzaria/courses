from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable=(), default=None):
        super().__init__(item for item in iterable)
        self.default = default

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default


# TEST_3:
defaultlist = DefaultList()

print(defaultlist)

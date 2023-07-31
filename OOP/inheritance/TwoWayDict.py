from collections import UserDict


class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        super().__setitem__(value, key)


d = TwoWayDict()
d[3] = 8
d[7] = 6
print(d[3], d[8])
print(d[7], d[6])

d.update({9: 7, 8: 2})
print(d[9], d[7])
print(d[8], d[2])
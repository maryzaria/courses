from collections.abc import *


class CustomRange(Collection):
    def __init__(self, *args):
        self._args = []
        for arg in args:
            if isinstance(arg, str):
                a, b = map(int, arg.split('-'))
                self._args.extend(list( range(a, b + 1)))
            else:
                self._args.append(arg)

    def __len__(self):
        return len(self._args)

    def __reversed__(self):
        yield from reversed(self._args)

    def __iter__(self):
        yield from self._args

    def __contains__(self, item):
        return item in self._args

    def __getitem__(self, index):
        return self._args[index]


customrange = CustomRange()

print(len(customrange))
print(*customrange)
print(*reversed(customrange))
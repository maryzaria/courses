from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version):
        self._version = list(map(int, version.split('.')))
        self._version += [0] * (3 - len(self._version))

    def __repr__(self):
        return f"{self.__class__.__name__}('{'.'.join(list(map(str, self._version)))}')"

    def __str__(self):
        return f"{'.'.join(list(map(str, self._version)))}"

    def __eq__(self, other):
        if isinstance(other, Version):
            return self._version == other._version
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Version):
            return self._version > other._version
        return NotImplemented



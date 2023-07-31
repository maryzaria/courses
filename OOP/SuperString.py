class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f"{self.string}"

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, int):
            return SuperString(self.string * n)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, n):
        if isinstance(n, int):
            m = len(self.string) // n
            return SuperString(self.string[:m])
        return NotImplemented

    def __lshift__(self, n):
        if isinstance(n, int):
            if n >= len(self.string):
                return SuperString('')
            return SuperString(self.string[:len(self.string) - n])
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            if n >= len(self.string):
                return SuperString('')
            return SuperString(self.string[n:])
        return NotImplemented


# TEST_4:
s = SuperString('beegeek')
for i in range(9):
    print(f'{s} << {i} =', s << i)

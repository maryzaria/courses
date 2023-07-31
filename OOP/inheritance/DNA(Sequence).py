from collections.abc import *


class DNA(Sequence):
    connect = {
        "T": "A",
        "A": "T",
        "G": "C",
        "C": "G"
    }

    def __init__(self, chain):
        self.chain = chain
        self._data = list((c, self.connect[c]) for c in chain)

    def __contains__(self, item):
        return item in self.chain

    def __str__(self):
        return f'{self.chain}'

    def __len__(self):
        return len(self.chain)

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self.chain[item], self.connect[self.chain[item]]
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, DNA):
            return self.chain == other.chain
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, DNA):
            return self.chain != other.chain
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, DNA):
            return DNA(self.chain + other.chain)
        return NotImplemented

# TEST_8:
dna = DNA('ACG')
print(dna.__eq__(1))
print(dna.__ne__(1.1))
print(dna.__add__([1, 2, 3]))

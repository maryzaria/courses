from copy import deepcopy, copy


class SequenceZip:
    def __init__(self, *args):
        self._args = deepcopy(args) # (item for item in zip(*args))
        # self._seq = zip(*self._args)

    def __len__(self):
        return len(tuple(zip(*self._args)))

    def __iter__(self):
        yield from zip(*self._args)

    def __getitem__(self, index):
        seq = zip(*self._args)
        for _ in range(index):
            next(seq)
        return next(seq)


# TEST_5:
many_large_sequences = [range(100000) for _ in range(100)]
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])

# TEST_6:
sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))

# TEST_7:
data = {'bee': 'bee', 'geek': 'geek'}

sequencezip = SequenceZip(data)
data['python'] = 'python'
print(data)
print(len(sequencezip))
print(list(sequencezip))
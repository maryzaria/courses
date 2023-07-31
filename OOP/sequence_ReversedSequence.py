class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __iter__(self):
        yield from reversed(self.sequence)

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('Индекс должен быть целым числом')
        if index < 0 or index >= len(self.sequence):
            raise IndexError('Неверный индекс')
        return self.sequence[len(self.sequence) - index - 1]


numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)
print(len(reversed_numbers))

numbers.append(6)
numbers.append(7)
print(len(reversed_numbers))
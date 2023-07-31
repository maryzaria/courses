from abc import ABC, abstractmethod


class Progression(ABC):
    def __init__(self, start, step):
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass


class ArithmeticProgression(Progression):
    def __next__(self):
        res = self.start
        self.start += self.step
        return res


class GeometricProgression(Progression):
    def __next__(self):
        res = self.start
        self.start *= self.step
        return res


# TEST_6:
progression = GeometricProgression(100, 10)
count = 0

for item in progression:
    if count == 20:
        break
    count += 1
    print(item, end=' ')
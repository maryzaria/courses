from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=()):
        self._data = list(iterable[:])

    def add(self, item):
        self._data.append(item)

    def clear(self):
        self._data.clear()

    @abstractmethod
    def result(self):
        pass


class MinStat(Stat):
    def result(self):
        return min(self._data, default=None)


class MaxStat(Stat):
    def result(self):
        return max(self._data, default=None)


class AverageStat(Stat):
    def result(self):
        return sum(self._data) / len(self._data) if self._data else None


minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
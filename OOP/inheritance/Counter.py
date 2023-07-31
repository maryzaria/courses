class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, num=1):
        self.value += num

    def dec(self, num=1):
        self.value -= num
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def dec(self, num=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        super().__init__(start)
        self.limit = limit

    def inc(self, num=1):
        if self.value + num <= self.limit:
            self.value += num
        else:
            self.value = self.limit

class DoubledCounter(Counter):
    def inc(self, num=1):
        super().inc(num * 2)

    def dec(self, num=1):
        super().dec(num * 2)


counter = LimitedCounter()

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)
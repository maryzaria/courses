class Summator:
    def total(self, n, m=1):
        return sum(i ** m for i in range(1, n + 1))


class SquareSummator(Summator):
    def total(self, n):
        return super().total(n, m=2)


class QubeSummator(Summator):
    def total(self, n):
        return super().total(n, m=3)


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n):
        return super().total(n, m=self.m)


summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))    # 1 + 2 + 3
print(summator2.total(3))    # 1 + 4 + 9
print(summator3.total(3))    # 1 + 8 + 27
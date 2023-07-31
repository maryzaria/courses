class SuperInt(int):
    def repeat(self, n=2):
        return SuperInt(str(self) * n)

    def to_bin(self):
        return f'{self:b}'

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        yield from (SuperInt(num) for num in str(abs(self)))


# TEST_13:
superint1 = SuperInt(2023)
# print(type(superint1))

for item in superint1:
    print(item, type(item))
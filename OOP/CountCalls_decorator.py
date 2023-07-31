class CountCalls:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)


@CountCalls
def square(a):
    return a ** 2


for i in range(100):
    square(i)

print(square.calls)
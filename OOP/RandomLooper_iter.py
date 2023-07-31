from random import shuffle


class RandomLooper:
    def __init__(self, *args):
        self.iterable = [el for arg in args for el in arg]
        shuffle(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable:
            return self.iterable.pop()
        raise StopIteration



colors = ['red', 'blue', 'green', 'purple']
shapes = ['square', 'circle', 'triangle', 'octagon']
randomlooper = RandomLooper(colors, shapes)

print(list(randomlooper))
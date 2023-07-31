class Queue:
    def __init__(self, pairs=()):
        if isinstance(pairs, dict):
            self.queue = [(k, v) for k, v in pairs.items()]
        elif isinstance(pairs, list):
            self.queue = pairs[:]
        else:
            self.queue = []

    def add(self, item):
        for elem in self.queue:
            if elem[0] == item[0]:
                self.queue.remove(elem)
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            raise KeyError('Очередь пуста')
        return self.queue.pop(0)

    def __str__(self):
        return f"{self.__class__.__name__}({self.queue})"

    def __len__(self):
        return len(self.queue)


queue = Queue()

try:
    queue.pop()
except KeyError as error:
    print(error)
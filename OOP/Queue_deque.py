import copy


class Node:
    """Class to represent each node of the deque (linked list)"""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f'{self.data}'


class Queue:
    """A double-ended queue or deque (pronounced “deck”)"""
    def __init__(self, *args):
        self.start = None
        self.end = None
        self.length = 0
        for arg in args:
            self._add(arg)

    def __iter__(self):
        """Return an iterator over items in order from front to back"""
        node = self.start
        if node:
            while node is not None:
                yield node
                node = node.next

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    def _add(self, item):
        """Add only 1 element to the queue"""
        node = Node(item)
        if self.end is None:
            self.start = node
            self.end = node
        else:
            end = self.end
            end.next = node
            node.prev = end
            self.end = node
        self.length += 1

    def add(self, *args):
        """Add multiple elements to the end of the queue"""
        for arg in args:
            self._add(arg)

    def pop(self):
        """Remove the first element of the queue"""
        if self.start is None:
            return None
        res = self.start.data
        self.start = self.start.next
        if self.start:
            self.start.prev = None
        self.length -= 1
        return res

    def __eq__(self, other):
        if isinstance(other, Queue):
            if self.length != other.length:
                return False
            return all(node1.data == node2.data for node1, node2 in zip(self, other))
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Queue):
            res = copy.deepcopy(self)
            for node in other:
                res._add(node.data)
            return res
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            for node in other:
                self._add(node.data)
            return self
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            if self.length <= n:
                return Queue()
            res = copy.deepcopy(self)
            for _ in range(n):
                res.pop()
            return res
        return NotImplemented


queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)

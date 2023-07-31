class TreeBuilder:
    def __init__(self):
        self.tree = []
        self.data = {}
        self.level = 0

    def __enter__(self):
        self.data.setdefault(self.level, []).append([])
        self.level += 1
        self.data[self.level] = self.data[self.level - 1][-1]

    def add(self, item):
        if self.level == 0:
            self.tree.append(item)
        else:
            self.data[self.level].append(item)

    def __exit__(self, *args, **kwargs):
        self.level -= 1
        if not self.data[self.level][-1]:
            self.data[self.level].pop()
        if self.level == 0:
            self.tree.extend(self.data[self.level])
            self.data.clear()

    def structure(self):
        return self.tree

    # ', '.join(f'{k}: {v}' for k, v in self.data.items()),


tree = TreeBuilder()

with tree:
    tree.add(1)
    tree.add(2)
    with tree:
        tree.add(3)
        with tree:
            tree.add(4)
    with tree:
        tree.add(5)

print(tree.structure())
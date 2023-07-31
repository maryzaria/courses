class TreeBuilder:

    def __init__(self):
        self.tree = []
        self.stack = []

    def add(self, data):
        self.tree.append(data)

    def __enter__(self):
        self.stack.append(self.tree)
        self.tree = []

    def __exit__(self, exc_type, exc_val, exc_tb):
        old_tree = self.tree
        self.tree = self.stack.pop()
        if len(old_tree) > 0:
            self.tree.append(old_tree)

    def structure(self):
        return str(self.tree)


tree = TreeBuilder()

tree.add('1st')

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
        with tree:
            tree.add('4th')
            with tree:
                tree.add('5th')
    with tree:
        pass

tree.add('6th')
print(tree.structure())

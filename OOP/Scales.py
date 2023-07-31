class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, m):
        self.right += m

    def add_left(self, m):
        self.left += m

    def get_result(self):
        if self.right > self.left:
            return 'Правая чаша тяжелее'
        elif self.right < self.left:
            return 'Левая чаша тяжелее'
        else:
            return 'Весы в равновесии'

scales = Scales()

scales.add_right(5)
scales.add_left(2)

print(scales.get_result())
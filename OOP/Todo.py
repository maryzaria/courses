class Todo:
    def __init__(self):
        self.things = []
        self.low_priority = 0
        self.high_priority = 0

    def add(self, task: str, num: int) -> None:
        self.things.append((task, num))
        self.low_priority = min(self.things, key=lambda x: x[1])[1]
        self.high_priority = max(self.things, key=lambda x: x[1])[1]

    def get_by_priority(self, n: int) -> list[str]:
        return [task for task, priority in self.things if priority == n]

    def get_low_priority(self) -> list[str]:
        return [task for task, priority in self.things if priority == self.low_priority]

    def get_high_priority(self) -> list[str]:
        return [task for task, priority in self.things if priority == self.high_priority]

todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))
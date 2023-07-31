class Numbers:
    def __init__(self):
        self.nums = []

    def add_number(self, n):
        self.nums.append(n)

    def get_even(self):
        return [num for num in self.nums if num % 2 == 0]

    def get_odd(self):
        return [num for num in self.nums if num % 2]

numbers = Numbers()

numbers.add_number(1)
numbers.add_number(3)
numbers.add_number(1)

print(numbers.get_even())
print(numbers.get_odd())
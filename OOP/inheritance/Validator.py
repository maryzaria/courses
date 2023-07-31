class Validator:
    def __init__(self, obj):
        self.obj = obj

    def is_valid(self):
        return None


class NumberValidator(Validator):
    def is_valid(self):
        if isinstance(self.obj, (int, float)):
            return True
        return False


# TEST_4:
instances = [12, 34.1, [1, 2, 3], {4, 5, 6}, (7, 8, 9), {1: 'one'}, 'this is string', True, False]

for instance in instances:
    validator = NumberValidator(instance)
    print(validator.is_valid())

from copy import copy


class Selfie:
    items = []

    def __init__(self, attrs=()):
        if isinstance(attrs, dict):
            for key, val in attrs.items():
                setattr(self, key, val)

    def save_state(self):
        self.items.append(copy(self.__dict__))

    def recover_state(self, index):
        if index > len(self.items):
            return self
        attrs = Selfie.items[index]
        self.items.clear()
        res = Selfie(attrs)
        self.items.append(res)
        return Selfie(attrs)

    def n_states(self):
        return len(self.items)


# TEST_2:
obj = Selfie()

print(obj.n_states())
obj.x = 0
obj.save_state()
obj.x = 1
obj.save_state()
obj.x = 2
obj.save_state()
print(obj.n_states())
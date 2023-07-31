class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha() and new_name != '':
            self._name = new_name
        else:
            raise ValueError('Некорректное имя')

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 <= new_age <= 110:
            self._age = new_age
        else:
            raise ValueError('Некорректный возраст')


user = User('Гвидо', 67)

print(user.get_name())
print(user.get_age())
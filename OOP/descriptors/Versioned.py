class Versioned:
    def __set_name__(self, cls, name):
        """
        Дескриптор должен закрепляться за атрибутом, имеющим то же имя,
        что и переменная, которой присваивается дескриптор.
        """
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if not self._attr in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr][-1]

    def __set__(self, obj, value):
        if not self._attr in obj.__dict__:
            obj.__dict__[self._attr] = []
        obj.__dict__[self._attr].append(value)

    def get_version(self, obj, n):
        if len(obj.__dict__[self._attr]) >= n:
            return obj.__dict__[self._attr][n - 1]

    def set_version(self, obj, n):
        if len(obj.__dict__[self._attr]) >= n:
            self.__set__(obj, self.get_version(obj, n))


# TEST_7:
class Student:
    age = Versioned()


student1 = Student()
student2 = Student()

student1.age = 18
student1.age = 19
student1.age = 20

student2.age = 30
student2.age = 31
student2.age = 32

print(student1.age)
print(student2.age)
Student.age.set_version(student1, 1)
Student.age.set_version(student2, 1)
print(student1.age)
print(student2.age)

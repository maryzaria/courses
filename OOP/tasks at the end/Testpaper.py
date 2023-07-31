class Testpaper:
    def __init__(self, subject: str, true_res: list[str], min_percent: str) -> None:
        self.subject = subject
        self.true_res = true_res
        self.min_percent = min_percent


class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'
        self._res = {}

    def take_test(self, test: Testpaper, answer: list[str]) -> None:
        test_percent = round(len(list(filter(lambda x: x[0] == x[1], zip(test.true_res, answer)))) / len(answer) * 100)
        score = 'Passed!' if test_percent >= int(test.min_percent.strip('%')) else 'Failed!'
        self._res.setdefault(test.subject, f'{score} ({test_percent}%)')
        self.tests_taken = self._res

# TEST_3:
papers = [
    Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%'),
    Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%'),
    Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%'),
    Testpaper(
        'Informatics',
        ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8A', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
         '18B', '19D', '20D'],
        '90%'
    )
]

student1 = Student()
student2 = Student()

student1.choices = [
    ['1C', '2B', '3D', '4C', '5B'],
    ['1A', '2D', '3A', '4D'],
    ['1B', '2D', '3D', '4C', '5B', '6C', '7C'],
    ['1B', '2A', '3C', '4C', '5A', '6B', '7C', '8B', '9D', '10C', '11A', '12D', '13C', '14A', '15B', '16A', '17C',
     '18B', '19C', '20B']
]

student2.choices = [
    ['1A', '2A', '3A', '4A', '5C'],
    ['1A', '2C', '3C', '4A'],
    ['1A', '2B', '3C', '4A', '5D', '6D', '7D'],
    ['1B', '2A', '3C', '4C', '5A', '6D', '7C', '8D', '9A', '10B', '11D', '12A', '13B', '14B', '15C', '16D', '17A',
     '18A', '19D', '20C']
]

for student in [student1, student2]:
    for i in range(4):
        student.take_test(papers[i], student.choices[i])
print(student1.tests_taken)
print(student2.tests_taken)

# TEST_4:
papers = [
    Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%'),
    Testpaper('Chemistry', ['1C', '2C', '3D', '4A'], '75%'),
    Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%'),
    Testpaper(
        'Informatics',
        ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8A', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
         '18B', '19D', '20D'],
        '90%'
    )
]

student = Student()

student.choices = [
    ['1A', '2C', '3D', '4B', '5A'],
    ['1C', '2A', '3D', '4A'],
    ['1D', '2C', '3C', '4B', '5D', '6A', '7A'],
    ['1A', '2A', '3A', '4A', '5A', '6C', '7A', '8B', '9D', '10B', '11C', '12A', '13C', '14B', '15B', '16B', '17D',
     '18B', '19D', '20D']
]

for i in range(4):
    student.take_test(papers[i], student.choices[i])

print(student.tests_taken)
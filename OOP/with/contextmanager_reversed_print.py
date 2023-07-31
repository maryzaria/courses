from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    standard_output = sys.stdout.write
    sys.stdout.write = lambda x: standard_output(x[::-1])
    yield
    sys.stdout.write = standard_output

# print('masha'[::-1])
# Sample Input 3:

print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with reversed_print():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')
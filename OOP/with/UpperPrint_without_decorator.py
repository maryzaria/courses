import sys


class UpperPrint:
    def __enter__(self):
        # сохраняем исходную функцию
        self.original_write = sys.stdout.write
        # исходная функция sys.stdout.write() подменяется на функцию upper_write()
        sys.stdout.write = self.upper_write
        return self

    def upper_write(self, text):
        # принимает строку в верхнем регистре и выводит на экран
        self.original_write(text.upper())

    def __exit__(self, exc_type, exc_val, exc_tb):
        #  восстанавливаем поведение по умолчанию
        sys.stdout.write = self.original_write


print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with UpperPrint():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')
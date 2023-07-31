from contextlib import contextmanager


@contextmanager
def safe_write(filename):

    new_file = open('help.txt', 'w')
    try:
        yield new_file
    except Exception as error:
        print(f"Во время записи в файл было возбуждено исключение {type(error).__name__}")
        return
    else:
        file = open(filename, 'w')
        new_file.close()
        text = open('help.txt', 'r')
        file.write(text.read())
        file.close()
    finally:
        new_file.close()


with safe_write('poem.txt') as file:
    print('''Я кашлянул в звенящей тишине,
И от шального эха стало жутко…, 
Расскажет ли утятам обо мне,
под утро мной испуганная утка?''', file=file)

with safe_write('poem.txt') as file:
    file.insert('Стихотворение про утку')       # неверный метод для записи в файл

with open('poem.txt') as file:
    print(file.read())

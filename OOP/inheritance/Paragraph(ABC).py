from abc import ABC, abstractmethod


class Paragraph(ABC):
    def __init__(self, length):
        self._length = length
        self.par = []

    def add(self, words):
        self.par.extend(words.split())

    @abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):
    def end(self):
        string = ''
        for word in self.par:
            string += ' ' + word
            if len(string.strip()) > self._length:
                print(' '.join(string.split()[:-1]))
                string = word
        print(string)
        self.par = []


class RightParagraph(Paragraph):
    def end(self):
        string = ''
        for word in self.par:
            string += ' ' + word
            if len(string.strip()) > self._length:
                print(' '.join(string.split()[:-1]).rjust(self._length))
                string = word
        print(string.rjust(self._length))
        self.par = []


# TEST_4:
rightparagraph = RightParagraph(28)
rightparagraph.add('Не стану я жалеть о розах')
rightparagraph.add('Увядших с легкою весной')
rightparagraph.add('Мне мил и виноград на лозах')
rightparagraph.add('В кистях созревший под горой')
rightparagraph.end()

rightparagraph.add('Краса моей долины злачной')
rightparagraph.add('Отрада осени златой')
rightparagraph.add('Продолговатый и прозрачный')
rightparagraph.add('Как персты девы молодой')
rightparagraph.end()

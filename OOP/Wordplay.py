import copy


class Wordplay:
    def __init__(self, words=None):
        self.words = copy.copy(words) if words else []

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [word for word in self.words if len(word) == n]

    def only(self, *args):
        return [word for word in self.words if all(w in args for w in word)]

    def avoid(self, *args):
        return [word for word in self.words if not any(w in args for w in word)]


# TEST_8:
words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)




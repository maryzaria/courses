class TextHandler:
    def __init__(self):
        self.words = []

    def add_words(self, text):
        self.words.extend(text.split())

    def get_shortest_words(self):
        return [word for word in self.words if len(word) == len(min(self.words, key=len))]

    def get_longest_words(self):
        return [word for word in self.words if len(word) == len(max(self.words, key=len))]


texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')
print(texthandler.words)

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
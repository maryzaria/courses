class ReversibleString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f'{self.string}'

    def __neg__(self):
        return ReversibleString(self.string[::-1])


# TEST_3:
string = ReversibleString('')

print(string)
print(-string)

# TEST_4:
string = ReversibleString("Namespaces are one honking great idea -- let's do more of those!")

print(string)
print(-string)


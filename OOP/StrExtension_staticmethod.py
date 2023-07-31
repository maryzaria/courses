class StrExtension:

    @staticmethod
    def remove_vowels(string: str) -> str:
        return ''.join([let for let in string if let not in 'aAeEiIoOuUyY'])

    @staticmethod
    def leave_alpha(string: str) -> str:
        return ''.join([let for let in string if let.isalpha()])

    @staticmethod
    def replace_all(string: str, chars, char) -> str:
        return ''.join([let if let not in chars else char for let in string])


print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))
print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))
print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))

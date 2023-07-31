class RoundedInt(int):
    def __new__(cls, num, even=True, *args, **kwargs):
        if even:
            num = num if not num % 2 else num + 1
        else:
            num = num if num % 2 else num + 1
        return super().__new__(cls, num)
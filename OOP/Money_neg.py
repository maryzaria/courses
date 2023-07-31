class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'{self.amount} руб.'

    def __neg__(self):
        if self.amount > 0:
            return Money(-self.amount)
        return Money(self.amount)

    def __pos__(self):
        return Money(abs(self.amount))


money = Money(0)

print(money)
print(+money)
print(-money)

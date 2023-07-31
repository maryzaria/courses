class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if type(amount) in (int, float):
            self._balance += amount
        else:
            raise ValueError('Некорректное число')

    def withdraw(self, amount):
        if self._balance >= amount and type(amount) in (int, float):
            self._balance -= amount
        else:
            raise ValueError('На счете недостаточно средств')

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)


# TEST_8:
account1 = BankAccount(balance=100)
account2 = BankAccount()
account1.transfer(account2, 100)
print(account1.get_balance())
print(account2.get_balance())
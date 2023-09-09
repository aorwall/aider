class BankAccount:
    def __init__(self):
        self.balance = 0
        self.open = False

    def get_balance(self):
        if not self.open:
            raise ValueError('account not open')
        return self.balance

    def open(self):
        if self.open:
            raise ValueError('account already open')
        self.open = True

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        if not self.open:
            raise ValueError('account not open')
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        if amount > self.balance:
            raise ValueError('amount must be less than balance')
        if not self.open:
            raise ValueError('account not open')
        self.balance -= amount

    def close(self):
        self.open = False
        self.balance = 0

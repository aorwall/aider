class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False

    def open(self):
        if self.is_open:
            raise ValueError('account already open')
        self.is_open = True
        self.balance = 0  # Reset balance to 0 when account is opened

    def close(self):
        if not self.is_open:
            raise ValueError('account not open')
        self.is_open = False

    def get_balance(self):
        if not self.is_open:
            raise ValueError('account not open')
        return self.balance

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        self.balance += amount

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        if amount > self.balance:
            raise ValueError('amount must be less than balance')
        self.balance -= amount

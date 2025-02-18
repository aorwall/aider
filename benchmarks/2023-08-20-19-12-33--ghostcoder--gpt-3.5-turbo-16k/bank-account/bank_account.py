from threading import Lock

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False
        self.lock = Lock()

    def get_balance(self):
        if not self.is_open:
            raise ValueError('account not open')
        return self.balance

    def open(self):
        if self.is_open:
            raise ValueError('account already open')
        self.is_open = True

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        with self.lock:
            if amount > self.balance:
                raise ValueError('amount must be less than balance')
            self.balance -= amount

    def close(self):
        if not self.is_open:
            raise ValueError('account not open')
        self.is_open = False
        self.balance = 0
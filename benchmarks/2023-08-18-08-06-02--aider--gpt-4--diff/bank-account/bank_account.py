import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.status = False
        self.lock = threading.Lock()

    def get_balance(self):
        if not self.status:
            raise ValueError('account not open')
        return self.balance

    def open(self):
        if self.status:
            raise ValueError('account already open')
        self.status = True
        self.balance = 0

    def deposit(self, amount):
        if not self.status:
            raise ValueError('account not open')
        if amount < 0:
            raise ValueError('amount must be greater than 0')
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        if not self.status:
            raise ValueError('account not open')
        if amount < 0:
            raise ValueError('amount must be greater than 0')
        if amount > self.balance:
            raise ValueError('amount must be less than balance')
        with self.lock:
            self.balance -= amount

    def close(self):
        if not self.status:
            raise ValueError('account not open')
        self.status = False

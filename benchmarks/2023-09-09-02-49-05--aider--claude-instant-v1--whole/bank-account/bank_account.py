import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.is_open = False

    def get_balance(self):
        self.lock.acquire()
        balance = self.balance
        self.lock.release()
        return balance

    def open(self):
        if self.is_open:
            raise ValueError('account already open')
        self.is_open = True

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        self.lock.acquire()
        self.balance += amount
        self.lock.release()

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError('account not open')
        if amount <= 0:
            raise ValueError('amount must be greater than 0')
        self.lock.acquire()
        if amount > self.balance:
            raise ValueError('amount must be less than balance')
        self.balance -= amount
        self.lock.release()

    def close(self):
        if not self.is_open:
            raise ValueError('account not open')
        self.is_open = False

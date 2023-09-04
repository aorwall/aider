import threading

class BankAccount:
    def __init__(self):
        self._lock = threading.Lock()
        self._is_open = False
        self._balance = 0

    def get_balance(self):
        with self._lock:
            if not self._is_open:
                raise ValueError('account not open')
            return self._balance

    def open(self):
        with self._lock:
            if self._is_open:
                raise ValueError('account already open')
            self._is_open = True

    def deposit(self, amount):
        with self._lock:
            if not self._is_open:
                raise ValueError('account not open')
            if amount <= 0:
                raise ValueError('amount must be greater than 0')
            self._balance += amount

    def withdraw(self, amount):
        with self._lock:
            if not self._is_open:
                raise ValueError('account not open')
            if amount <= 0:
                raise ValueError('amount must be greater than 0')
            if amount > self._balance:
                raise ValueError('amount must be less than balance')
            self._balance -= amount

    def close(self):
        with self._lock:
            self._is_open = False
            self._balance = 0

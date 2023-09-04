import threading

class BankAccount:
    def __init__(self):
        self._lock = threading.Lock()
        self._opened = False
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def open(self):
        with self._lock:
            if self._opened:
                raise ValueError('account already open')
            else:
                self._opened = True

    def deposit(self, amount):
        with self._lock:
            if not self._opened:
                raise ValueError('account not open')
            elif amount <= 0:
                raise ValueError('amount must be greater than 0')
            else:
                self._balance += amount

    def withdraw(self, amount):
        with self._lock:
            if not self._opened:
                raise ValueError('account not open')
            elif amount > self._balance:
                raise ValueError('amount must be less than balance')
            elif amount <= 0:
                raise ValueError('amount must be greater than 0')
            else:
                self._balance -= amount

    def close(self):
        with self._lock:
            if not self._opened:
                raise ValueError('account not open')
            else:
                self._opened = False

class BankAccount:
    def __init__(self):
        self._is_open = False
        self._balance = 0

    def get_balance(self):
        return self._balance

    def open(self):
        if self._is_open:
            raise ValueError("account already open")
        else:
            self._is_open = True

    def deposit(self, amount):
        if not self._is_open:
            raise ValueError("account not open")
        elif amount <= 0:
            raise ValueError("amount must be greater than 0")
        else:
            self._balance += amount

    def withdraw(self, amount):
        if not self._is_open:
            raise ValueError("account not open")
        elif amount > self._balance:
            raise ValueError("amount must be less than balance")
        elif amount < 0:
            raise ValueError("amount must be greater than 0")
        else:
            self._balance -= amount

    def close(self):
        self._is_open = False

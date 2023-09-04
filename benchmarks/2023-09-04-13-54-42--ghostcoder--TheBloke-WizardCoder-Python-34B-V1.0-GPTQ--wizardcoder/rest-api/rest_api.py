import json
from typing import Dict, Any

class User:
    def __init__(self, name: str):
        self.name = name
        self.owes = {}
        self.owed_by = {}
        self.balance = 0

    @property
    def total_owed(self) -> float:
        return sum(self.owes.values())

    @property
    def total_owed_to(self) -> float:
        return sum(self.owed_by.values())

    def update_balance(self):
        self.balance = self.total_owed_to - self.total_owed

    def add_debt(self, debtor: str, amount: float):
        if debtor not in self.owed_by:
            self.owed_by[debtor] = 0
        self.owed_by[debtor] += amount
        self.update_balance()

    def add_credit(self, creditor: str, amount: float):
        if creditor not in self.owes:
            self.owes[creditor] = 0
        self.owes[creditor] += amount
        self.update_balance()

class Database:
    def __init__(self):
        self._users = {}

    def create_user(self, name: str) -> User:
        if name in self._users:
            raise ValueError(f"User '{name}' already exists.")
        user = User(name)
        self._users[name] = user
        return user

    def list_users(self, names: list[str]) -> dict[str, User]:
        sorted_names = sorted(names)
        return {name: self._users[name] for name in sorted_names}

    def add_iou(self, lender: str, borrower: str, amount: float):
        if lender not in self._users:
            self.create_user(lender)
        if borrower not in self._users:
            self.create_user(borrower)

        self._users[lender].add_credit(borrower, amount)
        self._users[borrower].add_debt(lender, amount)

class RestAPI:
    def __init__(self, database: Database = None):
        self._database = database or Database()

    def _serialize_user(self, user: User) -> Dict[str, Any]:
        return {
            'name': user.name,
            'owes': user.owes,
            'owed_by': user.owed_by,
            'balance': round(user.balance, 2),
        }

    def get(self, url: str, payload: dict[str, Any] = None) -> dict[str, Any]:
        if url == '/users':
            users = self._database.list_users(payload['users'])
            return {'users': [self._serialize_user(u) for u in users.values()]}
        else:
            raise NotImplementedError('Invalid endpoint')

    def post(self, url: str, payload: dict[str, Any] = None) -> dict[str, Any]:
        if url == '/add':
            user = self._database.create_user(payload['user'])
            return {'users': [self._serialize_user(user)]}
        elif url == '/iou':
            self._database.add_iou(payload['lender'], payload['borrower'], payload['amount'])
            updated_users = self._database.list_users([payload['lender'], payload['borrower']])
            return {'users': [self._serialize_user(u) for u in updated_users.values()]}
        else:
            raise NotImplementedError('Invalid endpoint')

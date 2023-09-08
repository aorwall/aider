import json

class User:
    def __init__(self, name):
        self.name = name
        self.owes = {}
        self.owed_by = {}
        self.balance = 0

    def __str__(self):
        return json.dumps({
            "name": self.name,
            "owes": self.owes,
            "owed_by": self.owed_by,
            "balance": self.balance
        })

    def update_balance(self):
        self.balance = sum(self.owes.values()) - sum(self.owed_by.values())

class RestAPI:
    def __init__(self, database=None):
        self.users = {}
        if database:
            for user_data in database:
                user = User(user_data["name"])
                user.owes = user_data.get("owes", {})
                user.owed_by = user_data.get("owed_by", {})
                user.update_balance()
                self.users[user.name] = user

    def get(self, url, payload=None):
        if url == "/users" and payload:
            users = payload.get("users")
            if users:
                return [str(self.users[user]) for user in sorted(users) if user in self.users]
        return None

    def post(self, url, payload=None):
        if url == "/add" and payload:
            user_name = payload.get("user")
            if user_name and user_name not in self.users:
                user = User(user_name)
                self.users[user_name] = user
                return str(user)
        elif url == "/iou" and payload:
            lender_name = payload.get("lender")
            borrower_name = payload.get("borrower")
            amount = payload.get("amount")
            if lender_name and borrower_name and amount and lender_name in self.users and borrower_name in self.users:
                lender = self.users[lender_name]
                borrower = self.users[borrower_name]
                lender.owed_by.setdefault(borrower_name, 0)
                lender.owed_by[borrower_name] += amount
                borrower.owes.setdefault(lender_name, 0)
                borrower.owes[lender_name] += amount
                lender.update_balance()
                borrower.update_balance()
                return [str(lender), str(borrower)]
        return None

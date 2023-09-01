import json

class Database:
    def __init__(self):
        self.users = {}
        self.ious = {}

    def get_all_users(self):
        return list(self.users.keys())

    def get_users(self, users):
        return [self.users[user] for user in users]

    def add_user(self, user):
        self.users[user] = {"name": user, "owes": {}, "owed_by": {}}

    def add_users(self, users):
        for user in users:
            self.add_user(user)

    def add_iou(self, lender, borrower, amount):
        if lender not in self.users:
            self.add_user(lender)
        if borrower not in self.users:
            self.add_user(borrower)
        self.users[lender]["owes"][borrower] = amount
        self.users[borrower]["owed_by"][lender] = amount
        self.ious[(lender, borrower)] = amount

    def get_ious(self, lender, borrower):
        return self.ious.get((lender, borrower), 0)
class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == "/users":
            if payload is None:
                return json.dumps({"users": self.database.get_all_users()})
            else:
                users = payload.get("users")
                return json.dumps({"users": self.database.get_users(users)})
        elif url == "/add":
            user = payload.get("user")
            self.database.add_user(user)
            return json.dumps({"user": user})
        elif url == "/iou":
            lender = payload.get("lender")
            borrower = payload.get("borrower")
            amount = payload.get("amount")
            self.database.add_iou(lender, borrower, amount)
            return json.dumps({"users": self.database.get_users([lender, borrower])})
        else:
            return json.dumps({"error": "Invalid URL"})

    def post(self, url, payload=None):
        if url == "/users":
            users = payload.get("users")
            self.database.add_users(users)
            return json.dumps({"users": self.database.get_users(users)})
        elif url == "/add":
            user = payload.get("user")
            self.database.add_user(user)
            return json.dumps({"user": user})
        elif url == "/iou":
            lender = payload.get("lender")
            borrower = payload.get("borrower")
            amount = payload.get("amount")
            self.database.add_iou(lender, borrower, amount)
            return json.dumps({"users": self.database.get_users([lender, borrower])})
        else:
            return json.dumps({"error": "Invalid URL"})

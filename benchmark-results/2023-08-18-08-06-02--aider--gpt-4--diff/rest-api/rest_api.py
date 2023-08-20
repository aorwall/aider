import json

class RestAPI:
    def __init__(self, database=None):
        self.users = database or {}

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                names = json.loads(payload)["users"]
                for name in names:
                    if name not in self.users:
                        return json.dumps({"error": "User not found"})
                return json.dumps({"users": [self.users[name] for name in names]})
            else:
                return json.dumps({"users": list(self.users.values())})

    def post(self, url, payload=None):
        data = json.loads(payload)
        if url == "/add":
            return self.add_user(data["user"])
        elif url == "/iou":
            return self.create_iou(data["lender"], data["borrower"], data["amount"])

    def add_user(self, name):
        self.users[name] = {"name": name, "owes": {}, "owed_by": {}, "balance": 0.0}
        return json.dumps(self.users[name])

    def create_iou(self, lender, borrower, amount):
        if lender not in self.users or borrower not in self.users:
            return json.dumps({"error": "User not found"})
        self.users[lender]["owed_by"][borrower] = self.users[lender]["owed_by"].get(borrower, 0) + amount
        self.users[borrower]["owes"][lender] = self.users[borrower]["owes"].get(lender, 0) + amount
        self.users[lender]["balance"] += amount
        self.users[borrower]["balance"] -= amount
        return json.dumps({"users": sorted([self.users[lender], self.users[borrower]], key=lambda x: x["name"])})

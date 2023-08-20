import json

class RestAPI:
    def __init__(self, database=None):
        self.database = database if database else {"users": []}

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                names = json.loads(payload)["users"]
                return json.dumps({"users": [user for user in self.database["users"] if user["name"] in names]})
            else:
                return json.dumps(self.database)

    def post(self, url, payload=None):
        if url == "/add":
            name = json.loads(payload)["user"]
            user = {"name": name, "owes": {}, "owed_by": {}, "balance": 0.0}
            self.database["users"].append(user)
            return json.dumps(user)
        elif url == "/iou":
            data = json.loads(payload)
            lender = next(user for user in self.database["users"] if user["name"] == data["lender"])
            borrower = next(user for user in self.database["users"] if user["name"] == data["borrower"])
            amount = data["amount"]

            if borrower["name"] in lender["owes"]:
                lender["owes"][borrower["name"]] -= amount
                if lender["owes"][borrower["name"]] <= 0:
                    amount = -lender["owes"][borrower["name"]]
                    del lender["owes"][borrower["name"]]
                else:
                    amount = 0
            if amount > 0:
                lender["owed_by"][borrower["name"]] = lender["owed_by"].get(borrower["name"], 0) + amount
                borrower["owes"][lender["name"]] = borrower["owes"].get(lender["name"], 0) + amount

            lender["balance"] = sum(lender["owed_by"].values()) - sum(lender["owes"].values())
            borrower["balance"] = sum(borrower["owed_by"].values()) - sum(borrower["owes"].values())

            return json.dumps({"users": sorted([lender, borrower], key=lambda x: x["name"])})
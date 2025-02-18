import json
from collections import defaultdict

class RestAPI:
    def __init__(self, database=None):
        self.database = {} if database is None else database

    def get(self, url, payload=None):
        if url == "/users":
            users = sorted([{**user} for user in self.database.values()])
            return {"users": users}, 200
        elif url == "/add" and "user" in payload:
            name = payload["user"]
            if name in self.database:
                return None, 409
            else:
                self.database[name] = {
                    "name": name,
                    "owes": {},
                    "owed_by": {},
                    "balance": 0
                }
                return {**self.database[name]}
        else:
            return None, 404

    def post(self, url, payload=None):
        try:
            payload = json.loads(payload)
        except (json.JSONDecodeError, TypeError):
            return None, 400

        if url == "/iou" and all(key in payload for key in ["lender", "borrower", "amount"]):
            lender = payload["lender"]
            borrower = payload["borrower"]
            amount = float(payload["amount"])

            if lender not in self.database or borrower not in self.database:
                return None, 404

            # Update lender and borrower's records
            self.database[lender]["owes"][borrower] = self.database[lender].get("owes", {}).get(borrower, 0) + amount
            self.database[borrower]["owed_by"][lender] = self.database[borrower].get("owed_by", {}).get(lender, 0) + amount

            # Recalculate balance
            self.database[lender]["balance"] -= amount
            self.database[borrower]["balance"] += amount

            users = sorted([{**user} for user in [self.database[lender], self.database[borrower]]])
            return {"users": users}, 201
        else:
            return None, 400
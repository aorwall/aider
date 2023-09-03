class RestAPI:
    def __init__(self, database=None):
        self.database = database
        if not self.database:
            self.database = {}

    def get(self, url, payload=None):
        if url == "/users":
            users = payload.get("users")
            if users:
                return {user: self.database.get(user, {}) for user in users}
            return self.database

        return None

    def post(self, url, payload=None):
        if url == "/add":
            user = payload.get("user")
            if user and user not in self.database:
                self.database[user] = {}
                return self.database[user]
            return None

        if url == "/iou":
            lender = payload.get("lender")
            borrower = payload.get("borrower")
            amount = payload.get("amount")
            if lender and borrower and amount:
                lender_info = self.database.get(lender, {})
                borrower_info = self.database.get(borrower, {})
                lender_info["owes"] = lender_info.get("owes", {})
                lender_info["owes"][borrower] = lender_info["owes"].get(borrower, 0) + amount
                borrower_info["owed_by"] = borrower_info.get("owed_by", {})
                borrower_info["owed_by"][lender] = borrower_info["owed_by"].get(lender, 0) + amount
                self.database[lender] = lender_info
                self.database[borrower] = borrower_info
                return {"users": [lender_info, borrower_info]}
            return None

        return None

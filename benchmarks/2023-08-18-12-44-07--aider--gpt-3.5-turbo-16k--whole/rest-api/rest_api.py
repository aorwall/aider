class RestAPI:
    def __init__(self, database=None):
        self.users = {}

    def get_users(self, payload=None):
        if payload and 'users' in payload:
            requested_users = payload['users']
            user_objects = [self.users[user] for user in requested_users if user in self.users]
            user_objects.sort(key=lambda x: x['name'])
            return {"users": user_objects}
        else:
            return {"users": list(self.users.values())}

    def add_user(self, payload):
        name = payload['user']
        if name not in self.users:
            user = {
                "name": name,
                "owes": {},
                "owed_by": {},
                "balance": 0.0
            }
            self.users[name] = user
            return user
        else:
            return None

    def create_iou(self, payload):
        lender = payload['lender']
        borrower = payload['borrower']
        amount = payload['amount']

        if lender in self.users and borrower in self.users:
            lender_user = self.users[lender]
            borrower_user = self.users[borrower]

            if lender == borrower:
                return {"users": [lender_user]}

            if amount > 0:
                lender_user['owed_by'][borrower] = lender_user['owed_by'].get(borrower, 0) + amount
                borrower_user['owes'][lender] = borrower_user['owes'].get(lender, 0) + amount
            elif amount < 0:
                lender_user['owes'][borrower] = lender_user['owes'].get(borrower, 0) - amount
                borrower_user['owed_by'][lender] = borrower_user['owed_by'].get(lender, 0) - amount

            lender_user['balance'] = self.calculate_balance(lender_user)
            borrower_user['balance'] = self.calculate_balance(borrower_user)

            return {"users": [lender_user, borrower_user]}
        else:
            return None

    def calculate_balance(self, user):
        total_owed_by = sum(user['owed_by'].values())
        total_owed_to = sum(user['owes'].values())
        return total_owed_by - total_owed_to

    def post(self, url, payload):
        if url == "/add":
            return self.add_user(payload)
        elif url == "/iou":
            return self.create_iou(payload)

    def get(self, url, payload):
        if url == "/users":
            return self.get_users(payload)

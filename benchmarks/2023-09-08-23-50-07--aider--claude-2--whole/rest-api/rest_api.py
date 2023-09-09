
users = {}

class User:

    def __init__(self, name):
        self.name = name
        self.owes = {}
        self.owed_by = {}

    @property
    def balance(self):
        return sum(self.owed_by.values()) - sum(self.owes.values())


class RestAPI:

    def __init__(self):
        pass

    def get_users(self, user_names=None):
        if user_names is None:
            return sorted(users.values(), key=lambda user: user.name)
        else:
            return [users[name] for name in user_names if name in users]

    def add_user(self, name):
        if name in users:
            return f"User {name} already exists"
        user = User(name)
        users[name] = user
        return user

    def create_iou(self, lender, borrower, amount):
        if lender not in users:
            return f"User {lender} does not exist"
        if borrower not in users:
            return f"User {borrower} does not exist"

        lender_user = users[lender]
        borrower_user = users[borrower]
        lender_user.owes[borrower] = lender_user.owes.get(borrower, 0) + amount
        borrower_user.owed_by[lender] = borrower_user.owed_by.get(lender, 0) + amount

        return self.get_users([lender, borrower])


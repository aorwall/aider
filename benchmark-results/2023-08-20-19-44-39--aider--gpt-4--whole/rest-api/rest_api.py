import json

class RestAPI:
    def __init__(self, database=None):
        self.database = database if database else {'users': []}

    def get(self, url, payload=None):
        if url == '/users':
            if payload:
                names = eval(payload)['users']
                return json.dumps({'users': [user for user in self.database['users'] if user['name'] in names]})
            else:
                return json.dumps(self.database)

    def post(self, url, payload=None):
        if url == '/add':
            name = eval(payload)['user']
            user = {
                'name': name,
                'owes': {},
                'owed_by': {},
                'balance': 0.0
            }
            self.database['users'].append(user)
            return json.dumps(user)

        if url == '/iou':
            data = eval(payload)
            lender = self.get_user(data['lender'])
            borrower = self.get_user(data['borrower'])
            amount = data['amount']

            if borrower['name'] in lender['owed_by']:
                lender['owed_by'][borrower['name']] += amount
            else:
                lender['owed_by'][borrower['name']] = amount

            if lender['name'] in borrower['owes']:
                borrower['owes'][lender['name']] += amount
            else:
                borrower['owes'][lender['name']] = amount

            lender['balance'] += amount
            borrower['balance'] -= amount

            return json.dumps({'users': sorted([lender, borrower], key=lambda x: x['name'])})

    def get_user(self, name):
        for user in self.database['users']:
            if user['name'] == name:
                return user
        return None

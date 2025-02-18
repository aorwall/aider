import json
from operator import itemgetter

class RestAPI:
    def __init__(self, database=None):
        self.database = {} if not database else database

    def _update_user(self, action, data):
        # Check if 'user' is present in data dictionary
        if 'user' not in data:
            raise KeyError('User not found')

        user = data['user']
        if 'amount' in data:
            amount = float(data['amount'])
        else:
            amount = None

        if user not in self.database:
            self.database[user] = {'owes': {}, 'owed_by': {}}

        if action == 'create_user':
            return

        if 'target_user' in data:
            target_user = data['target_user']

            if action == 'add':
                if target_user not in self.database:
                    self.database[target_user] = {'owes': {}, 'owed_by': {}}

                self.database[target_user]['owes'][user] = amount
                self.database[user]['owed_by'][target_user] = amount
            elif action == 'iou':
                if target_user in self.database[user]['owed_by']:
                    del self.database[user]['owed_by'][target_user]
                if user in self.database[target_user]['owes']:
                    del self.database[target_user]['owes'][user]

    def get(self, url, payload=None):
        parts = url.split('/')
        action = parts[1]
        data = json.loads(payload) if payload else {}

        if len(parts) > 2:
            data['user'] = parts[2]

        if len(parts) > 3:
            data['target_user'] = parts[3]

        if len(parts) > 4:
            data['amount'] = parts[4]

        response = []
        if action == 'users':
            sorted_keys = sorted(self.database.keys(), key=itemgetter())
            if 'users' in data:
                filtered_keys = [key for key in sorted_keys if key in data['users']]
                for key in filtered_keys:
                    response.append({"name": key, **self.database[key]})
            else:
                for key in sorted_keys:
                    response.append({"name": key, **self.database[key]})
        else:
            try:
                self._update_user(action, data)
            except KeyError as e:
                print("Exception: ", str(e))

            response = list(filter(lambda u: u['name'] != data['user'], map(lambda k: {"name": k, **self.database[k]}, self.database)))

        return json.dumps({"users": response})

    def post(self, url, payload=None):
        parts = url.split('/')
        action = parts[1]
        data = json.loads(payload) if payload else {}

        if len(parts) > 2:
            data['user'] = parts[2]

        if len(parts) > 3:
            data['target_user'] = parts[3]

        if len(parts) > 4:
            data['amount'] = parts[4]

        try:
            self._update_user(action, data)
        except KeyError as e:
            print("Exception: ", str(e))

        response = list(filter(lambda u: u['name'] != data['user'], map(lambda k: {"name": k, **self.database[k]}, self.database)))
        return json.dumps({"users": response})

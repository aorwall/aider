import json

users = {}

class RestAPI:

  def __init__(self, database=None):
    if database:
      self.users = database
    else:  
      self.users = users

  def get(self, url, payload=None):
    if url == '/users':
      if payload and isinstance(payload, dict) and 'users' in payload:
        return {'users': [self.users[user] for user in payload['users']]}  
      else:
        return {'users': list(self.users.values())}

  def post(self, url, payload=None):
    if url == '/add' and isinstance(payload, dict) and 'user' in payload:
      user = payload['user']
      self.users[user] = {'name': user, 'owes': {}, 'owed_by': {}, 'balance': 0}
      return self.users[user]

    elif url == '/iou' and isinstance(payload, dict) and 'lender' in payload and 'borrower' in payload and 'amount' in payload:
      lender = payload['lender']
      borrower = payload['borrower'] 
      amount = payload['amount']

      self.users[lender]['owed_by'][borrower] = amount
      self.users[borrower]['owes'][lender] = amount

      for user in (lender, borrower):
        balance = sum(self.users[user]['owed_by'].values()) - sum(self.users[user]['owes'].values())
        self.users[user]['balance'] = balance

      return {'users': [self.users[lender], self.users[borrower]]}

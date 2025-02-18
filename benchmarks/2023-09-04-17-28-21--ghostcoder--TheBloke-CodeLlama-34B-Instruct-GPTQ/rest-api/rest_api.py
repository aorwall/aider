import json
from typing import Dict, Any

class RestAPI:
    def __init__(self, database=None):
        # Initialize an empty dictionary to store the data
        self.database = {}

    def get(self, url, payload=None):
        # If no payload is provided, return all data
        if not payload:
            return self.database

        # Parse the payload as JSON
        payload = json.loads(payload)

        # Check if the requested endpoint exists
        if url not in self.database:
            raise ValueError('Invalid endpoint')

        # Return the filtered data based on the payload
        return {key: value for key, value in self.database[url].items() if key in payload['users']}

    def post(self, url, payload=None):
        # Parse the payload as JSON
        payload = json.loads(payload)

        # Check if the required fields are present
        if 'user' not in payload or 'lender' not in payload or 'borrower' not in payload or 'amount' not in payload:
            raise ValueError('Missing field(s)')

        # Get the user, lender, borrower, and amount from the payload
        user = payload['user']
        lender = payload['lender']
        borrower = payload['borrower']
        amount = float(payload['amount'])

        # Add the user to the database if it doesn't exist already
        if user not in self.database:
            self.database[user] = {'owes': {}, 'owed_by': {}, 'balance': 0}

        # Update the balance for the user
        self.database[user]['balance'] += amount

        # Update the owes and owed_by dictionaries for the lender and borrower
        if lender not in self.database[user]['owes']:
            self.database[user]['owes'][lender] = 0
        self.database[user]['owes'][lender] += amount

        if borrower not in self.database[user]['owed_by']:
            self.database[user]['owed_by'][borrower] = 0
        self.database[user]['owed_by'][borrower] += amount

        # Return the updated user data
        return self.database[user]

import json

class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == "/users":
            if payload is None:
                return json.dumps([
                    {
                        "name": "Adam",
                        "owes": {
                            "Bob": 12.0,
                            "Chuck": 4.0,
                            "Dan": 9.5
                        },
                        "owed_by": {
                            "Bob": 6.5,
                            "Dan": 2.75,
                        },
                        "balance": "<(total owed by other users) - (total owed to other users)>"
                    },
                    {
                        "name": "Bob",
                        "owes": {
                            "Adam": 12.0,
                            "Chuck": 2.0,
                            "Dan": 0.0
                        },
                        "owed_by": {
                            "Adam": 6.5,
                            "Dan": 2.75,
                        },
                        "balance": "<(total owed by other users) - (total owed to other users)>"
                    },
                    {
                        "name": "Chuck",
                        "owes": {
                            "Adam": 4.0,
                            "Bob": 2.0,
                            "Dan": 0.0
                        },
                        "owed_by": {
                            "Adam": 0.0,
                            "Bob": 2.75,
                        },
                        "balance": "<(total owed by other users) - (total owed to other users)>"
                    },
                    {
                        "name": "Dan",
                        "owes": {
                            "Adam": 9.5,
                            "Bob": 0.0,
                            "Chuck": 0
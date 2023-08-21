import unittest
from rest_api import RestAPI

class RestApiTest(unittest.TestCase):
    def setUp(self):
        self.api = RestAPI()

    def test_get_single_user(self):
        self.api.post("/add", {"user": "Adam"})
        response = self.api.get("/users", {"users": ["Adam"]})
        self.assertEqual(response, {"users": [{"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0}]})

    def test_get_multiple_users(self):
        self.api.post("/add", {"user": "Adam"})
        self.api.post("/add", {"user": "Bob"})
        response = self.api.get("/users", {"users": ["Adam", "Bob"]})
        self.assertEqual(response, {"users": [
            {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
            {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0}
        ]})

    def test_add_user(self):
        response = self.api.post("/add", {"user": "Adam"})
        self.assertEqual(response, {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0})

    def test_create_iou(self):
        self.api.post("/add", {"user": "Adam"})
        self.api.post("/add", {"user": "Bob"})
        response = self.api.post("/iou", {"lender": "Adam", "borrower": "Bob", "amount": 5.25})
        self.assertEqual(response, {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {"Bob": 5.25}, "balance": 5.25},
                {"name": "Bob", "owes": {"Adam": 5.25}, "owed_by": {}, "balance": -5.25}
            ]
        })

    def test_create_iou_with_nonexistent_users(self):
        response = self.api.post("/iou", {"lender": "Adam", "borrower": "Bob", "amount": 5.25})
        self.assertIsNone(response)

    def test_create_iou_with_negative_amount(self):
        self.api.post("/add", {"user": "Adam"})
        self.api.post("/add", {"user": "Bob"})
        response = self.api.post("/iou", {"lender": "Adam", "borrower": "Bob", "amount": -5.25})
        self.assertIsNone(response)

    def test_both_users_have_0_balance(self):
        self.api.post("/add", {"user": "Adam"})
        self.api.post("/add", {"user": "Bob"})
        response = self.api.post("/iou", {"lender": "Adam", "borrower": "Bob", "amount": 5.25})
        self.assertEqual(response, {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {"Bob": 5.25}, "balance": 5.25},
                {"name": "Bob", "owes": {"Adam": 5.25}, "owed_by": {}, "balance": -5.25}
            ]
        })
        response = self.api.post("/iou", {"lender": "Bob", "borrower": "Adam", "amount": 5.25})
        self.assertEqual(response, {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {"Bob": 5.25}, "balance": 0.0},
                {"name": "Bob", "owes": {"Adam": 5.25}, "owed_by": {}, "balance": 0.0}
            ]
        })

    def test_borrower_has_negative_balance(self):
        self.api.post("/add", {"user": "Adam"})
        self.api.post("/add", {"user": "Bob"})
        response = self.api.post("/iou", {"lender": "Adam", "borrower": "Bob", "amount": 10.0})
        self.assertEqual(response, {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {"Bob": 10.0}, "balance": 10.0},
                {"name": "Bob", "owes": {"Adam": 10.0}, "owed_by": {}, "balance": -10.0}
            ]
        })
        response = self.api.post("/iou", {"lender": "Bob", "borrower": "Adam", "amount": 15.0})
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
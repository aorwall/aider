import unittest
from rest_api import RestAPI

class TestRestAPI(unittest.TestCase):
    def setUp(self):
        self.rest_api = RestAPI()

    def test_get_users(self):
        users = self.rest_api.get("/users")
        self.assertEqual(users, {})

        users = self.rest_api.get("/users", {"users": ["Adam", "Bob"]})
        self.assertEqual(users, {})

    def test_post_add(self):
        user = self.rest_api.post("/add", {"user": "Adam"})
        self.assertEqual(user, {})

        user = self.rest_api.post("/add", {"user": "Adam"})
        self.assertEqual(user, {})

    def test_post_iou(self):
        iou = self.rest_api.post("/iou", {"lender": "Adam", "borrower": "Bob", "amount": 5.25})
        self.assertEqual(iou, {})

        iou = self.rest_api.post("/iou", {"lender": "Adam", "borrower": "Bob", "amount": 5.25})
        self.assertEqual(iou, {})

if __name__ == "__main__":
    unittest.main()
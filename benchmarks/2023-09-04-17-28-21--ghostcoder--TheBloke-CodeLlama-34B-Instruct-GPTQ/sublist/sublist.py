import unittest
from sublist import *

class SublistTest(unittest.TestCase):
    """
    This class contains unit tests for the sublist function defined in sublist.py
    """
    def setUp(self):
        """
        Initialization performed before each individual test.
        """
        global SUBLIST, SUPERLIST, EQUAL, UNEQUAL

        SUBLIST = 0
        SUPERLIST = 1
        EQUAL = 2
        UNEQUAL = 3

    def tearDown(self):
        """
        Cleanup performed after each individual test.
        """
        pass

    def test_equal_return_value(self):
        """
        Test case for when two lists are equal.
        """
        result = sublist([1, 2, 3], [1, 2, 3])
        self.assertEqual(result, EQUAL)

    def test_unequal_return_value(self):
        """
        Test case for when two lists are not equal.
        """
        result = sublist([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, UNEQUAL)

    def test_sublist_return_value(self):
        """
        Test case for when one list is a sublist of another.
        """
        result = sublist([1, 2, 3], [1, 2, 3, 4, 5])
        self.assertEqual(result, SUBLIST)

    def test_superlist_return_value(self):
        """
        Test case for when one list is a superlist of another.
        """
        result = sublist([1, 2, 3, 4, 5], [1, 2, 3])
        self.assertEqual(result, SUPERLIST)

if __name__ == '__main__':
    unittest.main()
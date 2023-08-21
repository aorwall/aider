import unittest

from pascals_triangle import rows


class PascalsTriangleTest(unittest.TestCase):
    def test_zero_rows(self):
        self.assertEqual(rows(0), [])

    def test_single_row(self):
        self.assertEqual(rows(1), [[1]])

    def test_two_rows(self):
        self.assertEqual(rows(2), [[1], [1, 1]])

    def test_three_rows(self):
        self.assertEqual(rows(3), [[1], [1, 1], [1, 2, 1]])

    def test_four_rows(self):
        self.assertEqual(rows(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    def test_negative_rows(self):
        with self.assertRaises(ValueError) as err:
            rows(-1)
        self.assertEqual(str(err.exception), "number of rows is negative")


if __name__ == '__main__':
    unittest.main()
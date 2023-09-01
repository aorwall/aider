import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):
    def test_row(self):
        matrix = Matrix("9 8 7\n5 3 2\n6 6 7")
        self.assertEqual(matrix.row(0), [9, 8, 7])
        self.assertEqual(matrix.row(1), [5, 3, 2])
        self.assertEqual(matrix.row(2), [6, 6, 7])

    def test_column(self):
        matrix = Matrix("9 8 7\n5 3 2\n6 6 7")
        self.assertEqual(matrix.column(0), [9, 5, 6])
        self.assertEqual(matrix.column(1), [8, 3, 6])
        self.assertEqual(matrix.column(2), [7, 2, 7])

if __name__ == '__main__':
    unittest.main()
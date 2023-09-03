class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row:
            return True
        if self.column == another_queen.column:
            return True
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False

    def __repr__(self):
        return f"Queen at ({self.row}, {self.column})"

class QueenAttackTest(unittest.TestCase):
    def test_queen_must_have_positive_row(self):
        with self.assertRaises(ValueError) as err:
            Queen(-1, 2)
        self.assertEqual(str(err.exception), "row must be positive")

    def test_queen_must_have_row_on_board(self):
        with self.assertRaises(ValueError) as err:
            Queen(8, 2)
        self.assertEqual(str(err.exception), "row must be on the board")

    def test_queen_must_have_positive_column(self):
        with self.assertRaises(ValueError) as err:
            Queen(2, -1)
        self.assertEqual(str(err.exception), "column must be positive")

    def test_queen_must_have_column_on_board(self):
        with self.assertRaises(ValueError) as err:
            Queen(2, 8)
        self.assertEqual(str(err.exception), "column must be on the board")

    def test_queens_same_position_can_attack(self):
        queen1 = Queen(2, 3)
        queen2 = Queen(2, 3)
        self.assertTrue(queen1.can_attack(queen2))

    def test_queens_different_positions_cannot_attack(self):
        queen1 = Queen(2, 3)
        queen2 = Queen(4, 7)
        self.assertFalse(queen1.can_attack(queen2))

if __name__ == "__main__":
    unittest.main()

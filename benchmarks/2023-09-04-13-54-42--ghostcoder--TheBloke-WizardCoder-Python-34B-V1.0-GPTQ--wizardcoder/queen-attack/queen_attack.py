class Queen:
    def __init__(self, row, column):
        if row <= 0 or row > 7:
            raise ValueError("Row not on board")

        if column <= 0 or column > 7:
            raise ValueError("Column not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        # Check diagonals
        delta_x = abs(self.row - another_queen.row)
        delta_y = abs(self.column - another_queen.column)

        if delta_x == delta_y:
            return True

        return False

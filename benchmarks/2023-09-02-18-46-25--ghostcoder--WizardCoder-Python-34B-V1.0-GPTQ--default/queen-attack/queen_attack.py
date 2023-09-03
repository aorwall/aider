class Queen:
    def __init__(self, row, column):
        if row < 0 or column < 0:
            raise ValueError("Row and Column must be non-negative integers.")
        elif row > 7 or column > 7:
            raise ValueError("Row and Column must be within range of a chessboard (8x8).")

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        return (self.row == another_queen.row) or (self.column == another_queen.column) or \
               abs(self.row - another_queen.row) == abs(self.column - another_queen.column)

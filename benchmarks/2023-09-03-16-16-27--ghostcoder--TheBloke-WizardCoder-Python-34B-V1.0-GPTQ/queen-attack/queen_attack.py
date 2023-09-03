class Queen:
    def __init__(self, row, column):
        self.row = row
        self.col = column

        # Check if row and col are non-negative integers
        if not (isinstance(row, int) and isinstance(column, int)):
            raise ValueError("Row and Column must be integers.")
        elif row < 1 or column < 1:
            raise ValueError("Row and Column must be greater than zero.")
        elif not (1 <= row <= 8 and 1 <= column <= 8):
            raise ValueError("Row and Column must be between 1 and 8 inclusive.")


    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.col == another_queen.col:
            raise ValueError("Invalid queen position: both queens in the same square")
        return (self.row == another_queen.row or self.col == another_queen.col or abs(self.row - another_queen.row) == abs(self.col - another_queen.col))

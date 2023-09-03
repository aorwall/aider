class Queen:
    def __init__(self, row, column):
        if row < 0 or column < 0:
            raise ValueError("Row and Column values must be positive.")
        elif row >= 8 or column >= 8:
            raise ValueError("Row and Column values must be less than 8.")

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        # If both the queens are at the same location
        if (self.row == another_queen.row) and (self.column == another_queen.column):
            raise ValueError("Invalid queen position: both queens in the same square")

        return self.row == another_queen.row or \
               self.column == another_queen.column or \
               abs(self.row - another_queen.row) == abs(self.column - another_queen.column)

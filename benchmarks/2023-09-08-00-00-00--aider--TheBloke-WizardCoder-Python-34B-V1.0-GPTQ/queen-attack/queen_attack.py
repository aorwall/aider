class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        return self.row == another_queen.row or self.column == another_queen.column or abs(self.row - another_queen.row) == abs(self.column - another_queen.column)

# Test cases
white_queen = Queen(2, 3)
black_queen = Queen(5, 6)

print(white_queen.can_attack(black_queen))  # Output: True

class Queen:
    def __init__(self, row, column):
        if row < 0 or column < 0:
            raise ValueError("row and column must be positive")
        if row > 7 or column > 7:
            raise ValueError("row and column must be on the board")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        return self.row == another_queen.row or self.column == another_queen.column

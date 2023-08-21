class Queen:
    def __init__(self, row, column):
        if not isinstance(row, int) or row < 0 or row > 7:
            raise ValueError("row not on board")
        if not isinstance(column, int) or column < 0 or column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False
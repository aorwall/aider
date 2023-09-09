class Queen:
    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive") 
        if column < 0:
            raise ValueError("column not positive")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row or self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False

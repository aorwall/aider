class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        return self.row == another_queen.row or \
               self.row - another_queen.row == self.column - another_queen.column or \
               self.row - another_queen.row == -(self.column - another_queen.column) or \
               self.column == another_queen.column or \
               self.column - another_queen.column == self.row - another_queen.row or \
               self.column - another_queen.column == -(self.row - another_queen.row)

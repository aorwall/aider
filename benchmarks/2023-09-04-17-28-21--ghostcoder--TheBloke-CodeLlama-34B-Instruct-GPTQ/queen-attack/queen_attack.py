class Queen:
    def __init__(self, row, column):
        """
        Initialize a Queen instance.
        
        Args:
            row (int): The row where the queen is placed.
            column (int): The column where the queen is placed.
            
        Raises:
            ValueError: If either row or column is negative or not on the board.
        """
        # Check if row and column are within bounds
        if row < 0 or column < 0 or row > 7 or column > 7:
            raise ValueError("Row and column must be between 0 and 7.")

        self._row = row
        self._column = column

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    def can_attack(self, another_queen):
        """
        Determine if this queen can attack another queen.
        
        Args:
            another_queen (Queen): Another queen to check for attacks.
            
        Returns:
            bool: True if this queen can attack another queen, False otherwise.
            
        Raises:
            ValueError: If both queens are on the same location.
        """
        # Check if both queens are on the same location
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        # Check if both queens are on the same diagonal
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True

        # Check if both queens are on the same row or column
        if self.row == another_queen.row or self.column == another_queen.column:
            return True

        return False

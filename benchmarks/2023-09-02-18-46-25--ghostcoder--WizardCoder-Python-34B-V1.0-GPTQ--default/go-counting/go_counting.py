
class Board:
    """Count territories of each player in a Go game
    
    Args:
        board (list[str]): A two-dimensional Go board
    """

    WHITE = 'W'
    BLACK = 'B'

    def __init__(self, board):
        self.board = board

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board
        
        Args:
            x (int): Column on the board
            y (int): Row on the board
        
        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        Raises:
            ValueError: If the specified coordinate is out of range
        """

        if not self._valid_coord(x, y):
            raise ValueError("Invalid coordinate")

        # Check if the current position belongs to either black or white
        if self.board[y][x] == self.WHITE:
            return (self.WHITE, self._territory(self.WHITE, x, y))
        elif self.board[y][x] == self.BLACK:
            return (self.BLACK, self._territory(self.BLACK, x, y))
        else:
            return ('', set())

    def _valid_coord(self, x, y):
        """Helper function to check whether the given coordinates are valid"""
        return 0 <= x < len(self.board) and 0 <= y < len(self.board[x])

    def _territory(self, player, x, y):
        """Helper function for finding the territory of a player"""
        pass

    def territories(self):
        """Find the owners and the territories of the whole board
        
        Args:
            none
        
        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B".  The value being a set
                        of coordinates owned by the owner.
        """
        pass

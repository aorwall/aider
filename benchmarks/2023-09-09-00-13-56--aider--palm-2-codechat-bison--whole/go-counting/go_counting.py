class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

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
        """
        if x < 0 or x >= len(self.board):
            raise ValueError('Invalid coordinate')
        if y < 0 or y >= len(self.board[0]):
            raise ValueError('Invalid coordinate')

        # Initialize the territory and owner.
        territory = set()
        owner = ''

        # Recursively search all empty intersections that are connected to
        # the given coordinate.
        self._territory_recursive(x, y, territory, owner)

        return owner, territory

    def _territory_recursive(self, x, y, territory, owner):
        """Recursively search all empty intersections that are connected to
           the given coordinate.

        Args:
            x (int): Column on the board
            y (int): Row on the board
            territory (set): A set of coordinates that are already in the territory.
            owner (str): The owner of the territory.
        """
        # If the coordinate is not empty or already in the territory,
        # then do nothing.
        if self.board[y][x] != ' ' or x in territory or y in territory:
            return

        # Add the coordinate to the territory.
        territory.add((x, y))

        # Check all neighboring coordinates.
        for dx in [-1, 0, 1]:
            for dy in [-1,
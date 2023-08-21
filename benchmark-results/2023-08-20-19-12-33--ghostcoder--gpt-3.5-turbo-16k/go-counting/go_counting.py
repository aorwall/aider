class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self.territories_dict = {}

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
        if not (0 <= x < len(self.board[0]) and 0 <= y < len(self.board)):
            raise ValueError('Invalid coordinate')

        if (x, y) in self.territories_dict:
            return self.territories_dict[(x, y)]

        owner = self.board[y][x]
        territories = set()
        visited = set()

        def dfs(x, y):
            if (x, y) in visited:
                return
            visited.add((x, y))

            if not (0 <= x < len(self.board[0]) and 0 <= y < len(self.board)):
                return

            if self.board[y][x] == owner:
                territories.add((x, y))
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

        dfs(x, y)
        self.territories_dict[(x, y)] = (owner, territories)
        return (owner, territories)

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        territories_dict = {}

        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if (x, y) not in self.territories_dict:
                    owner, territories = self.territory(x, y)
                    if owner in territories_dict:
                        territories_dict[owner] |= territories
                    else:
                        territories_dict[owner] = territories

        return territories_dict
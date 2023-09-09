
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
        if not (0 <= x < len(self.board[0])) or not (0 <= y < len(self.board)):
            raise ValueError('Invalid coordinate')
        
        owner = self.board[y][x]
        territories = set()
        
        if owner != ' ':
            territories.add((x, y))
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                xx, yy = x + dx, y + dy
                if 0 <= xx < len(self.board[0]) and 0 <= yy < len(self.board):
                    if self.board[yy][xx] == owner:
                        territories |= self.territory(xx, yy)[1]
        
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
        territories = {}
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                owner, terr = self.territory(x, y)
                territories[owner] = territories.get(owner, set()) | terr
        return territories


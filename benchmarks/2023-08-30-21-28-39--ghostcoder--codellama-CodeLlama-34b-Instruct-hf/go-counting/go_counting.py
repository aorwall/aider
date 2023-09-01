
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
        if x < 0 or x >= len(self.board[0]) or y < 0 or y >= len(self.board):
            raise ValueError("Invalid coordinate")

        owner = self.board[y][x]
        territories = set()

        if owner == "W":
            territories.add((x, y))
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if self.board[j][i] == "W":
                        territories.add((i, j))
        elif owner == "B":
            territories.add((x, y))
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if self.board[j][i] == "B":
                        territories.add((i, j))

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
                owner, territory = self.territory(x, y)
                if owner not in territories:
                    territories[owner] = set()
                territories[owner].update(territory)

        return territories

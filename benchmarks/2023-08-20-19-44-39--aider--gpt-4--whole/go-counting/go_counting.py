WHITE = 'W'
BLACK = 'B'
NONE = ' '

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = [list(row) for row in board]

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

        owner = self.board[y][x]
        if owner in 'BW':
            return owner, set()

        territory = set()
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if (x, y) not in territory:
                territory.add((x, y))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < len(self.board[0]) and 0 <= ny < len(self.board)):
                        if self.board[ny][nx] == ' ':
                            stack.append((nx, ny))
                        elif self.board[ny][nx] in 'BW':
                            if owner == ' ':
                                owner = self.board[ny][nx]
                            elif owner != self.board[ny][nx]:
                                return ' ', set()
        return owner, territory

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        territories = {'B': set(), 'W': set(), ' ': set()}
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] == ' ':
                    owner, territory = self.territory(x, y)
                    territories[owner].update(territory)
        return territories

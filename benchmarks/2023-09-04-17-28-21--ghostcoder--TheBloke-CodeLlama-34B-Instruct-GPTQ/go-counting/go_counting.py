
#!/usr/bin/env python3

BLACK = 'B'
WHITE = 'W'
EMPTY = '.'
from collections import defaultdict

class Board:
    """Count territories of each player in a Go game
    
    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self._board = board
        self._height = len(board)
        self._width = len(board[0])

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def _get_neighbours(self, x, y):
        neighbours = []
        # top neighbour
        if y > 0:
            neighbours.append((x, y - 1))
        # bottom neighbour
        if y < self.height - 1:
            neighbours.append((x, y + 1))
        # left neighbour
        if x > 0:
            neighbours.append((x - 1, y))
        # right neighbour
        if x < self.width - 1:
            neighbours.append((x + 1, y))
        return neighbours

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
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ValueError("Coordinates out of range")

        visited = set()
        queue = [(x, y)]
        owner = ""
        while queue:
            coord = queue.pop(0)
            if coord in visited:
                continue
            visited.add(coord)
            cell = self._board[coord[1]][coord[0]]
            if cell == EMPTY:
                queue += self._get_neighbours(*coord)
            else:
                owner = cell
        return (owner, visited)

    def territories(self):
        """Find the owners and the territories of the whole board
        
        Args:
            none
        
        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        result = {BLACK: set(), WHITE: set()}
        for row in range(self.height):
            for col in range(self.width):
                if self._board[row][col] != EMPTY:
                    owner, territory = self.territory(col, row)
                    result[owner].update(territory)
        return result

def main():
    board = [
        '  B  ',
        ' B B ',
        'B W B',
        ' W W ',
        '  W  ',
    ]
    bd = Board(board)
    print(bd.territories())

if __name__ == "__main__":
    main()

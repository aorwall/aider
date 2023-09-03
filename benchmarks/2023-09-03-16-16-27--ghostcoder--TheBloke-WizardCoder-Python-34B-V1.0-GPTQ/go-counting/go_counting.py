
class Board:
    """Count territories of each player in a Go game
    
    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.columns = len(board[0])

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
        # Check if the input coordinates are valid
        if x < 0 or x >= self.columns or y < 0 or y >= self.rows:
            raise ValueError("Invalid coordinate")

        # Initialize variables
        visited = [[False]*self.columns for _ in range(self.rows)]
        owner = ""
        group = set()

        # Define recursive helper function to traverse the board
        def dfs(x, y):
            nonlocal visited, group, owner
            if visited[y][x]:
                return
            visited[y][x] = True
            group.add((x, y))
            if self.board[y][x] == 'W':
                owner = 'W'
            elif self.board[y][x] == 'B':
                owner = 'B'
            else:
                return

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < self.columns and 0 <= ny < self.rows and not visited[ny][nx] and self.board[ny][nx] != ' ':
                    dfs(nx, ny)

        # Call the helper function starting at the input position
        dfs(x, y)
        return owner, group

    def territories(self):
        """Find the owners and the territories of the whole board
        
        Args:
            none
        
        Returns:
            dict(str, set): A dictionary whose key being the owner,
                          i.e. "W", "B".  The value being a set
                          of coordinates owned by the owner.
        """
        result = {"W":set(), "B":set()}
        visited = [[False]*self.columns for _ in range(self.rows)]

        # Traverse the entire board recursively
        for y in range(self.rows):
            for x in range(self.columns):
                if not visited[y][x] and self.board[y][x] != ' ':
                    owner, group = self.territory(x, y)
                    result[owner].update(group)

        return result

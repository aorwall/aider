class ConnectGame:
    def __init__(self, rows=6, cols=7):
        self._rows = rows
        self._cols = cols
        self._board = [["."]*cols for _ in range(rows)]
        self._current_player = "O"
        self._winner = None
        self._turns = 0

        # Count how many pieces each player has on their side of the board
        o_count = sum([row.count("O") for row in self._board[:self._rows // 2]) + [row.count("O") - 1 if "O" in row else 0 for row in self._board[-1:0:-1]]
        x_count = sum([row.count("X") for row in self._board[:self._rows // 2] + [row.count("X") - 1 if "X" in row else 0 for row in self._board[-1:0:-1]])
        self._player_starting = "O"
        if o_count > x_count:
            self._player_starting = "X"

    def drop_piece(self, col):
        """Drop a piece down the specified column"""
        if self._winner is not None:
            raise ValueError("Game already won!")
        if col < 0 or col >= self._cols or self._board[0][col] != ".":
            raise ValueError("Invalid move")
        for i in range(self._rows-1, -1, -1):
            if self._board[i][col] == ".":
                self._board[i][col] = self._current_player
                break
        self._turns += 1
        self._current_player = "X" if self._current_player == "O" else "O"
        self._winner = self.check_win()

    def check_win(self):
        """Check for win conditions"""
        for row in range(self._rows):
            for col in range(self._cols):
                if self._board[row][col] != ".":
                    if (self._check_horizontal(self._board[row][col], col, row)
                           or self._check_vertical(self._board[row][col], col, row)
                           or self._check_diagonal(self._board[row][col], col, row, "/")
                           or self._check_diagonal(self._board[row][col], col, row, "\\")):
                        return self._board[row][col]
        return None

    def _check_horizontal(self, symbol, col, row):
        """Check for horizontal connection"""
        count = 0
        for c in range(max(0, col-4), min(self._cols, col+5)):
            if self._board[row][c] == symbol:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
        return False

    def _check_vertical(self, symbol, col, row):
        """Check for vertical connection"""
        count = 0
        for r in range(min(0, row-4), min(self._rows, row+5)):
            if self._board[r][col] == symbol:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
        return False

    def _check_diagonal(self, symbol, col, row, direction="/"):
        """Check for diagonal connection"""
        count = 0
        if direction == "/":
            inc_row = lambda r: r-1
            inc_col = lambda c: c+1
        elif direction == "\\":
            inc_row = lambda r: r+1
            inc_col = lambda c: c-1
        else:
            raise ValueError("Invalid direction")
        r, c = row, col
        while r >= 0 and c < self._cols:
            if self._board[r][c] == symbol:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
            r, c = inc_row(r), inc_col(c)
        return False

    @property
    def winner(self):
        return self._winner

    @property
    def current_player(self):
        return self._current_player

    @property
    def turns(self):
        return self._turns

    @property
    def player_starting(self):
        return self._player_starting
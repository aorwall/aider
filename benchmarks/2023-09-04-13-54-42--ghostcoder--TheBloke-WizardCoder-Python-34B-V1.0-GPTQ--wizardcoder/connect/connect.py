
import numpy as np
from collections import defaultdict

class ConnectGame:
    def __init__(self, board):
        self.board = np.array([list(map(str, row)) for row in board], dtype='<U2')
        self.rows, self.cols = self.board.shape

    def _is_winning_connection(self, x, y, dx, dy, color):
        if not (0 <= x < self.rows and 0 <= y < self.cols):
            return False

        if self.board[x, y] != color:
            return False

        if x == self.rows - 1 or y == self.cols - 1:
            return True

        return self._is_winning_connection(x+dx, y+dy, dx, dy, color)

    def get_winner(self):
        for color in ('O', 'X'):
            for dx, dy in ((1, 0), (0, 1), (1, 1)):
                for x, y in zip(range(-1, self.rows), range(self.cols)):
                    if self._is_winning_connection(x, y, dx, dy, color):
                        return color
        return None


# Example usage:
board = """
. O . X .
 . X X O .
  O O O X .
   . X O X O
    X O O O X
"""
connect_game = ConnectGame(board.strip().split('\n'))
print(connect_game.get_winner()) # Output: 'O'

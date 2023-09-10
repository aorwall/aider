import sys

class ConnectGame:
    def __init__(self, board):
        self.board = board
        self.width = len(board[0])
        self.height = len(board)

    def get_winner(self):
        # Check if either player has won
        for player in ["O", "X"]:
            if self.is_winner(player):
                return player

        return None

    def is_winner(self, player):
        # Check if there is a path from the top to the bottom for the given player
        for i in range(self.height):
            if self.is_connected(player, i, 0):
                return True
            if self.is_connected(player, 0, i):
                return True

        return False

    def is_connected(self, player, row, col):
        # Check if there is a path from the given cell to the opposite side of the board for the given player
        if row == 0 or row == self.height - 1 or col == 0 or col == self.width - 1:
            return True

        if self.board[row][col] != player:
            return False

        for row_offset in [-1, 1]:
            for col_offset in [-1, 1]:
                if row + row_offset >= 0 and row + row_offset < self.height:
                    if col + col_offset >= 0 and col + col_offset < self.width:
                        if self.board[row + row_offset][col + col_offset] == player:
                            if self.is_connected(player, row + row_offset, col + col_offset):
                                return True

        return False

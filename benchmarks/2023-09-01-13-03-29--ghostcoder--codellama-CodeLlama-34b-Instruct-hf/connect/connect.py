
class ConnectGame:
    def __init__(self, board):
        self.board = board

    def get_winner(self):
        for row in self.board:
            for col in row:
                if col == 'O' and self.board.index(row) == self.board.index(col):
                    return 'O'
                elif col == 'X' and self.board.index(row) == self.board.index(col):
                    return 'X'
        return None

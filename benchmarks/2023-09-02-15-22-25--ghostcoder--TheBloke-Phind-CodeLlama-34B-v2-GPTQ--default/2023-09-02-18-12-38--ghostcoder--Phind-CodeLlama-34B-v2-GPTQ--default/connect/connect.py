
class ConnectGame:
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

    def get_winner(self):
        for row in range(self.rows):
            if self._check_row(row):
                return 'O'
        for col in range(self.cols):
            if self._check_col(col):
                return 'X'
        return ""

    def _check_row(self, row):
        countx, counto = 0, 0
        for col in range(self.cols):
            if self.board[row][col] == 'X':
                countx += 1
                counto = 0
            elif self.board[row][col] == 'O':
                counto += 1
                countx = 0
            else:
                countx, counto = 0, 0
            if countx >= 3 or counto >= 3:
                return True
        return False

    def _check_col(self, col):
        countx, counto = 0, 0
        for row in range(self.rows):
            if self.board[row][col] == 'X':
                countx += 1
                counto = 0
            elif self.board[row][col] == 'O':
                counto += 1
                countx = 0
            else:
                countx, counto = 0, 0
            if countx >= 3 or counto >= 3:
                return True
        return False

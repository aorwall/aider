class ConnectGame:
    def __init__(self, board):
        self.board = board
        self.width = len(board[0])
        self.height = len(board)

    def get_winner(self):
        def check_winner(player, row, col, dx, dy):
            for _ in range(self.width):
                if self.board[row][col] != player:
                    break
                row += dy
                col += dx
            else:
                return True
            return False

        for player in ('O', 'X'):
            for row in range(self.height):
                for col in range(self.width):
                    if self.board[row][col] == player:
                        if check_winner(player, row, col, 0, 1) or check_winner(player, row, col, 1, 0):
                            return player
        return ""

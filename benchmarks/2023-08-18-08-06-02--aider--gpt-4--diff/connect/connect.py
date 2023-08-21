
class ConnectGame:
    def __init__(self, board):
        self.board = [list(row) for row in board.split("\n") if row]
        self.x_positions = {(i, j) for i, row in enumerate(self.board) for j, cell in enumerate(row) if cell == 'X'}
        self.o_positions = {(i, j) for i, row in enumerate(self.board) for j, cell in enumerate(row) if cell == 'O'}

    def get_winner(self):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == 'X' and self.dfs(i, j, 'X', {(i, j)}, self.x_positions):
                    return 'X'
                if cell == 'O' and self.dfs(i, j, 'O', {(i, j)}, self.o_positions):
                    return 'O'
        return ''

    def dfs(self, i, j, player, visited, positions):
        if player == 'X' and j == len(self.board[0]) - 1:
            return True
        if player == 'O' and i == len(self.board) - 1:
            return True

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(self.board) and 0 <= nj < len(self.board[0]) and (ni, nj) not in visited and (ni, nj) in positions:
                if self.dfs(ni, nj, player, visited | {(ni, nj)}, positions):
                    return True

        return False

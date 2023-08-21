class ConnectGame:
    def __init__(self, board):
        self.board = [list(row) for row in board.split("\n")]

    def get_winner(self):
        for i in range(len(self.board)):
            if self.dfs(i, 0, 'X', len(self.board[0])-1, set()):
                return 'X'
        for j in range(len(self.board[0])):
            if self.dfs(0, j, 'O', len(self.board)-1, set()):
                return 'O'
        return ''

    def dfs(self, i, j, player, target, visited):
        if i < 0 or i >= len(self.board) or j < i or j >= len(self.board[0]) + i or (i, j) in visited or self.board[i][j] != player:
            return False
        if (player == 'X' and j - i == target) or (player == 'O' and i == target):
            return True
        visited.add((i, j))
        return self.dfs(i-1, j, player, target, visited) or self.dfs(i+1, j, player, target, visited) or \
               self.dfs(i, j-1, player, target, visited) or self.dfs(i, j+1, player, target, visited) or \
               self.dfs(i-1, j+1, player, target, visited) or self.dfs(i+1, j-1, player, target, visited)
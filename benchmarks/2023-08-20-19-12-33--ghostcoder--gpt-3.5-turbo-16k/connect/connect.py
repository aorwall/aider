class ConnectGame:
    def __init__(self, board):
        self.board = board

    def get_winner(self):
        # Check if player O has won by connecting top and bottom
        for col in range(len(self.board[0])):
            if self.board[0][col] == 'O':
                if self.dfs(0, col, 'O', set()):
                    return 'O'

        # Check if player X has won by connecting left and right
        for row in range(len(self.board)):
            if self.board[row][0] == 'X':
                if self.dfs(row, 0, 'X', set()):
                    return 'X'

        # No winner
        return ''

    def dfs(self, row, col, player, visited):
        if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[0]):
            return False

        if (row, col) in visited:
            return False

        if self.board[row][col] != player:
            return False

        if player == 'O' and row == len(self.board) - 1:
            return True

        if player == 'X' and col == len(self.board[0]) - 1:
            return True

        visited.add((row, col))

        return (
            self.dfs(row - 1, col, player, visited) or
            self.dfs(row + 1, col, player, visited) or
            self.dfs(row, col - 1, player, visited) or
            self.dfs(row, col + 1, player, visited) or
            self.dfs(row - 1, col + 1, player, visited) or
            self.dfs(row + 1, col - 1, player, visited)
        )
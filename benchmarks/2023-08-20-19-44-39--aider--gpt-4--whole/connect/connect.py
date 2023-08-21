class ConnectGame:
    def __init__(self, board):
        self.board = [list(row) for row in board.split("\n") if row]
        self.height = len(self.board)
        self.width = len(self.board[0])

    def get_winner(self):
        for player in ['X', 'O']:
            if self.check_winner(player):
                return player
        return ''

    def check_winner(self, player):
        stack = []
        visited = set()
        if player == 'X':
            stack = [(i, j) for i in range(self.height) for j, cell in enumerate(self.board[i]) if cell == player]
        elif player == 'O':
            stack = [(i, j) for j in range(self.width) for i, cell in enumerate(self.board[j]) if cell == player]

        while stack:
            x, y = stack.pop()
            if player == 'X' and y == self.width - 1 or player == 'O' and x == self.height - 1:
                return True
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.height and 0 <= ny < self.width and self.board[nx][ny] == player:
                    stack.append((nx, ny))
        return False

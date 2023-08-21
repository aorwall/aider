WHITE = 'W'
BLACK = 'B'

class Board:
    def __init__(self, board):
        self.board = [list(row) for row in board]
        self.visited = set()

    def territory(self, x, y):
        if not (0 <= x < len(self.board[0]) and 0 <= y < len(self.board)):
            raise ValueError('Invalid coordinate')
        if self.board[y][x] != ' ':
            return '', set()

        territory = set()
        stack = [(x, y)]
        player = None
        while stack:
            x, y = stack.pop()
            if (x, y) in self.visited or self.board[y][x] != ' ':
                continue
            self.visited.add((x, y))
            territory.add((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.board[0]) and 0 <= ny < len(self.board):
                    if self.board[ny][nx] in 'BW':
                        if player is None:
                            player = self.board[ny][nx]
                        elif player != self.board[ny][nx]:
                            return '', set()
                    else:
                        stack.append((nx, ny))

        return player if player is not None else '', territory

    def territories(self):
        territories = {BLACK: set(), WHITE: set(), '': set()}
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] == ' ' and (x, y) not in self.visited:
                    player, territory = self.territory(x, y)
                    territories[player].update(territory)
        return territories
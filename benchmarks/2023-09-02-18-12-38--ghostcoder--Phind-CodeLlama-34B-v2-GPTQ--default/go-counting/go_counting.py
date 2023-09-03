
class Board:

    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

    def territory(self, x, y):
        if x < 0 or y < 0 or x >= self.cols or y >= self.rows:
            raise ValueError("Invalid coordinate")

        owner = self.board[y][x]
        territories = set()

        if owner == '':
            return '', territories

        stack = [(x, y)]
        while stack:
            curr_x, curr_y = stack.pop()

            if (curr_x, curr_y) in territories:
                continue

            territories.add((curr_x, curr_y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nxt_x, nxt_y = curr_x + dx, curr_y + dy
                if nxt_x >= 0 and nxt_y >= 0 and nxt_x < self.cols and nxt_y < self.rows and self.board[nxt_y][nxt_x] == '':
                    stack.append((nxt_x, nxt_y))

        return owner, territories

    def territories(self):
        result = {'W': set(), 'B': set()}
        for y in range(self.rows):
            for x in range(self.cols):
                piece = self.board[y][x]
                if piece not in ['', 'W', 'B']:
                    raise ValueError('Invalid piece on the board')
                elif piece != '':
                    _, territory = self.territory(x, y)
                    result[piece] |= territory
        return result

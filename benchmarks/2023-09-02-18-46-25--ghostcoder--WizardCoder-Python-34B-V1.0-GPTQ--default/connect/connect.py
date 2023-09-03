
class ConnectGame:
    def __init__(self, board):
        self.board = board
        self.rows = len(self.board)
        self.cols = len(self.board[0])

    def get_winner(self):
        # Check if the game is already over
        for i in range(self.rows):
            for j in range(self.cols):
                if self._check_winning_move((i,j), 'O'):
                    return 'O'
                elif self._check_winning_move((i,j), 'X'):
                    return 'X'

        return None

    def _check_winning_move(self, start_pos, player):
        directions = [(1, 0), (0, -1), (-1, -1), (-1, 1)]
        visited = set()
        stack = [start_pos]
        while stack:
            current_row, current_col = stack.pop()
            if (current_row, current_col) in visited:
                continue

            visited.add((current_row, current_col))
            if self.board[current_row][current_col] != player:
                continue

            for direction in directions:
                next_row = current_row + direction[0]
                next_col = current_col + direction[1]
                if 0 <= next_row < self.rows and 0 <= next_col < self.cols and self.board[next_row][next_col] == player and (next_row, next_col) not in visited:
                    stack.append((next_row, next_col))

            # Check if we have connected all the pieces of a player to the opposite side
            if player == 'O':
                if current_row == self.rows-1 or current_col == 0:
                    return True
            else:
                if current_row == 0 or current_col == self.cols-1:
                    return True

        return False

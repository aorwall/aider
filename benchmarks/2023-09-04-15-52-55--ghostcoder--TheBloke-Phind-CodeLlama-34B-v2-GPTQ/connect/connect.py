
from collections import defaultdict

class ConnectGame:
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.graph = defaultdict(set)

        # Build graph representation
        for r in range(self.rows):
            for c in range(self.cols):
                cell = board[r][c]
                if cell != '.':
                    if c > 0 and board[r][c - 1] == cell:
                        self.graph[(cell, 'h')].add((r, c))
                        self.graph[(cell, 'h')].add((r, c - 1))
                    if r > 0 and board[r - 1][c] == cell:
                        self.graph[(cell, 'v')].add((r, c))
                        self.graph[(cell, 'v')].add((r - 1, c))

    def _is_connected(self, node, visited, direction):
        stack = [node]
        while stack:
            curr_node = stack.pop()
            if curr_node not in visited:
                visited.add(curr_node)
                if len(visited) >= 4:
                    return True
                for neighbor in self.graph[(curr_node[direction], 'h', 'v')[curr_node[direction]=='.']]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return False

    def get_winner(self):
        horizontal_visited = set()
        vertical_visited = set()
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.board[r][c]
                if cell != '.':
                    if (r, c) not in horizontal_visited:
                        horizontal_visited.add((r, c))
                        if self._is_connected((r, c), horizontal_visited, 'h'):
                            return cell
                    if (r, c) not in vertical_visited:
                        vertical_visited.add((r, c))
                        if self._is_connected((r, c), vertical_visited, 'v'):
                            return cell
        return ""

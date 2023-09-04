
import re
from collections import defaultdict

class ConnectGame:
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.player_map = {'.': None, 'O': 'O', 'X': 'X'}
        self.winning_combinations = []

    def _get_neighbors(self, row, col):
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        valid_neighbors = []

        for neighbor in neighbors:
            r, c = neighbor

            # Check if the neighbor is within the bounds of the board
            if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
                continue

            # Check if the neighbor is already part of a winning combination
            if neighbor in self.winning_combinations:
                continue

            valid_neighbors.append(neighbor)

        return valid_neighbors

    def _find_connected_components(self, start_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            node = queue.popleft()

            if node in visited:
                continue

            visited.add(node)

            for neighbor in self._get_neighbors(*node):
                queue.append(neighbor)

        return list(visited)

    def _is_winning_move(self, move):
        row, col = move
        player = self.board[row][col]

        # Check if the move creates a horizontal line of three consecutive pieces
        for i in range(-1, 2):
            if self.board[row][col + i] != player:
                break
        else:
            return True

        # Check if the move creates a vertical line of three consecutive pieces
        for i in range(-1, 2):
            if self.board[row + i][col] != player:
                break
        else:
            return True

        # Check if the move creates a diagonal line of three consecutive pieces
        for i in range(-1, 2):
            if self.board[row + i][col + i] != player:
                break
        else:
            return True

        return False

    def get_winner(self):
        # Initialize the graph with each cell as a node
        graph = defaultdict(list)

        for row in range(self.rows):
            for col in range(self.cols):
                node = (row, col)
                graph[node].extend(self._get_neighbors(row, col))

        # Find connected components using BFS
        for node in graph:
            component = self._find_connected_components(node)

            # If the component contains more than one node, check if it forms a winning combination
            if len(component) > 1:
                for move in component:
                    if self._is_winning_move(move):
                        return self.player_map[self.board[move]]

        return None


from enum import Enum
from typing import Dict, List, Set, Tuple

class Player(Enum):
    WHITE = 'W'
    BLACK = 'B'

class InvalidMoveError(Exception):
    pass

class Board:
    def __init__(self, board: List[List[str]]):
        self._board = board

    def _get_neighbours(self, x: int, y: int) -> List[Tuple[int, int]]:
        directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        neighbours = [(x + dx, y + dy) for dx, dy in directions]
        return neighbours

    def _valid_coordinates(self, x: int, y: int) -> bool:
        rows = len(self._board)
        cols = len(self._board[0])
        return 0 <= x < rows and 0 <= y < cols

    def territory(self, x: int, y: int) -> Tuple[Player, Set[Tuple[int, int]]]:
        if not self._valid_coordinates(x, y):
            raise ValueError("Invalid coordinate")

        player = Player(self._board[x][y]).name
        visited = {(x, y)}
        stack = [(x, y)]

        while stack:
            current_x, current_y = stack.pop()
            for nx, ny in self._get_neighbours(current_x, current_y):
                if (nx, ny) not in visited and self._valid_coordinates(nx, ny) and \
                   ((player == 'W' and self._board[nx][ny] != 'B') or 
                    (player == 'B' and self._board[nx][ny] != 'W')) and \
                    self._board[nx][ny] != '.':
                    visited.add((nx, ny))
                    stack.append((nx, ny))
        return Player(player), visited

    def territories(self) -> Dict[str, Set[Tuple[int, int]]]:
        result = {Player.WHITE.value: set(), Player.BLACK.value: set()}
        visited = set()

        for r in range(len(self._board)):
            for c in range(len(self._board[r])):
                if (r, c) not in visited and self._board[r][c] in ('W', 'B'):
                    player, territory = self.territory(r, c)
                    result[player.value] = result[player.value].union(territory)
                    visited = visited.union(territory)
        return result

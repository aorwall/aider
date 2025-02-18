from typing import List, Tuple

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class WordSearch:
    def __init__(self, puzzle):
        self._puzzle = [list(row) for row in puzzle]
        self._height = len(self._puzzle)
        self._width = len(self._puzzle[0])

    def _find_first(self, word: str) -> Point:
        for y in range(self._height):
            for x in range(self._width):
                if self._puzzle[y][x] == word[0]:
                    for dx, dy in [(0, 1), (1, 0), (-1, 1), (1, -1)]:
                        found = True
                        for k in range(1, len(word)):
                            nx, ny = x + k * dx, y + k * dy
                            if nx < 0 or ny < 0 or nx >= self._width or ny >= self._height or self._puzzle[ny][nx] != word[k]:
                                found = False
                                break
                        if found:
                            return Point(x, y)
        return None

    def search(self, words: List[str]) -> List[Tuple[Point, Point]]:
        results = []
        for word in words:
            start = self._find_first(word)
            if start is not None:
                end = Point(start.x + len(word) - 1, start.y)
                results.append((start, end))
            else:
                results.append(None)
        return results

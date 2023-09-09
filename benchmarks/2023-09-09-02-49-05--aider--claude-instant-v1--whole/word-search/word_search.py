from typing import List, Tuple

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle: List[str]):
        self.puzzle = puzzle

    def search(self, word: str) -> Tuple[Point, Point]:
        for y in range(len(self.puzzle)):
            for x in range(len(self.puzzle[y])):
                if self._search_from(x, y, word):
                    return Point(x, y), Point(x+len(word)-1, y)
        return None

    def _search_from(self, x: int, y: int, word: str) -> bool:
        if len(word) == 0:
            return True
        try:
            if self.puzzle[y][x] == word[0]:
                return self._search_from(x+1, y, word[1:])
        except IndexError:
            return False
        return False

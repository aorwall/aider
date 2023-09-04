from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int
class Point:
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle: str):
        self.rows = puzzle.split('\n')

    def search(self, word: str) -> tuple[Point, Point]:
        for row_num, row in enumerate(self.rows):
            if word in row:
                start_col = row.index(word)
                end_col = start_col + len(word) - 1

                start_point = Point(start_col, row_num)
                end_point = Point(end_col, row_num)

                return (start_point, end_point)

        raise ValueError(f"{word} not found")

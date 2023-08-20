class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        if isinstance(puzzle, list):
            puzzle = '\n'.join(puzzle)
        self.puzzle = [list(row) for row in puzzle.split('\n') if row]

    def search(self, word):
        for y in range(len(self.puzzle)):
            for x in range(len(self.puzzle[y])):
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    if self._check_word(word, x, y, dx, dy):
                        return Point(x, y), Point(x + dx * (len(word) - 1), y + dy * (len(word) - 1))
        return None

    def _check_word(self, word, x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + dx * i, y + dy * i
            if nx < 0 or ny < 0 or ny >= len(self.puzzle) or nx >= len(self.puzzle[ny]) or self.puzzle[ny][nx] != word[i]:
                return False
        return True

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = [list(row) for row in puzzle]

    def search(self, word):
        for y in range(len(self.puzzle)):
            for x in range(len(self.puzzle[y])):
                if self.puzzle[y][x] == word[0]:
                    for direction in [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]:
                        if self._check_word(word, x, y, direction):
                            return (Point(x, y), Point(x + direction[0] * (len(word) - 1), y + direction[1] * (len(word) - 1)))
        return None

    def _check_word(self, word, x, y, direction):
        for i in range(len(word)):
            if x < 0 or y < 0 or y >= len(self.puzzle) or x >= len(self.puzzle[y]) or self.puzzle[y][x] != word[i]:
                return False
            x += direction[0]
            y += direction[1]
        return True

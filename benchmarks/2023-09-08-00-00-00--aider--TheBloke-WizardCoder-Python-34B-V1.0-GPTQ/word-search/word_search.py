class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.cols = len(puzzle[0])

    def find_word(self, word):
        for i in range(self.rows):
            for j in range(self.cols):
                if self._find_horizontal(i, j, word):
                    return True
                if self._find_vertical(i, j, word):
                    return True
                if self._find_diagonal(i, j, word):
                    return True
        return False

    def _find_horizontal(self, row, col, word):
        return self._find_word(row, col, word, (0, 1))

    def _find_vertical(self, row, col, word):
        return self._find_word(row, col, word, (1, 0))

    def _find_diagonal(self, row, col, word):
        return self._find_word(row, col, word, (1, 1))

    def _find_word(self, row, col, word, direction):
        if not word:
            return True
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        if self.puzzle[row][col] != word[0]:
            return False
        temp = self.puzzle[row][col]
        self.puzzle[row][col] = None
        result = self._find_word(row + direction[0], col + direction[1], word[1:], direction)
        self.puzzle[row][col] = temp
        return result

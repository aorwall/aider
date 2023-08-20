class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        word_length = len(word)
        rows = len(self.puzzle)
        cols = len(self.puzzle[0])

        for i in range(rows):
            for j in range(cols):
                if self.puzzle[i][j] == word[0]:
                    for dx, dy in [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]:
                        x, y = i, j
                        found = True
                        for k in range(1, word_length):
                            x += dx
                            y += dy
                            if x < 0 or x >= rows or y < 0 or y >= cols or self.puzzle[x][y] != word[k]:
                                found = False
                                break
                        if found:
                            return Point(j, i), Point(y, x)
        return None, None

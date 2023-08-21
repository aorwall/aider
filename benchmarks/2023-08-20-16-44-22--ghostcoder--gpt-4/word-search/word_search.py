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
                result = self.search_from(x, y, word)
                if result:
                    return Point(x, y), result
        return None

    def search_from(self, x, y, word):
        for dx, dy in [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]:
            end_point = self.search_in_direction(x, y, dx, dy, word)
            if end_point:
                return end_point
        return None

    def search_in_direction(self, x, y, dx, dy, word):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < len(self.puzzle[0]) and 0 <= ny < len(self.puzzle)):
                return None
            if self.puzzle[ny][nx] != word[i]:
                return None
        return Point(nx, ny)
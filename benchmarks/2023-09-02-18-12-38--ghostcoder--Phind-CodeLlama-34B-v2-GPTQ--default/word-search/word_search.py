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
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.cols = len(puzzle[0])
        self.grid = [[''.join(row) for row in zip(*(iter(puzzle),) * 4)] for _ in range(4)]

    def search(self, word):
        orientations = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for start_i in range(self.rows):
            for start_j in range(self.cols):
                for orientation in orientations:
                    position = self._find_word(start_i, start_j, orientation, word)

                    if position is not None:
                        return position

        return None

    def _find_word(self, start_i, start_j, orientation, word):
        i, j = start_i, start_j
        first_position = Point(None, None)
        last_position = Point(None, None)

        for char in word:
            while 0 <= i < self.rows and 0 <= j < self.cols:
                if 0 <= i < self.rows and 0 <= j < self.cols and self.grid[i][j] == char:
                    if first_position.x is None:
                        first_position.x, first_position.y = i, j
                    last_position.x, last_position.y = i, j
                    break
                else:
                    return None

                i, j = i + orientation[0], j + orientation[1]
            else:
                return None

            i += orientation[0]
            j += orientation[1]

        return [first_position, last_position]

import itertools

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
        self.height = len(puzzle)
        self.width = len(puzzle[0])

    def search(self, word):
        # Check rows
        for i in range(len(self.puzzle)):
            if word in "".join(self.puzzle[i]):
                start_index = self.puzzle[i].index(word[0])
                end_index = start_index + len(word) - 1
                return (Point(start_index, i), Point(end_index, i))

        # Check columns
        for j in range(len(self.puzzle[0])):
            column = [row[j] for row in self.puzzle]
            if word in "".join(column):
                start_index = column.index(word[0])
                end_index = start_index + len(word) - 1
                return (Point(j, start_index), Point(j, end_index))

        # Check diagonals
        for k in range(-self.height+1, self.height):
            diagonal = [self.puzzle[i+k][i] for i in range(min(self.height, self.width))]
            if word in "".join(diagonal):
                start_index = diagonal.index(word[0])
                end_index = start_index + len(word) - 1
                return (Point(start_index, start_index+k), Point(end_index, end_index+k))

        return None

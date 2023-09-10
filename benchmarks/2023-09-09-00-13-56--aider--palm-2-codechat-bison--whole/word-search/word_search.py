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
        # Check if the word is in the puzzle.
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[0])):
                if self.puzzle[i][j] == word[0]:
                    # Check if the word can be found in all directions from this starting point.
                    for direction in ['left', 'right', 'up', 'down', 'diagonal_left', 'diagonal_right']:
                        if self.can_find_word(word, i, j, direction):
                            return True
        return False

    def can_find_word(self, word, i, j, direction):
        # Check if the word can be found in the given direction from the given starting point.
        for k in range(len(word)):
            if i + k < 0 or i + k >= len(self.puzzle) or j + k < 0 or j + k >= len(self.puzzle[0]):
                return False
            if self.puzzle[i + k][j + k] != word[k]:
                return False
        return True

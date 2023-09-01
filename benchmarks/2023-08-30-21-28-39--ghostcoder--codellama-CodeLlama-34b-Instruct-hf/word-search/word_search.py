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
        # Find the first letter of the word in the puzzle
        first_letter = word[0]
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if self.puzzle[i][j] == first_letter:
                    # Check if the word is hidden in the puzzle
                    # starting from the current position
                    if self.is_word_hidden(word, i, j):
                        return (i, j), (i + len(word) - 1, j + len(word) - 1)
        return None

    def is_word_hidden(self, word, i, j):
        # Check if the word is hidden in the puzzle
        # starting from the current position
        for k in range(len(word)):
            if self.puzzle[i + k][j + k] != word[k]:
                return False
        return True

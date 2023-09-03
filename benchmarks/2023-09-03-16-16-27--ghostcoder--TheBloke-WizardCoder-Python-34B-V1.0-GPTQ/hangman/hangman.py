# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'

class Hangman:
    def __init__(self, word):
        self.secret_word = list(word)
        self.correct_chars = []
        self.incorrect_chars = set()
        self.max_lives = 9
        self.current_lives = self.max_lives

    def guess(self, char):
        """Takes a character as input and returns True if correct, False otherwise"""
        if self.get_status() != STATUS_ONGOING:
            # If the game has ended, raise an exception.
            raise ValueError("Game has already ended!")
        elif char in self.correct_chars or char in self.incorrect_chars:
            return bool(char in self.correct_chars)
        else:
            if char in self.secret_word:
                self.correct_chars.append(char)
                return True
            else:
                self.incorrect_chars.add(char)
                self.current_lives -= 1
                if self.current_lives == 0:
                    self.status = STATUS_LOSE
                return False

    def get_masked_word(self):
        """Returns the masked word after guessing a character."""
        return ['*' if c not in self.correct_chars else c for c in self.secret_word]

    def get_status(self):
        """Returns the current status of the game."""
        if '_' not in self.get_masked_word():
            self.status = STATUS_WIN
        elif self.current_lives <= 0:
            self.status = STATUS_LOSE
        else:
            self.status = STATUS_ONGOING
        return self.status

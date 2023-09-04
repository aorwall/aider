import string

# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.masked_word = '_' * len(word)
        self.remaining_guesses = 9
        self.guessed_chars = set()
        self.status = STATUS_ONGOING

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError('The game has already ended.')

        char = char.lower()
        if char in self.guessed_chars:
            return False

        self.guessed_chars.add(char)
        if char in self.word:
            indices = [i for i, letter in enumerate(self.word) if letter == char]
            for index in indices:
                self.masked_word = self.masked_word[:index] + char + self.masked_word[index + 1:]

            if self.masked_word == self.word:
                self.status = STATUS_WIN
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses == 0:
                self.status = STATUS_LOSE

        return True

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

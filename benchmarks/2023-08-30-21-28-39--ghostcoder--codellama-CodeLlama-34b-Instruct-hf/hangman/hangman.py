# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = '_' * len(word)

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        if char in self.word:
            self.masked_word = self.masked_word.replace(char, char)
            if self.masked_word == self.word:
                self.status = STATUS_WIN
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses == 0:
                self.status = STATUS_LOSE

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

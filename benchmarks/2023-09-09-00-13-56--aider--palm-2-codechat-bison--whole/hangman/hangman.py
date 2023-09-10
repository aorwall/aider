# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.masked_word = '___'
        self.status = STATUS_ONGOING

    def guess(self, char):
        if char in self.word:
            # The letter is in the word, so update the masked word to show it.
            for i in range(len(self.word)):
                if self.word[i] == char:
                    self.masked_word = self.masked_word[:i] + char + self.masked_word[i + 1:]
        else:
            # The letter is not in the word, so decrement the number of remaining guesses.
            self.remaining_guesses -= 1

        # Check if the game is over.
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
        elif self.masked_word == self.word:
            self.status = STATUS_WIN

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

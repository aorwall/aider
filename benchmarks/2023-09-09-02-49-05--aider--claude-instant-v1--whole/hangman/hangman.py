# Game status categories
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:

    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.secret_word = word
        self.guessed_letters = []

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        if char not in self.secret_word and char not in self.guessed_letters:
            self.remaining_guesses -= 1

        self.guessed_letters.append(char)

        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
        elif set(self.secret_word) <= set(self.guessed_letters):
            self.status = STATUS_WIN

    def get_masked_word(self):
        masked = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                masked += letter
            else:
                masked += "_"
        return masked

    def get_status(self):
        return self.status

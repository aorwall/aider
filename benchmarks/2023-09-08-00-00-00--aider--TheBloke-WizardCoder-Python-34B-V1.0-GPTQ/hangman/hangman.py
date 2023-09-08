# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'

class Hangman:
    def __init__(self, word):
        self.word = word
        self.status = STATUS_ONGOING
        self.missed_letters = []
        self.guessed_letters = []

    def guess(self, letter):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        if letter in self.guessed_letters or letter in self.missed_letters:
            return

        if letter in self.word:
            self.guessed_letters.append(letter)
            if self._has_won():
                self.status = STATUS_WIN
        else:
            self.missed_letters.append(letter)
            if self._is_lost():
                self.status = STATUS_LOSE

    def _is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def _is_lost(self):
        return len(self.missed_letters) >= 6

    def __str__(self):
        return f"Word: {self.word}\nMissed letters: {self.missed_letters}\nGuessed letters: {self.guessed_letters}\nStatus: {self.status}"

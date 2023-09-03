# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        ...
            if self.masked_word == self.word:
                self.status = 'win'
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses <= 0: # Changed from == 0 to <= 0
                self.status = 'lose'

    ...
        return True
    }
}

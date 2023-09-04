import random
from typing import List

# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.secret_word = word
        self.masked_word = ['*'] * len(word)
        self.remaining_guesses = 9 # Changed from 6 to 9
        self.used_chars = set()
        self.status = STATUS_ONGOING

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        if char in self.used_chars:
            self.remaining_guesses -= 1 # Penalize for guessing a used character
            return

        self.used_chars.add(char)

        found = False
        masked_word = []
        for secret_char in self.secret_word:
            if secret_char == char:
                found = True
                masked_word.append(char)
            else:
                masked_word.append(self.masked_word[self.secret_word.index(secret_char)] if char not in self.used_chars else "*")

        self.masked_word = masked_word

        if not found:
            self.remaining_guesses -= 1

        if all([c != '*' for c in self.masked_word]):
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return ''.join(self.masked_word)

    def get_status(self):
        return self.status


def pick_random_word():
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    return random.choice(words)

if __name__ == "__main__":
    word = pick_random_word()
    game = Hangman(word)
    print("Welcome to hangman!")
    while game.get_status() == STATUS_ONGOING:
        print("\nYour word: {}".format(game.get_masked_word()))
        print("You have {} guesses left".format(game.remaining_guesses))
        char = input("Enter your guess (one character): ")
        try:
            game.guess(char)
        except ValueError as e:
            print(e)

    if game.get_status() == STATUS_WIN:
        print("\nCongratulations! You won :)")
    else:
        print("\nSorry, you lost :(\nThe word was: {}".format(word))

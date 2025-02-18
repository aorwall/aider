import re
from typing import List


# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word: str):
        """Initializes the game state"""
        # Initialize private attributes
        self._word: str = word
        self._masked_word: List[str] = list('*' * len(word))
        self._remaining_guesses: int = 9
        self._status: str = STATUS_ONGOING

        # Sanity check
        assert all(c.isalpha() for c in word), f'"{word}" must contain only letters.'

    @property
    def remaining_guesses(self) -> int:
        """Returns the number of remaining guesses"""
        return self._remaining_guesses

    @property
    def masked_word(self) -> List[str]:
        """Returns the current masked word"""
        return self._masked_word

    @property
    def status(self) -> str:
        """Returns the current game status"""
        return self._status

    def _update_state(self, char: str) -> None:
        """Updates the internal state based on the provided character"""
        # Check if the game has already been won or lost
        if self._status != STATUS_ONGOING:
            raise ValueError(f'Game has already {self._status}.')

        # Update the masked word
        matches = [(i, c) for i, c in enumerate(self._word) if c == char]
        for i, _ in matches:
            self._masked_word[i] = char

        # Check if the user has won
        if all(c != '*' for c in self._masked_word):
            self._status = STATUS_WIN

        # Decrement the number of remaining guesses
        self._remaining_guesses -= 1

        # Check if the user has lost
        if self._remaining_guesses <= 0:
            self._status = STATUS_LOSE

    def guess(self, char: str) -> None:
        """Processes a guess by the user"""
        # Validate input
        if not char.isalpha():
            raise ValueError(f'"{char}" must be a letter.')

        # Update the internal state
        self._update_state(char)

    def get_masked_word(self) -> List[str]:
        """Returns the current masked word"""
        return self._masked_word

    def get_status(self) -> str:
        """Returns the current game status"""
        return self._status


if __name__ == '__main__':
    # Test the implementation
    secret_word = 'apple'
    game = Hangman(secret_word)

    print(f'Secret word: {secret_word}')
    while True:
        try:
            guess = input('Guess a letter: ')
            game.guess(guess)
            print(f'Masked word: {"".join(game.get_masked_word())}')
            print(f'Remaining guesses: {game.remaining_guesses}')
            if game.status != STATUS_ONGOING:
                break
        except ValueError as e:
            print(e)

    print(f'Status: {game.status}')

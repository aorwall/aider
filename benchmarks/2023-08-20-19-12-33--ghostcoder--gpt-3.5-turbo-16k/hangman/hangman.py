def test_winning_on_last_guess_still_counts_as_a_win(self):
    game = Hangman('apple')
    game.guess('a')
    game.guess('p')
    game.guess('l')
    game.guess('e')
    self.assertEqual(game.get_status(), hangman.STATUS_WIN)

def test_after_10_failures_the_game_is_over(self):
    game = Hangman('apple')
    game.guess('q')
    game.guess('w')
    game.guess('r')
    game.guess('t')
    game.guess('y')
    game.guess('u')
    game.guess('i')
    game.guess('o')
    game.guess('s')
    game.guess('d')
    self.assertEqual(game.get_status(), hangman.STATUS_LOSE)

def test_feeding_a_correct_letter_twice_counts_as_a_failure(self):
    game = Hangman('apple')
    game.guess('a')
    game.guess('a')
    self.assertEqual(game.remaining_guesses, 9)
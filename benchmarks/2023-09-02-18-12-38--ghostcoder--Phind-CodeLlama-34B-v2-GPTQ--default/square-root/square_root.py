def square_root(number):
    if number < 0:
        raise ValueError("Number must be non-negative")
    elif number == 0 or number == 1:
        return number

    guess = number / 2.0
    while True:
        better_guess = (guess + number / guess) / 2.0
        if abs(guess - better_guess) < 0.5:   # precision criteria
            return round(better_guess, 6)
        guess = better_guess

def square_root(number):
    if number < 0:
        raise ValueError("Radicand must be a positive real number")

    guess = number / 2
    while True:
        new_guess = (guess + number / guess) / 2
        if abs(new_guess - guess) < 1e-6:
            return round(new_guess, 6)
        else:
            guess = new_guess

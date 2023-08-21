def square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    if number == 0:
        return 0

    guess = number / 2
    while True:
        new_guess = (guess + number / guess) / 2
        if abs(guess - new_guess) < 1e-6:
            return round(new_guess, 6)  # Round to 6 decimal places
        guess = new_guess
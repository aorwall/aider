def square_root(number):
    if number < 0:
        raise ValueError("Square root is not defined for negative numbers")
    if number == 0:
        return 0

    # Initial guess for the square root
    guess = number / 2

    # Iterate until the guess is close enough
    while True:
        new_guess = (guess + number / guess) / 2
        if abs(new_guess - guess) < 1e-9:
            return new_guess
        guess = new_guess

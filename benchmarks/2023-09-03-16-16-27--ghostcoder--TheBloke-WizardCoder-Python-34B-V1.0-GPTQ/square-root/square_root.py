def square_root(number):
    if number < 0: # negative numbers do not have square roots
        raise ValueError("Number must be non-negative")
    elif number == 0: # edge case where sqrt(0) = 0
        return 0

    x = number / 2 # start with an initial guess of half the number
    while True:
        prev_guess = x
        x = (x + number / x) / 2 # calculate the next guess using the average of current guess and number/current guess
        diff = abs(prev_guess - x)
        if diff <= 0.00001: # set a tolerance threshold at 0.0001
            break

    return round(x, 4) # round off to four decimal places

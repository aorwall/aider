def square_root(number):
    # Check if the input is a natural number
    if number < 0:
        raise ValueError('The input value must be a natural number')

    # Initialize two variables for the iteration process
    start_val = max(1, int(number / 2))
    close_enough = lambda x : abs(x**2 - number) < .000001

    while True:
        better_guess = (start_val + number//start_val)/2

        if close_enough(better_guess):
            return round(better_guess,6)

        start_val = better_guess

def steps(number):
    # Check if the number is less than 1, if true then raise ValueError
    if number < 1:
        raise ValueError('Only positive integers are allowed')

    count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = (3 * number) + 1
        count += 1
    return count

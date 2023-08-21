def square_root(number):
    if number == 0 or number == 1:
        return number

    guess = number
    while True:
        temp = 0.5 * (guess + (number / guess))
        if abs(temp - guess) < 0.00001:
            result = temp
            break
        guess = temp

    return int(result) if result.is_integer() else result

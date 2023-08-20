def square_root(number):
    if number == 0 or number == 1:
        return number

    x = number
    y = 1
    precision = 0.000001  # Define the precision to which we want to calculate the square root

    while x - y > precision:
        x = (x + y) / 2
        y = number / x

    return round(x)
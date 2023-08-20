def square_root(number):
    if number == 0 or number == 1:
        return number

    x = number
    y = 1
    e = 0.000001  # e decides the accuracy level
    while x - y > e:
        x = (x + y) / 2
        y = number / x

    return round(x)

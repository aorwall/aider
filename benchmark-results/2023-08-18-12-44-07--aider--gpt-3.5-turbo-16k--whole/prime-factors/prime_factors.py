def factors(value):
    factors_list = []
    divisor = 2

    while value > 1:
        if value % divisor == 0:
            factors_list.append(divisor)
            value = value / divisor
        else:
            divisor += 1

    return factors_list

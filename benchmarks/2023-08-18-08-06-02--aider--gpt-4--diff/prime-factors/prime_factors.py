def factors(value):
    factors_list = []
    i = 2
    while i <= value:
        if value % i:
            i += 1
        else:
            value //= i
            factors_list.append(i)
    if value > 1:
        factors_list.append(value)
    return factors_list

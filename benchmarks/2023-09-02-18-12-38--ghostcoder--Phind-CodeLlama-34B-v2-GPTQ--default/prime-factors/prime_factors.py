def factors(value):
    i = 2
    result = []
    while i * i <= value:
        if value % i:
            i += 1
        else:
            value //= i
            result.append(i)
    if value > 1:
        result.append(value)
    return result

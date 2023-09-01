def factors(value):
    result = []
    for i in range(2, int(value**0.5) + 1):
        if value % i == 0:
            result.append(i)
            value //= i
    if value > 1:
        result.append(value)
    return result

def sum_of_multiples(level, factors):
    multiples = []
    for factor in factors:
        for i in range(1, level // factor + 1):
            multiples.append(factor * i)
    return sum(set(multiples))
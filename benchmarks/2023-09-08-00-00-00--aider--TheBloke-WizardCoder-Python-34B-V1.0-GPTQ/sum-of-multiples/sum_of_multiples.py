def sum_of_multiples(limit, factors):
    multiples = set()
    for factor in factors:
        if factor != 0:
            for i in range(factor, limit, factor):
                multiples.add(i)
    return sum(multiples)

def sum_of_multiples(limit, multiples):
    if not multiples:
        return 0

    return sum(set(x for x in range(1, limit) if any(x % y == 0 for y in multiples)))

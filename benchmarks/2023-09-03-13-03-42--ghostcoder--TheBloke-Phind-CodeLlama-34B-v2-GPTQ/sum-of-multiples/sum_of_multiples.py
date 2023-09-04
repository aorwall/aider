def sum_of_multiples(limit, multiples):
    def get_factors(factor, limit):
        factors = set()
        current = factor
        while current < limit:
            factors.add(current)
            current += factor
        return factors

    total = 0
    combined_set = set()

    for factor in multiples:
        factors = get_factors(factor, limit)
        combined_set.update(factors)

    total = sum(combined_set)
    return total

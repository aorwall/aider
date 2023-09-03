def sum_of_multiples(limit, multiples):
    result = set()

    for multiple in multiples:
        value = multiple
        while value < limit:
            result.add(value)
            value += limit  # Correct this line

    return sum(result)

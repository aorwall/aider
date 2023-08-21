def sum_of_multiples(limit, multiples):
    result = set()
    for multiple in multiples:
        if multiple == 0:
            continue
        result.update(range(multiple, limit, multiple))
    return sum(result)

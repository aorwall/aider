def sum_of_multiples(limit, multiples):
    """Calculate the sum of all unique multiples of each factor up to a limit."""
    result = set()
    for factor in multiples:
        if factor == 0:
            continue
        multiple = factor
        while multiple < limit:
            result.add(multiple)
            multiple += factor
    return sum(result)

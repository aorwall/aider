def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    for base_value in multiples:
        if base_value != 0:
            for i in range(base_value, limit, base_value):
                unique_multiples.add(i)
    return sum(unique_multiples)

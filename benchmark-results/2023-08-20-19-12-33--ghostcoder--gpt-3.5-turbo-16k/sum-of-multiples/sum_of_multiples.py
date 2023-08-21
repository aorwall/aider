def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    for num in multiples:
        if num == 0:
            continue
        for i in range(num, limit, num):
            unique_multiples.add(i)
    return sum(unique_multiples)
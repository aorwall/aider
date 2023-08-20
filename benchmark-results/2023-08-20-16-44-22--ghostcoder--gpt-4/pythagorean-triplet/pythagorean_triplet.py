def triplets_with_sum(number):
    triplets = []
    for a in range(1, number):
        for b in range(a, number):
            c = number - a - b
            if a*a + b*b == c*c:
                triplets.append([a, b, c])
    return triplets
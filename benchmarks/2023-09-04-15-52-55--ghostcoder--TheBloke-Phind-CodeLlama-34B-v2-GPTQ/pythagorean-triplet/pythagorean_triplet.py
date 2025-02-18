import math

def triplets_with_sum(N):
    results = []

    # Iterate over possible values of a
    for a in range(1, int(math.sqrt(N))):
        # Iterate over possible values of b
        for b in range(a+1, int(math.sqrt(N - a))):
            # Calculate c using the Pythagorean theorem
            c = math.sqrt((a**2) + (b**2))

            # If c is an integer and a + b + c equals N, then we found a valid triplet
            if c.is_integer() and a + b + round(c) == N:
                results.append([int(a), int(b), int(round(c))])

    return results
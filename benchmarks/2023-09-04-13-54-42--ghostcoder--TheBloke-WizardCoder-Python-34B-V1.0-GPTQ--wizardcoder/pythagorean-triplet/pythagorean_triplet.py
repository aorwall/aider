from itertools import combinations
import math

def triplets_with_sum(number):
    triplets = []

    # Iterate through all possible pairs of integers between 1 and number // 2
    for a, b in combinations(range(1, number // 2), 2):

        # Check if the pair satisfies the condition a^2 + b^2 = c^2
        c = math.sqrt(a**2 + b**2)
        if int(c) ** 2 == a**2 + b**2:

            # Check if the sum of the triplet equals to the given number
            if a + b + int(c) == number:
                triplets.append([int(a), int(b), int(c)])

    return triplets

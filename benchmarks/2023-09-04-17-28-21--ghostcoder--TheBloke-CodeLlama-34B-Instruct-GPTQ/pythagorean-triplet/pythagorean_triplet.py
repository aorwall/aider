def triplets_with_sum(number):
    """Return a list of Pythagorean triplets where a + b + c = number"""
    # Initialize empty list to store results
    triplets = []

    # Loop through possible values of 'a'
    for a in range(1, number // 3 + 1):
        # Calculate 'b' using the formula b^2 = a^2 - c^2
        b = int((number ** 2 - (a ** 2)) ** 0.5)

        # Check if 'b' is an integer
        if b % 1 == 0:
            # Calculate 'c' using the formula c = sqrt(a^2 + b^2)
            c = int((a ** 2 + b ** 2) ** 0.5)

            # Check if 'c' is an integer
            if c % 1 == 0:
                # Add triplet to results list
                triplets.append([a, b, c])

    return triplets

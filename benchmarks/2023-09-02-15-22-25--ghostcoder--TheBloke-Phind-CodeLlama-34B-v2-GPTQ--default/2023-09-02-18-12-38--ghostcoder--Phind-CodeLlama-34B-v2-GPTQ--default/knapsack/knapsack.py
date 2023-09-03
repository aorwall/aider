def maximum_value(maximum_weight, items):
    # Initialize a list with zeroes up to the maximum weight + 1
    dp = [0] * (maximum_weight + 1)

    # For each item
    for wi, vi in items:
        # Ensure both wi and vi are integers
        wi, vi = int(wi), int(vi)

        # For each possible weight from the item's weight down to zero
        for w in range(wi, -1, -1):
            # Update the maximum value obtainable with this item included
            dp[w] = max(dp[w], dp[max(0, w - wi)] + vi)

    return dp[0]

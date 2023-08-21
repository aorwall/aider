def maximum_value(maximum_weight, items):
    # Initialize a 2D array for storing the maximum value for each weight
    dp = [[0 for _ in range(maximum_weight + 1)] for _ in range(len(items) + 1)]
    
    # Iterate over the items
    for i in range(1, len(items) + 1):
        for w in range(1, maximum_weight + 1):
            # If the weight of the current item is less than or equal to the current weight
            if items[i - 1]['weight'] <= w:
                # Update the maximum value for the current weight
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1]['weight']] + items[i - 1]['value'])
            else:
                # If the weight of the current item is greater than the current weight, use the previous item's value
                dp[i][w] = dp[i - 1][w]
    
    # Return the maximum value
    return dp[len(items)][maximum_weight]

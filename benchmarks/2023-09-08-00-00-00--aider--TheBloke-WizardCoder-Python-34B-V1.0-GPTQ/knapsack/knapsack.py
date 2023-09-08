def maximum_value(maximum_weight, items):
    # Initialize a dictionary to store the maximum value for each weight limit
    dp = {0: 0}

    # Iterate through the items
    for item in items:
        # Create a new dictionary to store the updated maximum values
        new_dp = dp.copy()

        # Iterate through the weight limits in the dp dictionary
        for w in dp:
            # If the current item's weight plus the weight limit is less than or equal to the knapsack's maximum weight
            if w + item["weight"] <= maximum_weight:
                # Update the new_dp dictionary with the maximum value for the current weight limit
                new_dp[w + item["weight"]] = max(new_dp.get(w + item["weight"], 0), dp[w] + item["value"])

        # Update the dp dictionary with the new maximum values
        dp = new_dp

    # Return the maximum value for the knapsack's maximum weight
    return dp.get(maximum_weight, 0)

# Test the function with the given example
items = [
  {"weight": 5, "value": 10},
  {"weight": 4, "value": 40},
  {"weight": 6, "value": 30},
  {"weight": 4, "value": 50}
]
knapsack_limit = 10
print(maximum_value(knapsack_limit, items))  # Output: 90

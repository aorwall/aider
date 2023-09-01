def maximum_value(W, items):
    # Initialize a dictionary to store the maximum value for each weight
    dp = {0: 0}
    for item in items:
        # Loop through the items and update the dictionary
        for w in range(W + 1):
            if w < item["weight"]:
                dp[w] = dp.get(w, 0)
            else:
                if item["weight"] <= W:
                    dp[w] = max(dp.get(w, 0), dp.get(w - item["weight"], 0) + item["value"])
                else:
                    return dp[W]
    return dp[W]
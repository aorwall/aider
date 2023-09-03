def maximum_value(maximum_weight, items):
    n = len(items)
    dp = [[0]*(maximum_weight+1) for _ in range(n+1)]

    # Fill the first column with zeros as we cannot take any item if we have no capacity
    for i in range(n+1):
        dp[i][0] = 0

    # Fill the first row with zeros as we cannot take any item if we don't have any items to choose from
    for j in range(maximum_weight+1):
        dp[0][j] = 0

    for i in range(1, n+1):
        w_i, v_i = items[i-1]['weight'], items[i-1]['value']
        for j in range(1, maximum_weight+1):
            if j < w_i:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w_i]+v_i)

    return dp[n][maximum_weight]

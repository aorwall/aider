def maximum_value(maximum_weight, items):
    n = len(items)
    dp = [[0 for _ in range(maximum_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, maximum_weight + 1):
            if items[i - 1]['weight'] <= w:
                dp[i][w] = max(items[i - 1]['value'] + dp[i - 1][w - items[i - 1]['weight']], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][maximum_weight]

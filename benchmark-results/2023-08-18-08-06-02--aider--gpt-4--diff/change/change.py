def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target > 0 and min(coins) > target:
        raise ValueError("Change value is smaller than the smallest coin value")
    dp = [None] * (target + 1)
    dp[0] = []
    for coin in coins:
        for i in range(coin, target + 1):
            if dp[i - coin] is not None:
                if dp[i] is None or len(dp[i - coin]) + 1 < len(dp[i]):
                    dp[i] = dp[i - coin] + [coin]
    if dp[target] is None:
        raise ValueError("can't make target with given coins")
    return dp[target]

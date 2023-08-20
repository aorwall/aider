def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target > 0 and min(coins) > target:
        raise ValueError("can't make target with given coins")

    dp = [0] + [float('inf')] * target
    coins_used = [[] for _ in range(target + 1)]
    for coin in coins:
        for i in range(coin, target + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coins_used[i] = coins_used[i - coin] + [coin]

    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    return coins_used[target]
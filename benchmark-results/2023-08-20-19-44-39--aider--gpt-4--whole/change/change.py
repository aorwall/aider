def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target != 0 and min(coins) > target:
        raise ValueError("can't make target with given coins")
    
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, target + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    result = []
    while target:
        for coin in coins:
            if target >= coin and dp[target] == dp[target - coin] + 1:
                result.append(coin)
                target -= coin
                break

    return result

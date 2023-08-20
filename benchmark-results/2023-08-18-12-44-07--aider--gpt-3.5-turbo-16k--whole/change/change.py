def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")
    
    result = []
    i = target
    while i > 0:
        for coin in coins:
            if i - coin >= 0 and dp[i] == dp[i - coin] + 1:
                result.append(coin)
                i -= coin
                break
    
    return result

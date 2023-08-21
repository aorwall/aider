def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("Target cannot be negative")
    if target < min(coins):
        raise ValueError("Target value is smaller than the smallest coin value")
    
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while target >= coin:
            target -= coin
            result.append(coin)
    if target != 0:
        raise ValueError("Cannot make target with given coins")
    return result
def find_fewest_coins(coins, target):
    """Return the minimum number of coins that sum up to the target."""
    min_coins = []
    while target > 0:
        for coin in sorted(coins, reverse=True):
            if coin <= target:
                min_coins.append(coin)
                target -= coin
                break
    return len(min_coins)

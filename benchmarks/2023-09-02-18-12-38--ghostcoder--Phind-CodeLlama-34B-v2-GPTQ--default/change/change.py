def find_fewest_coins(coins, target):
    # Check if target is negative or zero
    if target < 0:
        raise ValueError("target can't be negative")
    elif target == 0:
        return []

    # Sort the coins in descending order
    coins.sort(reverse=True)

    result = []
    current_sum = 0

    for coin in coins:
        while current_sum + coin <= target:
            current_sum += coin
            result.append(coin)

    if current_sum != target:
        raise ValueError("can't make target with given coins")

    return result

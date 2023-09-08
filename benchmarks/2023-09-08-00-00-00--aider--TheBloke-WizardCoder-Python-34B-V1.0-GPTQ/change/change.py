def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    if not coins:
        raise ValueError("no coins available")
    if target < coins[0]:
        raise ValueError("can't make target with given coins")

    # initialize result list with empty list
    result = []
    # initialize index to the last element of the coins list
    index = len(coins) - 1

    # loop until target is zero
    while target > 0:
        # if current coin value is less than or equal to the target
        if coins[index] <= target:
            # add the coin to the result list
            result.append(coins[index])
            # subtract the coin value from the target
            target -= coins[index]
        else:
            # decrement the index
            index -= 1
            # if index goes below zero, raise an exception
            if index < 0:
                raise ValueError("can't make target with given coins")

    return result

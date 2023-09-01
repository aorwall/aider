def find_fewest_coins(coins, target):
    """
    Find the fewest number of coins to make the target amount using the given coins.
    
    Args:
        coins (list): A list of coin values.
        target (int): The target amount to make.
    
    Returns:
        list: A list of the fewest number of coins to make the target amount.
    """
    # Initialize a dictionary to keep track of the number of coins used for each coin value
    coin_counts = {coin: 0 for coin in coins}

    # Loop through the coins and add the number of coins used for each coin value to the dictionary
    for coin in coins:
        coin_counts[coin] += 1

    # Initialize a variable to keep track of the fewest number of coins used
    min_coins = len(coins)

    # Loop through the coins and check if the number of coins used for each coin value is less than the fewest number of coins used
    for coin in coins:
        if coin_counts[coin] < min_coins:
            min_coins = coin_counts[coin]

    # Return the fewest number of coins used
    return min_coins

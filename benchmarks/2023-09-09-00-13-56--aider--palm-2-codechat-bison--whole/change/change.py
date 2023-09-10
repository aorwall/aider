def find_fewest_coins(coins, target):
    """
    Given a list of coins and a target amount, return the fewest number of coins
    that can be used to make change for the target amount.

    Args:
        coins (list): A list of coin denominations.
        target (int): The target amount of change.

    Returns:
        list: A list of the coin denominations used to make change for the target amount.

    Raises:
        ValueError: If the target amount cannot be made with the given coins.
    """

    # Check if the target amount is negative.
    if target < 0:
        raise ValueError("target amount cannot be negative")

    # Check if the coins list is empty.
    if not coins:
        raise ValueError("coins list cannot be empty")

    # Initialize the result list.
    result = []

    # Iterate through the coins list in descending order.
    for coin in coins[::-1]:
        # While the target amount is greater than or equal to the coin value,
        # subtract the coin value from the target amount and add the coin to the result list.
        while target >= coin:
            target -= coin
            result.append(coin)

    # If the target amount is not equal to zero, raise an exception.
    if target != 0:
        raise ValueError("can't make target with given coins")

    # Return the result list.
    return result

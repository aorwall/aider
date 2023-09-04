def find_fewest_coins(coins, target):
    # Sort the coins in ascending order
    coins.sort()

    # Initialize variables
    total = 0
    count = 0
    index = 0

    while total <= target:
        # If there are no more coins left, we need to check if we have enough coins to reach the target
        if index >= len(coins):
            break

        # Add the current coin to the total
        total += coins[index]

        # Increment the counter for the number of coins used
        count += 1

        # Move on to the next coin
        index += 1

    # Remove the last coin from the total and decrease the counter by one
    total -= coins[-1]
    count -= 1

    return count

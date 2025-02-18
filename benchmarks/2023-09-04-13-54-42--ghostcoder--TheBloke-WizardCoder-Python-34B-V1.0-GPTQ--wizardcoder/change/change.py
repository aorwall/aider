from typing import List

def find_fewest_coins(coins: List[int], target: int) -> List[int]:
    # sort coins in ascending order by their value
    sorted_coins = sorted(coins)

    # initialize variables
    current_sum = 0
    min_count = float('inf')
    used_coins = []

    # iterate through all possible combinations of coins
    def dfs(index, count, total, curr_sum):
        nonlocal min_count

        # base case: found combination of coins that adds up to target
        if curr_sum == target:
            if count < min_count:
                min_count = count
                used_coins[:] = curr_used_coins

        elif index < len(sorted_coins):

            # try using next coin
            if curr_sum + sorted_coins[index] <= target:
                curr_used_coins.append(sorted_coins[index])
                dfs(index, count+1, curr_sum+sorted_coins[index], sorted_coins[index])
                curr_used_coins.pop()

            # try skipping next coin
            dfs(index+1, count, curr_sum, curr_used_coins)

    dfs(0, 0, 0, [])

    if min_count == float('inf'):
        raise ValueError("can't make target with given coins")

    return used_coins
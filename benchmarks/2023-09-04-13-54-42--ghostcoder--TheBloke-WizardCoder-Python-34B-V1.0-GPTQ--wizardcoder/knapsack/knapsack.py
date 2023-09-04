from typing import List, Tuple

def maximum_value(maximum_weight: int, items: List[Tuple[int, int]]) -> int:
    # Initialize a table to store the maximum value for each possible weight
    dp = [[0] * (maximum_weight + 1) for _ in range(len(items) + 1)]

    # Fill the table using dynamic programming
    for i in range(1, len(items) + 1):
        wi, vi = items[i - 1]

        for j in range(1, maximum_weight + 1):
            if isinstance(wi, str):
                wi = int(wi)
            if j < wi:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wi] + vi)

    return dp[-1][-1]

# Test cases
print(maximum_value(10, [(5, 10), (4, 40), (6, 30), (4, 50)]))  # Output: 90
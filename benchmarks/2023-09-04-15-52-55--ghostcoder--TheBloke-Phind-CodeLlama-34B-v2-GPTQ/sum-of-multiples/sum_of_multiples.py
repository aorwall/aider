from typing import List

def sum_of_multiples(limit: int, factors: List[int]) -> int:
    total = 0

    for factor in factors:
        for multiple in range(factor, limit, factor):
            total += multiple

    return total - sum([factor for factor in factors if factor > 1]) * (limit - 1) // 2
import itertools
from typing import List, Tuple

Item = Tuple[int, int]

def maximum_value(maximum_weight: int, items: List[Tuple[int, int]]) -> int:
    # Sort the items by their ratio of value to weight in descending order
    sorted_items = sorted(items, key=lambda x: x[1]/x[0] if x[0] != 0 else float('inf'), reverse=True)

    # Initialize the maximum value to 0
    max_val = 0

    # Iterate over different combinations of items
    for i in range(len(sorted_items)+1):
        for combo in itertools.combinations(sorted_items, i):
            # Calculate the current weight and value
            curr_weight = sum([item[0] for item in combo])
            curr_value = sum([item[1] for item in combo])

            # If the current weight does not exceed the maximum weight and the current value is greater than the previous max value
            if curr_weight <= maximum_weight and curr_value > max_val:
                max_val = curr_value

    return max_val

def maximum_value(maximum_weight: int, items: List[Item]) -> int:
    # Sort the items by their ratio of value to weight in descending order
    sorted_items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)

    # Initialize the maximum value to 0
    max_val = 0

    # Iterate over different combinations of items
    for i in range(len(sorted_items)+1):
        for combo in itertools.combinations(sorted_items, i):
            # Calculate the current weight and value
            curr_weight = sum([item[0] for item in combo])
            curr_value = sum([item[1] for item in combo])

            # If the current weight does not exceed the maximum weight and the current value is greater than the previous max value
            if curr_weight <= maximum_weight and curr_value > max_val:
                max_val = curr_value

    return max_val
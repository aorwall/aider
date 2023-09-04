def maximum_value(maximum_weight, items):
    # Initialize variables
    max_val = 0
    current_weight = 0
    taken = [False] * len(items)

    # Sort items by value per weight ratio
    sorted_items = sorted(items, key=lambda x: x['value'] / x['weight'], reverse=True)

    # Loop through sorted items and check if they fit in the knapsack
    for i in range(len(sorted_items)):
        item = sorted_items[i]
        if current_weight + item['weight'] <= maximum_weight:
            # Add item to knapsack
            taken[i] = True
            max_val += item['value']
            current_weight += item['weight']

    # Return maximum value
    return max_val

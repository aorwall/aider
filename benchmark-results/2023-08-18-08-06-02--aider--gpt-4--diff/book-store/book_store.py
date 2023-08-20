from collections import Counter
from itertools import combinations

def total(basket):
    # Define the discounts
    discounts = {1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}
    
    # Count the number of each book in the basket
    counts = Counter(basket)
    
    # Initialize the costs list
    costs = [0] * (len(basket) + 1)
    
    # Calculate the cost for each possible number of distinct books
    for i in range(1, len(basket) + 1):
        costs[i] = min(sum(discounts[len(combination)] * 8 for combination in combinations(counts, i)) + costs[len(basket) - i] for _ in range(i))
    
    # Return the minimum total cost
    return costs[len(basket)]

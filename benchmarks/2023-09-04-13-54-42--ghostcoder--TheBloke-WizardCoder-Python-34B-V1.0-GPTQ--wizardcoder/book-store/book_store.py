from collections import Counter

def total(basket):
    prices = {1: 8, 2: 7.2, 3: 6.4, 4: 5.6, 5: 5}

    # Count the number of each type of book in the basket
    counts = Counter(basket)

    # Calculate the total cost before applying any discounts
    subtotal = sum([prices[counts[book]] for book in set(basket)])

    # Determine the size of the largest group of unique books
    max_group_size = len(set(basket))

    # Apply the appropriate discount based on the size of the largest group
    if max_group_size >= 5:
        discount = 0.25
    elif max_group_size >= 4:
        discount = 0.2
    elif max_group_size >= 3:
        discount = 0.1
    else:
        discount = 0

    # Return the final price after discounts have been applied
    return subtotal * (1 - discount)

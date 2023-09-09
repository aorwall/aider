from itertools import combinations

def total(basket):
    # Initialize basic price
    total = len(basket) * 8
    
    # Find all unique books
    unique_books = set(basket)
    
    if not unique_books:
        return 0
    
    if len(unique_books) == 1:
        # No discount
        return total
    
    # Find all possible combinations of books
    combos = []
    for i in range(1, len(unique_books)+1):
        combos.extend(combinations(unique_books, i))
    
    # Calculate discount for each combo
    prices = []
    for combo in combos:
        books = len(combo)
        if books == 1:
            price = books * 8
        elif books == 2:
            price = books * 8 * 0.95
        elif books == 3:
            price = books * 8 * 0.9
        elif books == 4:
            price = books * 8 * 0.8
        elif books == 5:
            price = books * 8 * 0.75
        
        prices.append(price)
    
    # Return minimum price
    return min(prices)

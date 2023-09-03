def total(basket):
    # Calculate the total cost of the books in the basket
    total_cost = 0
    for book in basket:
        total_cost += book.price

    # Apply the discounts
    if len(basket) >= 5:
        total_cost *= 0.75
    elif len(basket) >= 4:
        total_cost *= 0.9
    elif len(basket) >= 3:
        total_cost *= 0.95
    elif len(basket) >= 2:
        total_cost *= 0.98

    return total_cost

def main():
    # Create a list of books
    books = [
        Book("Book 1", 8),
        Book("Book 2", 8),
        Book("Book 3", 8),
        Book("Book 4", 8),
        Book("Book 5", 8)
    ]

    # Create a basket of books
    basket = [
        books[0],
        books[1],
        books[2],
        books[3],
        books[4]
    ]

    # Calculate the total cost of the basket
    total_cost = total(basket)

    # Print the total cost
    print(f"Total cost: {total_cost}")

if __name__ == "__main__":
    main()

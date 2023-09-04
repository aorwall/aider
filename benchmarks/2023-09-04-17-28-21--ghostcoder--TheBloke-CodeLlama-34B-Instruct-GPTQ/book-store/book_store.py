def total(basket):
    # Calculate the number of unique books in the basket
    unique_books = len(set(basket))

    # Initialize the total cost to 0
    total_cost = 0

    # Check if there are any duplicate books in the basket
    if len(basket) > unique_books:
        # If so, calculate the number of duplicates for each book
        dupes = [basket.count(book) for book in set(basket)]

        # Sort the list of duplicates in descending order
        sorted_dupes = sorted(dupes, reverse=True)

        # Iterate over the sorted list of duplicates
        for i, num_dupes in enumerate(sorted_dupes):
            # Calculate the discount based on the number of duplicates
            discount = 0
            if num_dupes >= 4:
                discount = 0.2
            elif num_dupes == 3:
                discount = 0.1
            elif num_dupes == 2:
                discount = 0.05

            # Calculate the cost of the current book
            cost = 8 * (1 - discount)

            # Add the cost of the current book to the total cost
            total_cost += cost * num_dupes

            # Remove the current book from the basket
            basket.remove(list(set(basket))[i])

    # Return the total cost
    return total_cost

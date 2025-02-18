def sum_of_multiples(limit, multiples):
    """Return the sum of unique multiples of multiple numbers up to but not including limit."""
    # Initialize an empty set to store the unique multiples
    unique_multiples = set()

    # Iterate over the list of factors
    for factor in multiples:
        if factor != 0:
            # Find the multiples of the current factor
            for multiple in range(factor, limit, factor):
                # Add the multiple to the set of unique multiples
                unique_multiples.add(multiple)

    # Return the sum of the unique multiples
    return sum(unique_multiples)

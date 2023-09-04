from typing import List

def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    """Calculates the sum of unique multiples of the given factors within the limit."""

    # Initialize an empty set to store the unique multiples
    unique_multiples = set()

    # Iterate through the factors
    for factor in multiples:

        # Find all the unique multiples of this factor up to the limit
        current_multiple = factor
        while current_multiple < limit:
            unique_multiples.add(current_multiple)
            current_multiple += factor

    # Return the sum of the unique multiples
    return sum(unique_multiples)
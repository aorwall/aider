def distance(strand_a, strand_b):
    """
    Calculate the Hamming distance between two DNA strands.
    
    Args:
        strand_a (str): First DNA strand.
        strand_b (str): Second DNA strand.
    
    Returns:
        int: The number of positions at which the corresponding symbols are different.
    
    Raises:
        ValueError: If the input strings are not of equal length.
    """
    # Check if the input strings are of equal length.
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    # Initialize the counter for the number of differences.
    diff_count = 0

    # Iterate over each symbol pair in the input strings.
    for char_a, char_b in zip(strand_a, strand_b):
        # Increment the difference counter if the characters are different.
        if char_a != char_b:
            diff_count += 1

    # Return the final difference count.
    return diff_count

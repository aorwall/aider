def distance(strand_a, strand_b):
    """Calculate the Hamming Distance between two DNA strands."""

    # Check if lengths of strands are equal
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    # Calculate the Hamming Distance by counting differences
    return sum(el_a != el_b for el_a, el_b in zip(strand_a, strand_b))

def distance(strand_a, strand_b):
    """Calculate the Hamming distance between two DNA strands."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    count = sum([1 for i in range(len(strand_a)) if strand_a[i] != strand_b[i]])
    return count

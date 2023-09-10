def hamming_distance(dna_strand_1, dna_strand_2):
    """
    Given two DNA strands, calculate the Hamming distance between them.

    The Hamming distance is the number of differences between the two DNA strands.

    Args:
        dna_strand_1 (str): The first DNA strand.
        dna_strand_2 (str): The second DNA strand.

    Returns:
        int: The Hamming distance between the two DNA strands.
    """

    # Check that the two DNA strands are of equal length.
    if len(dna_strand_1) != len(dna_strand_2):
        raise ValueError("The two DNA strands must be of equal length.")

    # Initialize the Hamming distance to 0.
    hamming_distance = 0

    # Iterate over the two DNA strands, one character at a time.
    for i in range(len(dna_strand_1)):
        # If the two characters are different, increment the Hamming distance.
        if dna_strand_1[i] != dna_strand_2[i]:
            hamming_distance += 1

    # Return the Hamming distance.
    return hamming_distance

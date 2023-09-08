def hamming_distance(dna_strand_1, dna_strand_2):
    """
    Calculate the Hamming distance between two DNA strands.

    Args:
        dna_strand_1 (str): DNA strand 1
        dna_strand_2 (str): DNA strand 2

    Returns:
        int: Hamming distance between the two strands
    """
    if len(dna_strand_1) != len(dna_strand_2):
        raise ValueError("Strands must have the same length")

    hamming_distance = 0
    for i in range(len(dna_strand_1)):
        if dna_strand_1[i] != dna_strand_2[i]:
            hamming_distance += 1

    return hamming_distance

def hamming_distance(dna_strand1, dna_strand2):
    """Calculate the Hamming difference between two DNA strands."""
    if len(dna_strand1) != len(dna_strand2):
        return None

    count = 0
    for i in range(len(dna_strand1)):
        if dna_strand1[i] != dna_strand2[i]:
            count += 1

    return count
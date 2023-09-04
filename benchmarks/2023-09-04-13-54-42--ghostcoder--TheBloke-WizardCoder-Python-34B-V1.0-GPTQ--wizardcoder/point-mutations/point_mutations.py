def hamming_distance(dna_strand_1, dna_strand_2):
    if len(dna_strand_1) != len(dna_strand_2):
        raise ValueError("Both strings must have the same length")

    count = 0
    for i in range(min(len(dna_strand_1), len(dna_strand_2))):
        if dna_strand_1[i] != dna_strand_2[i]:
            count += 1

    return count

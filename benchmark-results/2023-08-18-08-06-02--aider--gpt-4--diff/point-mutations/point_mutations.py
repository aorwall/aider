def hamming_distance(dna_strand_1, dna_strand_2):
    return sum(a != b for a, b in zip(dna_strand_1, dna_strand_2))

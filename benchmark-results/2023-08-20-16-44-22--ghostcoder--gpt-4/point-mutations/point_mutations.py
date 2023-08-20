def hamming_distance(dna_strand_1, dna_strand_2):
    return sum(el1 != el2 for el1, el2 in zip(dna_strand_1, dna_strand_2))
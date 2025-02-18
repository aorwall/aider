def hamming_distance(dna_strand_1, dna_strand_2):
    assert len(dna_strand_1) == len(dna_strand_2), "DNA strands must be of same length"
    return sum([el1 != el2 for el1, el2 in zip(dna_strand_1[:len(dna_strand_2)], dna_strand_2)])

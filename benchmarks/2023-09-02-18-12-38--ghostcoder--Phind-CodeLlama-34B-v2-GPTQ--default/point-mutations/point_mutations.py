def hamming_distance(dna_strand_1, dna_strand_2):

    return sum(el_1 != el_2 for el_1, el_2 in zip(dna_strand_1[:min(len(dna_strand_1), len(dna_strand_2))], dna_strand_2[:min(len(dna_strand_1), len(dna_strand_2))]))

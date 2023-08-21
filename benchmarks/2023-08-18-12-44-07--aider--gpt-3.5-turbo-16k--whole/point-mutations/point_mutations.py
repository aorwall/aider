def hamming_distance(dna_strand_1, dna_strand_2):
    distance = 0
    for base1, base2 in zip(dna_strand_1, dna_strand_2):
        if base1 != base2:
            distance += 1
    
    return distance

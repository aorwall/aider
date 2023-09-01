def hamming_distance(dna_strand_1, dna_strand_2):
    if len(dna_strand_1) != len(dna_strand_2):
        raise ValueError("Strands must be of equal length.")
    distance = 0
    for i in range(len(dna_strand_1)):
        if dna_strand_1[i] != dna_strand_2[i]:
            distance += 1
    return distance
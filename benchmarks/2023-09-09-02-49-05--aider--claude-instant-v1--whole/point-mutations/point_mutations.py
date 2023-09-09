from math import min

def hamming_distance(dna_strand_1, dna_strand_2):
    length = min(len(dna_strand_1), len(dna_strand_2))
    
    distance = 0
    for i in range(length):
        if dna_strand_1[i] != dna_strand_2[i]:
            distance += 1
    return distance

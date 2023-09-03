def hamming_distance(dna_strand_1, dna_strand_2):
    count = 0
    for i in range(min(len(dna_strand_1), len(dna_strand_2))):
        if dna_strand_1[i] != dna_strand_2[i]:
            count += 1

    count += abs(len(dna_strand_1) - len(dna_strand_2)) # add difference in length as mismatches

    return count

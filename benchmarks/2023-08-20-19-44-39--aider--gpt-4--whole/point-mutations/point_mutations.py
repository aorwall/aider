import itertools

def hamming_distance(dna_strand_1, dna_strand_2):
    return sum(nucleotide_1 != nucleotide_2 for nucleotide_1, nucleotide_2 in itertools.zip_longest(dna_strand_1, dna_strand_2, fillvalue=None))

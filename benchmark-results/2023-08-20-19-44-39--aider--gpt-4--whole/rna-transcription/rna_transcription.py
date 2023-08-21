def to_rna(dna_strand):
    dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join([dna_to_rna[nucleotide] for nucleotide in dna_strand])

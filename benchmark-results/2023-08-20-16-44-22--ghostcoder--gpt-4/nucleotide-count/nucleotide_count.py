def count(strand, nucleotide):
    if nucleotide not in 'ACGT':
        raise ValueError("Invalid Nucleotide")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    return {'A': count(strand, 'A'), 'C': count(strand, 'C'), 'G': count(strand, 'G'), 'T': count(strand, 'T')}
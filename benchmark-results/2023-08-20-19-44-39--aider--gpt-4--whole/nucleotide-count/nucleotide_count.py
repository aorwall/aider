def count(strand, nucleotide):
    if not all(x in 'ACGT' for x in strand):
        raise ValueError("Invalid strand")
    if nucleotide not in 'ACGT':
        raise ValueError("Invalid nucleotide")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    if not all(x in 'ACGT' for x in strand):
        raise ValueError("Invalid strand")
    return {'A': strand.count('A'), 'C': strand.count('C'), 'G': strand.count('G'), 'T': strand.count('T')}

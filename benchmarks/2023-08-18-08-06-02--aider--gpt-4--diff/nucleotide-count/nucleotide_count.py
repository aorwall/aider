def count(strand, nucleotide):
    if not all(n in 'ACGT' for n in strand + nucleotide):
        raise ValueError("Invalid DNA sequence")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    if not all(n in 'ACGT' for n in strand):
        raise ValueError("Invalid DNA sequence")
    return {'A': strand.count('A'), 'C': strand.count('C'), 'G': strand.count('G'), 'T': strand.count('T')}

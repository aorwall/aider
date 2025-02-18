def count(strand, nucleotide):
    """Count the number of occurrences of a nucleotide in a strand of DNA."""
    if nucleotide not in ['A', 'C', 'G', 'T']:
        raise ValueError("Invalid nucleotide")

    return strand.count(nucleotide)


def nucleotide_counts(strand):
    """Return a dictionary containing counts for each nucleotide in a strand of DNA."""
    if not all([n in ['A', 'C', 'G', 'T'] for n in set(strand)]):
        raise ValueError("Invalid character in DNA strand.")

    return {'A': count(strand, 'A'), 'C': count(strand, 'C'), 'G': count(strand, 'G'), 'T': count(strand, 'T')}

def count(strand, nucleotide):
    if nucleotide not in ['A', 'C', 'G', 'T']:
        raise ValueError("Invalid nucleotide")
    return strand.count(nucleotide)


def nucleotide_counts(strand):
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in strand:
        counts[nucleotide] += 1
    return counts
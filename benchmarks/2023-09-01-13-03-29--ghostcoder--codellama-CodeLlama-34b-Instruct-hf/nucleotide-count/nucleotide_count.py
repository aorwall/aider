def count(strand, nucleotide):
    if nucleotide not in ['A', 'C', 'G', 'T']:
        raise ValueError("Invalid nucleotide")
    count = 0
    for base in strand:
        if base == nucleotide:
            count += 1
    return count


def nucleotide_counts(strand):
    counts = {
        'A': count(strand, 'A'),
        'C': count(strand, 'C'),
        'G': count(strand, 'G'),
        'T': count(strand, 'T')
    }
    return counts

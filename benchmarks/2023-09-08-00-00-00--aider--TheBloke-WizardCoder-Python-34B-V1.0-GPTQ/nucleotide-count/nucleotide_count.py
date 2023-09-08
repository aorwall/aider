def count(strand, nucleotide):
    if nucleotide not in "ACGT":
        raise ValueError("Invalid nucleotide")
    return strand.count(nucleotide)

def nucleotide_counts(strand):
    counts = {}
    for nucleotide in "ACGT":
        counts[nucleotide] = count(strand, nucleotide)
    return counts

def count(strand, nucleotide):
    return strand.upper().count(nucleotide)

def nucleotide_counts(strand):
    valid_chars = {'A', 'C', 'G', 'T'}

    # Check if there are any invalid characters in the strand
    if any((char not in valid_chars) for char in strand.upper()):
        raise ValueError('Invalid character found in DNA sequence')

    counts = {}
    for nucleotide in valid_chars:
        counts[nucleotide] = count(strand, nucleotide)

    return counts

def count(strand, nucleotide):
    """Counts the number of occurrences of a specific nucleotide in a given strand."""
    valid_chars = set('ACGT')
    if not all(c in valid_chars for c in strand):
        raise ValueError("Invalid DNA strand")

    count = 0
    for char in strand:
        if char == nucleotide:
            count += 1

    return count


def nucleotide_counts(strand):
    """Returns a dictionary with the count of each nucleotide in a given strand."""
    valid_chars = set('ACGT')
    if not all(c in valid_chars for c in strand):
        raise ValueError("Invalid DNA strand")

    counts = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0
    }

    for char in strand:
        counts[char] += 1

    return counts

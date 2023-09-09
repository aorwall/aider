def count(strand, nucleotide):
    if not all(char in "ACGT" for char in strand):
        raise ValueError("Invalid DNA sequence")

    return strand.count(nucleotide)


def nucleotide_counts(strand):
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}

    for char in strand:
        if char not in counts:
            raise ValueError("Invalid DNA sequence")
        counts[char] += 1

    return counts

def count(strand, nucleotide):
    """
    Returns the number of occurrences of a nucleotide in a strand.
    
    Args:
        strand (string): The DNA strand to search.
        nucleotide (char): The nucleotide to search for.
        
    Returns:
        int: The number of times the nucleotide appears in the strand.
    """
    # Check if the input strand is valid
    if len(strand) > 0 and all([c in ["A", "C", "G", "T"] for c in strand]):
        # Count the number of occurrences of the specified nucleotide
        count = sum([1 for c in strand if c == nucleotide])
        return count
    else:
        raise ValueError("Invalid strand")


def nucleotide_counts(strand):
    """
    Returns a dictionary containing the counts of each nucleotide in a strand.
    
    Args:
        strand (string): The DNA strand to analyze.
        
    Returns:
        dict: A dictionary where keys are nucleotides ('A', 'C', 'G', 'T') and values are their respective counts.
    """
    # Initialize an empty dictionary to store the counts
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}

    # Iterate over the strand and increment the count for each nucleotide
    for c in strand:
        if c in counts:
            counts[c] += 1

    return counts

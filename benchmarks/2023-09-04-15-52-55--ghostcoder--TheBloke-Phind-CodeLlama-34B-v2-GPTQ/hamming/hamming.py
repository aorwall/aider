def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return sum(el_a != el_b for el_a, el_b in zip(strand_a, strand_b))

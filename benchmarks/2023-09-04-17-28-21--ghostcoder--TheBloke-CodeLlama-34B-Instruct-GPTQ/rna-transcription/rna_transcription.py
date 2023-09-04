def to_rna(dna_strand):
    # Create a dictionary to map the base pairing
    dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}

    # Use list comprehension to translate the DNA strand into RNA
    rna_strand = ''.join([dna_to_rna[base] for base in dna_strand])

    return rna_strand

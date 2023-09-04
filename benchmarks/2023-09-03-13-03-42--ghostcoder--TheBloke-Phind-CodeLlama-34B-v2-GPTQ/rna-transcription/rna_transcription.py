def to_rna(dna_strand):
    # Create a dictionary where keys are DNA characters and values are their corresponding RNA characters
    dna_to_rna = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}

    # Use list comprehension to convert each character in the DNA strand to its RNA equivalent
    rna_strand = ''.join([dna_to_rna[base] for base in dna_strand])

    return rna_strand

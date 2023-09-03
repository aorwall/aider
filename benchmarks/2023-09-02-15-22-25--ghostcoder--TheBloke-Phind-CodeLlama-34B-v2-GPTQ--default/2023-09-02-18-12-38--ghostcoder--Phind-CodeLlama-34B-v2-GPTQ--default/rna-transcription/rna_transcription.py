def to_rna(dna_strand):
    # Create a dictionary that maps each DNA nucleotide to its corresponding RNA nucleotide
    dna_to_rna = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}

    # Use a list comprehension to convert each nucleotide in the DNA strand
    rna_strand = ''.join([dna_to_rna[nucleotide] for nucleotide in dna_strand])

    return rna_strand

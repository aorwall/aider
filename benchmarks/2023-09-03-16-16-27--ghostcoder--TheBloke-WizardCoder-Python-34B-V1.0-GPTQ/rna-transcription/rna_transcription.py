def to_rna(dna_strand):
    """
    Transcribes a DNA strand into its corresponding RNA strand.
    
    Args:
      dna_strand (str): A string representing a DNA strand.
    Returns:
      The RNA strand obtained by replacing each nucleotide in the input DNA strand with its complementary nucleotide.
    """
    mapping = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna_strand = ''
    for nucleotide in dna_strand:
        if nucleotide in mapping:
            rna_strand += mapping[nucleotide]
        else:
            raise ValueError('Invalid DNA strand')
    return rna_strand

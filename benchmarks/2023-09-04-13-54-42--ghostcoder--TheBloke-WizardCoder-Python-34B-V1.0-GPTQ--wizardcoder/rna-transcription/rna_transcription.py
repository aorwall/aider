def to_rna(dna_strand):
    mapping = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return ''.join([mapping[char] for char in dna_strand])

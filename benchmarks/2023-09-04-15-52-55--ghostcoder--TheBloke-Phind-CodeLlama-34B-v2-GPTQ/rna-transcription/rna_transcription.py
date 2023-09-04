def to_rna(dna_strand):
    dna_to_rna = {
        "A": "U",
        "C": "G",
        "G": "C",
        "T": "A"
    }

    return ''.join([dna_to_rna[base] for base in dna_strand])

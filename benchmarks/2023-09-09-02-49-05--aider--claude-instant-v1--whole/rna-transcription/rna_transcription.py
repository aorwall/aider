def to_rna(dna_strand):
    rna = ""
    for nucleotide in dna_strand:
        if nucleotide == "G":
            rna += "C"
        elif nucleotide == "C":
            rna += "G" 
        elif nucleotide == "T":
            rna += "A"
        elif nucleotide == "A":
            rna += "U"
    return rna

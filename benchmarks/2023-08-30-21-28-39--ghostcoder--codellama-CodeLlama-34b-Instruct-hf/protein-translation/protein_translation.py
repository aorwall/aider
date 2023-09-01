def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    amino_acids = []
    for codon in codons:
        if codon == "AUG":
            amino_acids.append("Methionine")
        elif codon == "UUU" or codon == "UUC":
            amino_acids.append("Phenylalanine")
        elif codon == "UUA" or codon == "UUG":
            amino_acids.append("Leucine")
        elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
            amino_acids.append("Serine")
        elif codon == "UAU" or codon == "UAC":
            amino_acids.append("Tyrosine")
        elif codon == "UGU" or codon == "UGC":
            amino_acids.append("Cysteine")
        elif codon == "UGG":
            amino_acids.append("Tryptophan")
        elif codon == "UAA" or codon == "UAG" or codon == "UGA":
            break
    return amino_acids

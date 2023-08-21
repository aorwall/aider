def proteins(strand):
    codon_protein_map = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }

    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    proteins = []
    for codon in codons:
        protein = codon_protein_map.get(codon)
        if protein == "STOP":
            break
        if protein:
            proteins.append(protein)
    return proteins

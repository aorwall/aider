def proteins(strand):
    codon_table = {
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

    protein_sequence = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        if codon in codon_table:
            if codon_table[codon] == "STOP":
                break
            protein_sequence.append(codon_table[codon])

    return protein_sequence

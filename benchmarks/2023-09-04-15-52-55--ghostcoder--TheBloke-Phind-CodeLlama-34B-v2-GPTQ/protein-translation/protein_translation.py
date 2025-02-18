def proteins(rna_sequence):
    genetic_code = {
        "AUG": "Methionine", "UUU": "Phenylalanine", "UUC": "Phenylalanine",
        "UUA": "Leucine", "UUG": "Leucine", "UCU": "Serine", "UCC": "Serine",
        "UCA": "Serine", "UCG": "Serine", "UAU": "Tyrosine", "UAC": "Tyrosine",
        "UGU": "Cysteine", "UGC": "Cysteine", "UGG": "Tryptophan",
        "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
    }

    proteins = []
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        aminoacid = genetic_code.get(codon, None)
        if aminoacid == "STOP":
            break
        else:
            proteins.append(aminoacid)

    return proteins
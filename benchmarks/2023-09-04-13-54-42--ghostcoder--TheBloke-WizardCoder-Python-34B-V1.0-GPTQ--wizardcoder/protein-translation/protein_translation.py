def proteins(rna_sequence):
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
        "UAA": "",
        "UAG": "",
        "UGA": ""
    }

    rna_sequence = rna_sequence.upper()
    protein_list = []
    current_codon = ""

    for base in rna_sequence:
        current_codon += base
        if len(current_codon) == 3:
            amino_acid = codon_table[current_codon]

            if amino_acid != "":
                protein_list.append(amino_acid)
            else:
                break

            current_codon = ""

    return protein_list
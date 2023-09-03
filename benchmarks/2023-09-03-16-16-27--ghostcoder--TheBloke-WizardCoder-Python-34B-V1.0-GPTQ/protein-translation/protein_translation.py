def proteins(strand):
    codon_table = {
        'AUG': 'Methionine',
        'UUUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
        'UUA': 'Leucine', 'UUG': 'Leucine',
        'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
        'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
        'UGU': 'Cysteine', 'UGC': 'Cysteine',
        'UGG': 'Tryptophan'
    }

    rna_codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    amino_acids = []
    for codon in rna_codons:
        if codon in codon_table:
            amino_acid = codon_table[codon]
            if amino_acid == 'Stop':
                break
            else:
                amino_acids.append(amino_acid)
    return amino_acids

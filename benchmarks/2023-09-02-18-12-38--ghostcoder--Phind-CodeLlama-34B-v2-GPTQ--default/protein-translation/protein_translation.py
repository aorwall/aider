def proteins(strand):
    codon_table = {
        'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
        'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine',
        'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
        'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan',
        'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
    }

    protein_list = []
    for i in range(0, len(strand), 3):
        if codon_table[strand[i:i+3]] != 'STOP':
            protein_list.append(codon_table[strand[i:i+3]])
        else:
            break

    return protein_list
